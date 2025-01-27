import streamlit as st
import folium
import leafmap.foliumap as leafmap
import pandas as pd

# Konfiguration festlegen
st.set_page_config(
    page_title="Umweltauswirkungen",
    page_icon="🌍",
)

# Logo
st.logo('images/logos/Uvex_logo.svg', size='large', icon_image='images/logos/uvex_logo_black.svg')

# Page-Überschrift
st.write("# Umweltauswirkungen 🌍")

# Tabs aufmachen
tab1, tab2 = st.tabs(["Lieferkette", "Umwelt KPI's"])

# Tab 1: Lieferkette
with tab1:
    # Überschrift
    st.write("### Lieferkette")

    # Leafmap-Karte initialisieren
    m = leafmap.Map(center=(42.46222863788524, 59.620992904976305), zoom=2)

    # Lieferkette Vorprodukt 1
    supply_chain1 = [
        {"latitude": 23.00643, "longitude": 72.61509, "name": "Ahmedabad, Indien", "info": "<b>Vikas Cotton Mills</b><br>Baumwoll Produktion"},
        {"latitude": 21.168785189241476, "longitude": 72.83223864673094, "name": "Surat, Indien", "info": "<b>Tapti Textiles Inc.</b><br>Oberstoff 1 Produktion"}
    ]

    # Weitere Lieferanten
    supply_chain2 = [
        {"latitude": 31.498178715202318, "longitude": 120.31263924581572, "name": "Wuxi, China", "info": "<b>Tai-Hu Textiles Ltd.</b><br>Oberstoff 2 Produktion"},
        {"latitude": 22.838693853281605, "longitude": 113.67749121687903, "name": "Dongguan, China", "info": "<b>SBS Zipper</b><br>Reißverschluss Produktion"}
    ]

    # Produktiosnsstandort UVEX
    production_loc = {"latitude": 31.28735, "longitude": 120.94789, "name": "Kunshan, China", "info": "<b>UVEX Safety Equipment Kunshan</b><br>Jacken Produktion"}

    # Weitere Stationen der Lieferkette
    supply_chain3 = [
        {"latitude": 49.32039, "longitude": 11.05019, "name": "Schwabach, Deutschland", "info": "<b>UVEX Safety Logistics</b><br>Lagerung und Versand"},
        {"latitude": 50.87554, "longitude": 11.63310, "name": "Jena, Deutschland", "info": "<b>Böttcher AG</b><br>B2B Großhandel"},
        {"latitude": 47.37463, "longitude": 8.52508, "name": "Zürich, Schweiz", "info": "<b>mr. clean AG</b><br>Gebäudereinigungsdienstleister"}
    ]

    # Marker für Lieferanten und Produktionsstandort hinzufügen
    for sup1 in supply_chain1:
        folium.Marker(
                location=(sup1["latitude"], sup1["longitude"]),
                tooltip=f"{sup1['name']}",
                popup=folium.Popup(sup1["info"], max_width=300),  # Add HTML content
            ).add_to(m)

    for sup2 in supply_chain2:
        folium.Marker(
                location=(sup2["latitude"], sup2["longitude"]),
                tooltip=f"{sup2['name']}",
                popup=folium.Popup(sup2["info"], max_width=300),  # Add HTML content
            ).add_to(m)

    # Marker für Produktionsstandort
    folium.Marker(
                location=(production_loc["latitude"], production_loc["longitude"]),
                tooltip=f"{production_loc['name']}",
                popup=folium.Popup(production_loc["info"], max_width=300),  # Add HTML content
            ).add_to(m)

    # Marker für weitere Stationen der Lieferkette
    for sup3 in supply_chain3:
        folium.Marker(
                location=(sup3["latitude"], sup3["longitude"]),
                tooltip=f"{sup3['name']}",
                popup=folium.Popup(sup3["info"], max_width=300),  # Add HTML content
            ).add_to(m)

    # Linie für Lieferkette 1
    folium.PolyLine(locations=[(supply_chain1[0]["latitude"], supply_chain1[0]["longitude"]), (supply_chain1[1]["latitude"], supply_chain1[1]["longitude"])], color='blue', weight=4, opacity=1).add_to(m)

    # Linie von L1 zur Produktion
    folium.PolyLine(locations=[(supply_chain1[1]["latitude"], supply_chain1[1]["longitude"]), (production_loc["latitude"], production_loc["longitude"])], color='blue', weight=4, opacity=1).add_to(m)

    # Linien für Lieferkette 2 zur Produktion
    for sup2 in supply_chain2:
        folium.PolyLine(locations=[(sup2["latitude"], sup2["longitude"]), (production_loc["latitude"], production_loc["longitude"])], color='blue', weight=4, opacity=1).add_to(m)

    # Linien für Lieferkette 3
    folium.PolyLine(locations=[(production_loc["latitude"], production_loc["longitude"]), (supply_chain3[0]["latitude"], supply_chain3[0]["longitude"])], color='blue', weight=4, opacity=1).add_to(m)
    folium.PolyLine(locations=[(supply_chain3[0]["latitude"], supply_chain3[0]["longitude"]), (supply_chain3[1]["latitude"], supply_chain3[1]["longitude"])], color='blue', weight=4, opacity=1).add_to(m)
    folium.PolyLine(locations=[(supply_chain3[1]["latitude"], supply_chain3[1]["longitude"]), (supply_chain3[2]["latitude"], supply_chain3[2]["longitude"])], color='blue', weight=4, opacity=1).add_to(m)

    # Karte in Streamlit anzeigen
    m.to_streamlit(height=600)

    # Transportwege und Co2-Emissionen
    st.write("### Transportwege und CO2-Emissionen")

    # Transportweg Dataframe
    df_transportation = pd.DataFrame(
        {
            "Transportstrecke": [
                "Ahmedabad - Surat",
                "Surat - Kunshan",
                "Dongguan - Kunshan",
                "Wuxi - Kunshan",
                "Kunshan - Schwabach",
                "Schwabach - Jena",
                "Jena - Zürich"
            ],
            "Transportmittel": [
                '🚂 Güterzug',
                '🚢 Containerschiff',
                '🚂 Güterzug',
                '🚛 LKW',
                '✈️ Frachtflugzeug',
                '🚛 LKW',
                '🚂 Güterzug'
            ],
            "Distanz [km]": [
                203.10,
                4891.54,
                1172.54,
                84.81,
                8691.71,
                182.24,
                453.25
            ],
            "CO2-Ausstoß [kg]": [
                0.01,
                0.05,
                0.02,
                0.01,
                4.02,
                0.01,
                0.01
            ]
        }
    )

    # Dataframe ausgeben lassen
    st.dataframe(df_transportation, hide_index=True, use_container_width=True)

# Tab 2: Umwelt KPI's
with tab2:
    # Überschrift
    st.write("### Umwelt KPI's")

    # Spalten definieren
    a, b, c = st.columns(3)
    d, e, f = st.columns(3)

    # KPI's ausgeben lassen
    a.metric(label="Wasserverbrauch 💦", value="15,00 l", border=True)
    b.metric(label="Chemikalienverbrauch 💀", value="5,00 kg", border=True)
    c.metric(label="Energieverbrauch ⚡", value="2,30 kWh", border=True)
    d.metric(label="CO2-Emissionen ☁️", value="4,13 kg", border=True)
    e.metric(label="Rezyklatgehalt ♻️", value="80 %", border=True)
    f.metric(label="Nachhaltige Materialien 🍃", value="60 %", border=True)