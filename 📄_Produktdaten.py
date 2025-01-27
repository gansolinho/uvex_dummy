import streamlit as st
import pandas as pd

# Konfigruation festlegen
st.set_page_config(
    page_title="Produktdaten",
    page_icon="📄",
)

# Logo
st.logo('images/logos/Uvex_logo.svg', size='large', icon_image='images/logos/uvex_logo_black.svg')

# Page-Überschrift
st.write("# Produktdaten 📄")

# Artikel Name
st.write("## Jacke suXXeed industry")

# Tabs aufmachen
tab1, tab2, tab3 = st.tabs(["Artikelinformationen", "Produktbilder", "Technische Informationen"])

# Tab 1
with tab1:
    # Allgemeine Infos
    st.write("#### Allgemeine Informationen")

    # Weitere Spalten festlegen
    col1b, col2b, col3b, col4b, col5b, col6b = st.columns(6)

    # Allgemeine Infos
    col1b.write("Artikelnr.:")
    col1b.write("EAN / UPC:")
    col1b.write("Größe:")
    col1b.write("Farbe:")
    col1b.write("Preis:")
    col1b.write("Verkaufsjahr:")
    col1b.write("Nettogewicht:")
    col2b.write("8854811")
    col2b.write("4049358590111")
    col2b.write("L")
    col2b.write("anthrazit")
    col2b.write("27,00 Euro")
    col2b.write("2025")
    col2b.write("0,850 kg")

    # Allgemeine Merkmale
    st.write("#### Allgemeine Merkmale")
    st.markdown('''
        - Sportive workwear-Jacke, das Gewebe mit Stretchanteil sorgt für angenehmen Tragekomfort
        - High-rise Armkonstruktion
        - Stehkragen
        - verlängertes Rückenteil
        - Reflexdetails
        - Alle Verschlusselemente sind abgedeckt
        - Zwei verschließbare Brusttaschen, 1 verschließbare Innentasche, 2 Seitentaschen
        - Ärmelsaumweite verstellbar
        ''')

    # Komfortmerkmale
    st.write("#### Komfortmerkmale")
    st.markdown('''
        - Dehnelemente im Rücken, am Bund und an den Ärmel sorgen für hohen Tragekomfort
        - Ergonomische Linienführung für mehr Bewegungsfreiheit
        - Ausgezeichnete Passform
        ''')

    # Einsatzgebiete
    st.write("#### Einsatzgebiete")
    st.markdown('''
        - Arbeit und Freizeit
        - Indoorworker
        - Automobilindustrie
        ''')

    # Pflegehinweis
    st.write("#### Pflegehinweis")
    st.markdown('''
        - Bügeln mit einer Höchsttemperatur der Bügeleisensohle von 150 °C
        - Industrial Wash 2, Nicht bleichen, Normalwaschgang 60°C
        - Professionelle Trockenreinigung mit Perchlorethylen und/oder Kohlenwasserstoffen
        - Trocknen im Tumbler/Trockner möglich, niedrige Temperatur 60 °C, schonender Trocknungsprozess
        ''')

# Tab 2
with tab2:
    # Produktbilder für gescanntes Produkt
    st.write("#### Produktfarbe: anthrazit")

    # Spalten festlegen
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    # Artikelbilder anzeigen
    col1.image('images/jacke_suXXeed_industry/anthrazit/jacke_bild_1.webp')
    col2.image('images/jacke_suXXeed_industry/anthrazit/jacke_bild_2.webp')
    col3.image('images/jacke_suXXeed_industry/anthrazit/jacke_bild_3.webp')
    col4.image('images/jacke_suXXeed_industry/anthrazit/jacke_bild_4.webp')
    col5.image('images/jacke_suXXeed_industry/anthrazit/jacke_bild_5.webp')
    col6.image('images/jacke_suXXeed_industry/anthrazit/jacke_bild_6.webp')

    # Trennstrich
    st.divider()

    # Weitere Farben
    st.write("#### Weitere Farben")

    # Produktbilder: Nachtblau
    st.write('##### nachtblau')

    # Spalten festlegen
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    # Artikelbilder anzeigen
    col1.image('images/jacke_suXXeed_industry/nachtblau/jacke_bild_1.webp')
    col2.image('images/jacke_suXXeed_industry/nachtblau/jacke_bild_2.webp')
    col3.image('images/jacke_suXXeed_industry/nachtblau/jacke_bild_3.webp')
    col4.image('images/jacke_suXXeed_industry/nachtblau/jacke_bild_4.webp')
    col5.image('images/jacke_suXXeed_industry/nachtblau/jacke_bild_5.webp')
    col6.image('images/jacke_suXXeed_industry/nachtblau/jacke_bild_6.webp')

    # Produktbilder: Ultramarin
    st.write("##### ultramarin")

    # Spalten festlegen
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    # Artikelbilder anzeigen
    col1.image('images/jacke_suXXeed_industry/ultramarin/jacke_bild_1.webp')
    col2.image('images/jacke_suXXeed_industry/ultramarin/jacke_bild_2.webp')
    col3.image('images/jacke_suXXeed_industry/ultramarin/jacke_bild_3.webp')
    col4.image('images/jacke_suXXeed_industry/ultramarin/jacke_bild_4.webp')
    col5.image('images/jacke_suXXeed_industry/ultramarin/jacke_bild_5.webp')
    col6.image('images/jacke_suXXeed_industry/ultramarin/jacke_bild_6.webp')

    # Produktbilder: Graphit
    st.write("##### graphit")

    # Spalten festlegen
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    # Artikelbilder anzeigen
    col1.image('images/jacke_suXXeed_industry/graphit/jacke_bild_1.webp')
    col2.image('images/jacke_suXXeed_industry/graphit/jacke_bild_2.webp')
    col3.image('images/jacke_suXXeed_industry/graphit/jacke_bild_3.webp')
    col4.image('images/jacke_suXXeed_industry/graphit/jacke_bild_4.webp')
    col5.image('images/jacke_suXXeed_industry/graphit/jacke_bild_5.webp')
    col6.image('images/jacke_suXXeed_industry/graphit/jacke_bild_6.webp')

    # Produktbilder: Rot
    st.write("##### rot")

    # Spalten festlegen
    col1, col2, col3, col4, col5, col6 = st.columns(6)

    # Artikelbilder anzeigen
    col1.image('images/jacke_suXXeed_industry/rot/jacke_bild_1.webp')
    col2.image('images/jacke_suXXeed_industry/rot/jacke_bild_2.webp')
    col3.image('images/jacke_suXXeed_industry/rot/jacke_bild_3.webp')
    col4.image('images/jacke_suXXeed_industry/rot/jacke_bild_4.webp')
    col5.image('images/jacke_suXXeed_industry/rot/jacke_bild_5.webp')
    col6.image('images/jacke_suXXeed_industry/rot/jacke_bild_6.webp')

# Tab 3
with tab3:
    # Technische Informationen
    st.write("#### Technische Informationen")

    # Daten als Dictionary
    technical_info = {
        "Eigenschaft": [
            "Produktart",
            "Produkttyp",
            "Produkttyp Untertypen",
            "Produktname",
            "Produktfamilie",
            "Größe",
            "Geschlecht",
            "Passform",
            "Farbe",
            "Marketingfarbe",
            "Verschluss",
            "Material Verschluss",
            "Material Oberstoff 1",
            "Material Oberstoff 1 inkl. Anteil",
            "Flächengewicht Oberstoff 1",
            "Material Oberstoff 2",
            "Material Oberstoff 2 inkl. Anteil",
            "Flächengewicht Oberstoff 2",
            "Zertifikate",
            "Eignung für Arbeitsumgebung"
        ],
        "Wert": [
            "Arbeitskleidung",
            "Jacke",
            "Arbeitsjacke",
            "Jacke",
            "uvex suXXeed industry",
            "S - 6XL",
            "Herren",
            "Regular Fit",
            "blau, grau, rot",
            "nachtblau, ultramarin, anthrazit, graphit",
            "Reißverschluss",
            "Kunststoff",
            "Baumwolle, Elasthan®, Polyester",
            "49 % Baumwolle, 49 % Polyester, 2 % Elasthan®",
            "0,260 kg",
            "Polyester",
            "100 % Polyester",
            "0,490 kg",
            "STANDARD 100 by OEKO-TEX®",
            "staubig, trocken"
        ]
    }

    # DataFrame erstellen
    df_technical_info = pd.DataFrame(technical_info)

    # Tabelle ausgeben
    st.dataframe(df_technical_info, hide_index=True, use_container_width=True)