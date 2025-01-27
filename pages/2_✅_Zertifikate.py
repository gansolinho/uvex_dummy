import streamlit as st

# Konfiguration festlegen
st.set_page_config(
    page_title="Zertifikate",
    page_icon="✅",
)

# Logo
st.logo('images/logos/Uvex_logo.svg', size='large', icon_image='images/logos/uvex_logo_black.svg')

# Page-Überschrift
st.write("# Zertifikate ✅")

# Tabs aufmachen
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Oeko Tex", "OHRIS", "ISO 9001", "ISO 14001", "ISO 45001", "ISO 50001"])

# Tab 1
with tab1:
    # Spalten aufmachen
    col1, col2, col3 = st.columns(3)

    # Bild einfügen
    col2.image('images/certificates/oeko_tex.png')

    # Text einfügen
    st.markdown('''
        Der **OEKO-TEX® Standard 100** ist ein weltweit einheitliches, unabhängiges Prüf- und Zertifizierungssystem für textile Roh-, Zwischen- und Endprodukte
        sowie verwendete Zubehörmaterialien. Es garantiert, dass zertifizierte Produkte schadstoffgeprüft und umweltfreundlich sind.
        Die Kriterien basieren auf wissenschaftlichen Erkenntnissen und umfassen strenge Grenzwerte für Schadstoffe wie Pestizide, Schwermetalle und Formaldehyd.
    ''')

    st.markdown('''
        Alle Bestandteile eines Produkts – vom Garn bis zum Knopf – werden geprüft. Das Label bietet Verbrauchern Sicherheit und Transparenz,
        da es gesundheitliche Unbedenklichkeit bestätigt. Die jährliche Aktualisierung der Kriterien stellt sicher,
        dass die Standards stets den neuesten gesetzlichen Vorgaben und wissenschaftlichen Erkenntnissen entsprechen.
    ''')

# Tab 2
with tab2:
    # Spalten aufmachen
    col1, col2, col3 = st.columns(3)

    # Bild einfügen
    col2.image('images/certificates/ohris.png')

    # Text einfügen
    st.markdown('''
        Mit der Anwendung des **OHRIS-Systems (Occupational Health and Risk Management System)** stellen wir sicher, dass Arbeits- und Gesundheitsschutz
        in unserem Unternehmen höchste Priorität genießen. OHRIS unterstützt uns dabei, systematisch Risiken zu identifizieren, zu bewerten
        und durch gezielte Maßnahmen zu minimieren. Dieses maßgeschneiderte Managementsystem fördert die Sicherheit unserer Mitarbeiter
        und gewährleistet, dass wir alle relevanten rechtlichen Vorgaben einhalten.
    ''')

    st.markdown('''
        Als Unternehmen, das OHRIS umsetzt, beweisen wir unser Engagement für ein sicheres Arbeitsumfeld und stärken zugleich unser Risiko- und Gesundheitsmanagement,
        um kontinuierlich eine hohe Arbeitsqualität zu gewährleisten.
    ''')

# Tab 3
with tab3:
    # Spalten aufmachen
    col1, col2, col3 = st.columns(3)

    # Bild einfügen
    col2.image('images/certificates/iso_9001.webp')

    # Text einfügen
    st.markdown('''
        Mit der **ISO 9001-Zertifizierung** gewährleisten wir höchste Qualität in all unseren Produkten und Dienstleistungen.
        Diese international anerkannte Norm für Qualitätsmanagementsysteme hilft uns, kontinuierlich unsere Prozesse zu verbessern
        und die Zufriedenheit unserer Kunden zu steigern. Durch die systematische Analyse und Optimierung unserer Arbeitsabläufe gewährleisten´
        wir eine gleichbleibend hohe Qualität und erfüllen die Erwartungen unserer Kunden.
    ''')

    st.markdown('''
        Die Zertifizierung zeigt unser Engagement für exzellenten Service, effiziente Arbeitsmethoden und eine starke Kundenorientierung.
        Als ISO 9001-zertifiziertes Unternehmen belegen wir, dass wir zuverlässig und effizient arbeiten und uns kontinuierlich verbessern.
    ''')

# Tab 4
with tab4:
    # Spalten aufmachen
    col1, col2, col3 = st.columns(3)

    # Bild einfügen
    col2.image('images/certificates/iso_14001.png')

    # Text einfügen
    st.markdown('''
        Als **ISO 14001-zertifiziertes** Unternehmen verpflichten wir uns zu einem verantwortungsbewussten Umgang mit natürlichen Ressourcen
        und zur Minimierung unserer Umweltbelastungen. Diese international anerkannte Norm für Umweltmanagementsysteme unterstützt uns dabei,
        unsere Umweltleistung kontinuierlich zu verbessern und alle relevanten Umweltvorschriften einzuhalten. Wir identifizieren
        und bewerten systematisch unsere Umweltaspekte und setzen effektive Maßnahmen zur Reduktion von Emissionen und Abfällen um.
    ''')

    st.markdown('''
        Die ISO 14001-Zertifizierung unterstreicht unser Engagement für den Umweltschutz und zeigt, dass wir als Unternehmen sowohl ressourcenschonend
        als auch nachhaltig wirtschaften.
    ''')

# Tab 5
with tab5:
    # Spalten aufmachen
    col1, col2, col3 = st.columns(3)

    # Bild einfügen
    col2.image('images/certificates/iso_45001.webp')

    # Text einfügen
    st.markdown('''
        Mit der **ISO 45001-Zertifizierung** demonstrieren wir unser Engagement für die Gesundheit und Sicherheit unserer Mitarbeiter.
        Diese international anerkannte Norm für Arbeitsgesundheit und -sicherheit hilft uns, potenzielle Gefährdungen zu erkennen und systematisch zu beseitigen.
        Durch die Implementierung effektiver Schutzmaßnahmen und kontinuierliche Verbesserung der Arbeitsbedingungen reduzieren wir das Risiko von Arbeitsunfällen
        und Gesundheitsproblemen.
    ''')

    st.markdown('''
        Als ISO 45001-zertifiziertes Unternehmen schaffen wir ein sicheres Arbeitsumfeld, das die Sicherheit unserer Mitarbeiter gewährleistet
        und gleichzeitig unser Engagement für verantwortungsvolle Arbeitspraktiken unterstreicht.
    ''')

# Tab 6
with tab6:
    # Spalten aufmachen
    col1, col2, col3 = st.columns(3)

    # Bild einfügen
    col2.image('images/certificates/iso_50001.jpg')

    # Text einfügen
    st.markdown('''
        Mit der Zertifizierung nach **ISO 50001** setzen wir als Unternehmen auf ein effektives Energiemanagement,
        um unseren Energieverbrauch nachhaltig zu optimieren und Kosten zu senken.
        Diese international anerkannte Norm hilft uns, Energieeffizienzmaßnahmen systematisch umzusetzen und unsere Umweltauswirkungen zu minimieren.
        Durch kontinuierliche Verbesserung und regelmäßige Überprüfung unserer Prozesse identifizieren wir Energiesparpotenziale und steigern unsere Wettbewerbsfähigkeit.
    ''')

    st.markdown('''
        Die ISO 50001-Zertifizierung unterstreicht unser Engagement für eine nachhaltige Energienutzung und bekräftigt unsere Verantwortung gegenüber Umwelt und Gesellschaft.
        Als zertifiziertes Unternehmen zeigen wir unseren Kunden, Partnern und Mitarbeitern, dass wir zukunftsorientiert und ressourcenschonend wirtschaften.
    ''')