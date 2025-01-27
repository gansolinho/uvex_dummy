import streamlit as st
import pandas as pd
import folium
import leafmap.foliumap as leafmap
import plotly.express as px

# Konfiguration festlegen
st.set_page_config(
    page_title="Unternehmen",
    page_icon="🏭",
    initial_sidebar_state="expanded"
)

# Logo
st.logo('images/logos/Uvex_logo.svg', size='large', icon_image='images/logos/uvex_logo_black.svg')

# Page-Überschrift
st.write("# Unternehmen 🏭")

# Uvex Group Logo
st.image('images/logos/uvex_group_logo.svg')

# Tabs aufmachen
tab1, tab2, tab3, tab4 = st.tabs(["Geschäftszahlen", "Philosophie", "Geschichte", "Standorte"])

# Tab 1
with tab1:
    # Überschrift
    st.write("### Geschäftszahlen der UVEX Group")

    # Definieren von Color Maps
    division_color_map = {
        "UVEX Safety": "#98d83e",
        "UVEX Sports": "#25ac82",
        "UVEX Group": "#2b748e"
    }

    national_international_color_map = {
        "Inland": "#90e0ef",
        "Ausland": "#00b4d8"
    }

    # Sales Daten als Liniendiagramm ausgeben
    sales_data_new = pd.DataFrame(
        {
            "Geschäftszahlen": [
                "UVEX Group",
                "UVEX Safety",
                "UVEX Sports"
            ],
            '16/17': [426, 310, 122],
            '17/18': [453, 334, 126],
            '18/19': [475, 352, 131],
            '19/20': [480, 365, 128],
            '20/21': [524, 399, 142],
            '21/22': [585, 445, 148],
            '22/23': [655, 522, 139],
            '23/24': [666, 546, 126]
        }
    )

    # Umwandeln in ein langes Format für Plotly
    df_long = sales_data_new.melt(id_vars='Geschäftszahlen', var_name='Geschäftsjahr', value_name='Umsatz')

    # Liniendiagramm erstellen
    fig_sales_data = px.line(
        df_long,
        x='Geschäftsjahr',
        y='Umsatz',
        title='Konsolidierte Geschäftszahlen im Zeitverlauf',
        color='Geschäftszahlen',
        labels={'Geschäftsjahr': 'Geschäftsjahr', 'Wert': 'Wert in Einheiten'},
        color_discrete_map=division_color_map
    )

    # Anpassung der Achsen und Limits
    fig_sales_data.update_layout(
        yaxis=dict(range=[0, 700], title=None),  # y-Achse: Limits von 0 bis 700, keine Überschrift
        paper_bgcolor="#F8F9FB",  # Grauer Rahmen
        plot_bgcolor="white",  # Weißes Diagramm
        margin=dict(l=50, r=50, t=50, b=50),  # Platz für den Rahmen schaffen
    )

    # Y-Achse formatieren mit "Mio. €"
    fig_sales_data.update_yaxes(
        tickformat=".0s",  # Zahl als wissenschaftliche Notation formatieren
        ticksuffix=" Mio. €"  # Zusatz "Mio. €" anfügen
    )

    # Liniendiagramm ausgeben
    st.plotly_chart(fig_sales_data, use_container_width=True)

    # Daten als Dictionary
    sales_division_data = {
        "Unternehmen": [
            "UVEX Safety", 
            "UVEX Sports", 
        ],
        "16/17": [73.0, 27.0],
        "17/18": [74.0, 26.0],
        "18/19": [74.0, 26.0],
        "19/20": [76.0, 24.0],
        "20/21": [76.0, 24.0],
        "21/22": [75.0, 25.0],
        "22/23": [79.0, 21.0],
        "23/24": [81.0, 19.0],
    }

    # DataFrame erstellen
    df_sales_division = pd.DataFrame(sales_division_data)

    # Umstrukturierung der Daten (Melt), um für jedes Jahr eine Zeile zu haben
    df_melted_sales_division = df_sales_division.melt(id_vars=["Unternehmen"], var_name="Jahr", value_name="Wert")

    # Erstellen des gestapelten Balkendiagramms
    fig_sales_divison = px.bar(df_melted_sales_division, 
        x="Jahr", 
        y="Wert", 
        color="Unternehmen", 
        title="Umsatzanteile der Sparten",
        labels={"Wert": "Umsatzanteil", "Jahr": "Geschäftsjahr"},
        color_discrete_map=division_color_map
    )

    # Anpassung der Achsen und Limits
    fig_sales_divison.update_layout(
        yaxis=dict(title=None),  # keine Überschrift
        paper_bgcolor="#F8F9FB",  # Grauer Rahmen
        plot_bgcolor="white",  # Weißes Diagramm
        margin=dict(l=50, r=50, t=50, b=50),  # Platz für den Rahmen schaffen
    )

    # Y-Achse mit Prozentzeichen formatieren
    fig_sales_divison.update_yaxes(tickformat="%d", ticksuffix=" %")

    # Gestapeltes Balkendiagramm ausgeben
    st.plotly_chart(fig_sales_divison, use_container_width=True)

    # Daten als Dictionary
    sales_national_international_data = {
        "Inland/Ausland": [
            "Inland", 
            "Ausland", 
        ],
        "16/17": [52.0, 48.0],
        "17/18": [53.0, 47.0],
        "18/19": [54.0, 46.0],
        "19/20": [53.0, 47.0],
        "20/21": [54.0, 46.0],
        "21/22": [46.0, 54.0],
        "22/23": [42.0, 58.0],
        "23/24": [40.0, 60.0],
    }

    # DataFrame erstellen
    df_sales_national_international = pd.DataFrame(sales_national_international_data)

    # Umstrukturierung der Daten (Melt), um für jedes Jahr eine Zeile zu haben
    df_melted_sales_national_international = df_sales_national_international.melt(id_vars=["Inland/Ausland"], var_name="Jahr", value_name="Wert")

    # Erstellen des gestapelten Balkendiagramms
    fig_sales_national_international = px.bar(df_melted_sales_national_international, 
        x="Jahr", 
        y="Wert", 
        color="Inland/Ausland", 
        title="Umsatzanteile Inland vs. Ausland",
        labels={"Wert": "Umsatzanteil", "Jahr": "Geschäftsjahr"},
        color_discrete_map=national_international_color_map
    )

    # Anpassung der Achsen und Limits
    fig_sales_national_international.update_layout(
        yaxis=dict(title=None),  # keine Überschrift
        paper_bgcolor="#F8F9FB",  # Grauer Rahmen
        plot_bgcolor="white",  # Weißes Diagramm
        margin=dict(l=50, r=50, t=50, b=50),  # Platz für den Rahmen schaffen
    )

    # Y-Achse mit Prozentzeichen formatieren
    fig_sales_national_international.update_yaxes(tickformat="%d", ticksuffix=" %")

    # Gestapeltes Balkendiagramm ausgeben
    st.plotly_chart(fig_sales_national_international, use_container_width=True)

# Tab 2
with tab2:
    # Überschrift
    st.write("### Philosophie der UVEX Group")

    # Spalten aufstellen
    col1, col2 = st.columns(2)

    # Bilder einfügen
    col1.image('images/company/uvex_philosophie_1.png')
    col2.image('images/company/uvex_philosophie_2.png')

    # Text einfügen
    st.markdown('''
        Die uvex group ist ein mittelständisches Familienunternehmen mit der Mission **protecting people** – dem Schutz des Menschen in Beruf, Sport und Freizeit.
        Dieses Leitmotiv prägt die Entwicklung, Produktion und den Vertrieb innovativer Produkte und Dienstleistungen, die höchsten Qualitäts- und Sicherheitsstandards entsprechen.
    ''')

    st.markdown('''
        Durch intensive Forschungs- und Entwicklungsarbeit sowie moderne Fertigung in eigenen Werken sichert uvex die Zukunft seiner Marken.
        Der Austausch von Ideen und Know-how zwischen den Bereichen uvex sports und uvex safety fördert kontinuierliche Innovationen,
        die den Anforderungen der Kund:innen gerecht werden. Dabei legt das Unternehmen Wert auf nachhaltiges Handeln zum Schutz von Mensch und Umwelt.
    ''')

    st.markdown('''
        Die Unternehmenswerte – verantwortungsvoll, unternehmerisch sowie fordernd und fördernd – bilden die Grundlage für das tägliche Miteinander
        und den Umgang mit Mitarbeiter:innen, Kund:innen und Geschäftspartner:innen. Ein respektvoller Umgang und die Förderung der individuellen
        Entwicklung stehen dabei im Vordergrund.
    ''')

    st.markdown('''
        Mit dem Anspruch, Innovationsführer zu sein, setzt uvex auf kontinuierliches, solides Wachstum und eine ausgewogene Balance von Wachstum,
        Rendite und Risiko. Durch nachhaltiges Handeln und wertorientiertes Wachstum strebt das Unternehmen danach, weltweit auf dem Siegerpodest zu stehen.
    ''')

    st.markdown('''
        Die Vision der uvex group ist es, die Besten ihrer Branche zu sein, indem sie durch Innovationen und an Werten orientiertes Wachstum Maßstäbe setzt.
        Das Leitmotiv **protecting people** verbindet dabei die Geschäftsbereiche sports und safety und gibt die Richtung für die tägliche Arbeit vor – vom Produktdesign bis zur Kommunikation.
    ''')

# Tab 3
with tab3:
    # Überschrift
    st.write("### Geschichte der UVEX Group")

    # Spalten aufstellen
    col1, col2 = st.columns(2)

    # Bilder einfügen
    col1.image('images/company/uvex_history_1.png')
    col2.image('images/company/uvex_history_2.png')

    # Text einfügen
    st.markdown('''
        Die uvex group blickt auf eine beeindruckende Unternehmensgeschichte zurück, die 1926 mit der Gründung der Optischen-Industrie-Anstalt Philipp M. Winter in Fürth, Bayern, begann.
    ''')

    st.markdown('''
        1956 prägte Rainer Winter die Marke **uvex**, abgeleitet von "UltraViolet EXcluded", unter der fortan alle Sport- und Freizeitprodukte vertrieben wurden.
    ''')

    st.markdown('''
        In den folgenden Jahrzehnten expandierte das Unternehmen durch die Einführung und Übernahme weiterer Marken:
        - 1967: Einführung der Marke Filtral für modische Sonnenbrillen
        - 1980: Gründung der Tochtergesellschaft ALPINA in Derching
        - 1986: Gründung der Profas GmbH, heute bekannt als uvex safety gloves
        - 1987: Joint Venture mit laservision, seit 2004 eine 100%ige Tochter der uvex safety group
        - 2001: Übernahme des Arbeitsschutzschuh-Spezialisten "Heckel"
        - 2009: Einstieg in den Reitsport mit Athletinnen wie Ingrid Klimke und Isabell Werth
    ''')

    st.markdown('''
        Die dritte Generation trat mit Gabriele Grau (1981) und Michael Winter (1987) in das Familienunternehmen ein.
    ''')

    st.markdown('''
        1999 wurde Michael Winter Geschäftsführender Gesellschafter der uvex Winter Holding.
    ''')

    st.markdown('''
        2005 gründete das Unternehmen die uvex academy, die erste privatwirtschaftliche Ausbildungsinstitution im Bereich Arbeitsschutz und Persönliche Schutzausrüstung (PSA).
    ''')

    st.markdown('''
        2009 wurde uvex als "Marke des Jahrhunderts" für die konsequente Markenpflege des Produkts Skibrille ausgezeichnet.
    ''')

    st.markdown('''
        2014 feierte uvex große Erfolge bei den Olympischen Spielen in Sotschi mit 62 Medaillen und der Ausstattung von 450 Athlet:innen.
    ''')

    st.markdown('''
        Heute ist die uvex group ein international agierendes Unternehmen, das innovative Produkte und Dienstleistungen für den
        Schutz des Menschen in Beruf, Sport und Freizeit entwickelt, produziert und vertreibt.
    ''')

# Tab 4
with tab4:
    # Überschrift
    st.write("### Standorte der UVEX Group")

    # Einleitungstest
    st.markdown('''
        Die UVEX Group verfügt über **zehn deutsche Niederlassungen**. Jeder dieser Standorte trägt mit seiner Spezialisierung und Expertise
        zur Gesamtleistung der UVEX group bei und unterstreicht das Engagement des Unternehmens für Qualität und Innovation im Bereich des
        Schutzes von Menschen in Beruf, Sport und Freizeit.
    ''')

    # Locations with detailed HTML popups
    locations = [
        {"latitude": 49.48323444386772, "longitude": 10.95867820054877, "name": "Fürth Hardhöhe", "info": "<b>UVEX WINTER HOLDING GmbH</b><br>HQ & Verwaltung<br>Produktion von Arbeitsschutzbrillen"},
        {"latitude": 52.029175294725704, "longitude": 8.762831226109714, "name": "Bad Sulzuflen", "info": "<b>Primetta GmbH & Co. KG</b><br>Tochterunternehmen<br>Produktion von Sonnenbrillen & Lesehilfen"},
        {"latitude": 49.4922709258416, "longitude": 10.925112997155944, "name": "Fürth Burgfarrnbach", "info": "<b>Filtral GmbH & Co. Vertriebs KG</b><br>Tochterunternehmen<br>Vertrieb von Sonnenbrillen & Lesehilfen"},
        {"latitude": 50.48520378894244, "longitude": 12.383174012073193, "name": "Ellefeld", "info": "<b>UVEX Safety Textiles GmbH</b><br>Produktion von Berufskleidung"},
        {"latitude": 48.395282306544, "longitude": 11.087344866625655, "name": "Laimering", "info": "<b>ALPINA Sports GmbH</b><br>Tochterunternehmen<br>Logistikzentrum"},
        {"latitude": 49.19272955696746, "longitude": 12.80157052386513, "name": "Lederdorn", "info": "<b>UVEX Sports Lederdorn GmbH</b><br>Produktion von Skibrillen, Ski- & Reithelmen"},
        {"latitude": 53.246763809206, "longitude": 10.485021253159278, "name": "Lüneburg", "info": "<b>UVEX Safety Gloves GmbH & Co. KG</b><br>Produktion von Schutzhandschuhen"},
        {"latitude": 49.321858726492735, "longitude": 11.050024872567, "name": "Schwabach", "info": "<b>UVEX Safety Logistics GmbH</b><br>Logistikzentrum"},
        {"latitude": 49.508425729342875, "longitude": 10.979310529724874, "name": "Fürth Stadeln", "info": "<b>UVEX SPORTS GmbH & Co. KG</b><br>Logistikzentrum"},
        {"latitude": 48.28765649335756, "longitude": 11.263981354770966, "name": "Sulzemoos", "info": "<b>Alpina SPorts GmbH</b><br>Tochterunternehmen<br>HQ, Produktion, Logistik"}
    ]

    # Koordinatenliste erstellen
    coordinates = [(loc["latitude"], loc["longitude"]) for loc in locations]

    # Leafmap-Karte initialisieren
    m = leafmap.Map(center=(51.1657, 10.4515), zoom=6)

    # Marker für jede Location hinzufügen
    for loc in locations:
        folium.Marker(
            location=(loc["latitude"], loc["longitude"]),
            tooltip=f"{loc['name']}",
            popup=folium.Popup(loc["info"], max_width=300),  # Add HTML content
            icon=folium.Icon(color="black", icon="building", prefix="fa")
        ).add_to(m)

    # Karte in Streamlit anzeigen
    m.to_streamlit(height=600)