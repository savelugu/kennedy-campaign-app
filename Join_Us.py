import streamlit as st
import pandas as pd
import os
from datetime import date

def app():

    st.set_page_config(page_title="NPP – Polling Station Executive Form", layout="centered")
    # NPP gradient and glow style
    npp_card_style = """
        background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(215, 26, 40, 0.7);
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        margin-top: 30px;
    """

    st.markdown(f"""
        <div style="{npp_card_style}">
            🗳️ Polling Station Executive Registration
        </div>
    """, unsafe_allow_html=True)
    st.markdown("Fill out the form below to register polling station executives for Kennedy Agyapong.")

    # --- Region-Constituency Mapping (Full List) ---
    region_constituency_map = {
        "Ahafo": ["Asunafo North", "Asunafo South", "Asutifi North", "Asutifi South", "Tano North", "Tano South"],
        "Ashanti": ["Adansi‑Asokwa", "Fomena", "New Edubease", "Afigya Kwabre North", "Afigya‑Kwabre South",
                    "Ahafo Ano North", "Ahafo Ano South East", "Ahafo Ano South West", "Akrofuom", "Amansie Central",
                    "Amansie West", "Asante‑Akim Central", "Asante‑Akim North", "Asante‑Akim South", "Asokwa", "Asawase",
                    "Atwima‑Kwanwoma", "Atwima‑Mponua", "Atwima‑Nwabiagya North", "Atwima‑Nwabiagya South", "Bantama",
                    "Bekwai", "Bosome‑Freho", "Bosomtwe", "Ejisu", "Ejura‑Sekyedumase", "Juaben", "Kumawu", "Kwabre East",
                    "Kwadaso", "Mampong", "Manhyia North", "Manhyia South", "Nhyiaeso", "Obuasi East", "Obuasi West",
                    "Offinso North", "Offinso South", "Oforikrom", "Old Tafo", "Sekyere Afram Plains", "Sekyere Central",
                    "Sekyere East", "Sekyere Kumawu", "Sekyere South", "Suame", "Subin"],
        "Bono": ["Berekum East", "Berekum West", "Dormaa Central", "Dormaa East", "Dormaa West", "Jaman North",
                "Jaman South", "Sunyani East", "Sunyani West", "Tain", "Wenchi"],
        "Bono East": ["Atebubu‑Amantin", "Kintampo North", "Kintampo South", "Nkoranza North", "Nkoranza South",
                    "Pru East", "Pru West", "Sene East", "Sene West", "Techiman North", "Techiman South"],
        "Central": ["Abura‑Asebu‑Kwamankese", "Agona East", "Agona West", "Ajumako‑Enyan‑Essiam",
                    "Asikuma‑Odoben‑Brakwa", "Assin Central", "Assin North", "Assin South", "Awutu Senya East",
                    "Awutu Senya West", "Cape Coast North", "Cape Coast South", "Effutu", "Ekumfi", "Gomoa Central",
                    "Gomoa East", "Gomoa West", "Komenda‑Edina‑Eguafo‑Abirem", "Mfantsiman", "Twifo‑Atti‑Morkwa",
                    "Hemang Lower Denkyira", "Upper Denkyira East", "Upper Denkyira West"],
        "Eastern": ["Abuakwa South", "Abuakwa North", "Afram Plains North", "Afram Plains South", "Akropong", "Akwatia",
                    "Akyemansa", "Asene‑Manso‑Akroso", "Asuogyaman", "Atiwa East", "Atiwa West", "Ayensuano",
                    "Birim Central", "Birim North", "Birim South", "Denkyembour", "Fanteakwa North", "Fanteakwa South",
                    "Kwaebibirem", "Kwahu Afram Plains North", "Kwahu Afram Plains South", "Kwahu East", "Kwahu South",
                    "Kwahu West", "Lower Manya Krobo", "New Juaben North", "New Juaben South", "Nsawam Adoagyiri",
                    "Okere", "Suhum", "Upper Manya Krobo", "Upper West Akim", "West Akim", "Yilo Krobo"],
        "Greater Accra": ["Ablekuma Central", "Ablekuma North", "Ablekuma South", "Ablekuma West", "Adenta", "Amasaman",
                        "Anyaa‑Sowutuom", "Ayawaso Central", "Ayawaso East", "Ayawaso North", "Ayawaso West Wuogon",
                        "Dome‑Kwabenya", "Domeabra‑Obom", "Madina", "Korle Klottey", "Odododiodioo",
                        "OkaiKwei Central", "OkaiKwei North", "Tema East", "Tema West", "Krowor", "Ledzokuku",
                        "Dade Kotopon", "Abokobi‑Madina", "Ningo‑Prampram", "Shai Osudoku", "Trobu", "Ga East",
                        "Ga Central", "Ga North", "Ga South", "Ga West"],
        "North East": ["Bunkpurugu", "Chereponi", "Nalerigu", "Walewale", "Yagaba‑Kubori", "Yunyoo"],
        "Northern": ["Bimbilla", "Garu", "Gushegu", "Karaga", "Klocalu-Kpandai", "Mion", "Nanton", "Nanumba North",
                    "Nanumba South", "Saboba", "Sagnarigu", "Savelugu", "Tamale North", "Tamale Central", "Tamale South",
                    "Tolon", "Yendi", "Zabzugu"],
        "Oti": ["Biakoye", "Buem", "Akan (Jasikan)", "Krachi East", "Krachi West", "Krachi Nchumuru", "Nkwanta North",
                "Nkwanta South"],
        "Savannah": ["Bole Bamboi", "Yapei‑Kusawgu", "Salaga South", "Salaga North", "Daboya‑Mankarigu",
                    "Sawla‑Tuna‑Kalba", "Damongo"],
        "Upper East": ["Bawku Central", "Bawku West", "Zebilla", "Binduri", "Bolgatanga East", "Bolgatanga Central",
                    "Bongo", "Pusiga", "Garu", "Nabdam", "Navrongo Central", "Chiana‑Paga", "Talensi", "Tempane"],
        "Upper West": ["Wa Central", "Wa East", "Wa West", "Sissala East", "Sissala West", "Nadowli Kaleo", "Jirapa",
                    "Lambussie", "Lawra", "Nandom", "Daffiama‑Bussie‑Issa"],
        "Volta": ["Ho Central", "Ho West", "Hohoe", "Anlo (Keta)", "Akatsi Central", "Akatsi North", "Akatsi South",
                "Ketu North", "Ketu South", "Kpando", "North Tongu", "South Tongu", "North Dayi", "South Dayi",
                "Adaklu", "Agotime‑Ziope", "Afadzato South", "Central Tongu"],
        "Western": ["Jomoro", "Ellembelle", "Mpohor", "Ahanta West", "Effia", "Kwesimintsim", "Tarkwa‑Nsuaem",
                    "Prestea‑Huni Valley", "Wassa East", "Amenfi East", "Amenfi Central", "Amenfi West",
                    "Evalue‑Gwira", "Essikado‑Ketan", "Sekondi", "Takoradi", "Mpohor District"],
        "Western North": ["Aowin", "Bia East", "Bia West", "Bibiani‑Anhwiaso‑Bekwai", "Bodi", "Juabeso",
                        "Sefwi‑Akontombra", "Sefwi‑Wiawso", "Suaman"]
    }

    # --- Step 1: Region & Constituency Selection ---
    selected_region = st.selectbox("Select your Region", list(region_constituency_map.keys()))
    selected_constituency = st.selectbox("Select your Constituency", region_constituency_map[selected_region])

    # --- Form ---
    with st.form("polling_exec_form"):
        # NPP gradient and glow style
        npp_card_style = """
            background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(215, 26, 40, 0.7);
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-top: 30px;
        """

        st.markdown(f"""
            <div style="{npp_card_style}">
                🗳️ Personal Information
            </div>
        """, unsafe_allow_html=True)
        name = st.text_input("Full Name")
        polling_station = st.text_input("Polling Station Name")
        contact = st.text_input("Phone / WhatsApp Number")
        voter_id = st.text_input("Voter ID Number")
        location = st.text_input("Town/City")
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        dob = st.date_input("Date of Birth")
        age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
        st.info(f"🎂 You are {age} years old.")
        if age < 18:
            st.warning("⚠️ Must be 18+ to register.")

        # NPP gradient and glow style
        npp_card_style = """
            background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(215, 26, 40, 0.7);
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-top: 30px;
        """

        st.markdown(f"""
            <div style="{npp_card_style}">
                🗳️ Upload Photo
            </div>
        """, unsafe_allow_html=True)
        photo = st.file_uploader("Upload your photo (JPG/PNG)", type=["jpg", "jpeg", "png"])
        if photo:
            st.image(photo, width=150)

        # NPP gradient and glow style
        npp_card_style = """
            background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(215, 26, 40, 0.7);
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            margin-top: 30px;
        """

        st.markdown(f"""
            <div style="{npp_card_style}">
                🗳️ Identity Verification
            </div>
        """, unsafe_allow_html=True)
        id_type = st.selectbox("ID Type", ["National ID", "Driver's License", "Passport"])
        id_number = st.text_input("ID Number")
        id_upload = st.file_uploader("Upload scanned ID (optional)", type=["jpg", "jpeg", "png", "pdf"])

        wants_to_volunteer = st.checkbox("I want to volunteer for the campaign")
        volunteer_role = ""
        if wants_to_volunteer:
            volunteer_role = st.selectbox("Select Volunteer Role", ["Coordinator", "Polling Agent", "Logistics", "Media", "Security", "Other"])

        agree = st.checkbox("I support Kennedy Agyapong and want to be part of the movement.")

        submit = st.form_submit_button("📋 Submit")

        if submit:
            if not all([name, polling_station, contact, voter_id, location, id_number, agree]):
                st.error("🚫 Please fill out all required fields and agree to the statement.")
            elif age < 18:
                st.error("🚫 You must be at least 18 years old to register.")
            else:
                st.success(f"✅ Thank you, {name}! Your registration has been recorded.")
                st.balloons()

                # Display summary
                st.markdown("### Submission Summary")
                st.write({
                    "Name": name,
                    "Polling Station": polling_station,
                    "Phone": contact,
                    "Voter ID": voter_id,
                    "Region": selected_region,
                    "Constituency": selected_constituency,
                    "Location": location,
                    "Gender": gender,
                    "DOB": str(dob),
                    "Age": age,
                    "Volunteer": wants_to_volunteer,
                    "Volunteer Role": volunteer_role,
                    "ID Type": id_type,
                    "ID Number": id_number
                })

                # Save to CSV
                data = {
                    "Name": name,
                    "Polling Station": polling_station,
                    "Phone": contact,
                    "Voter ID": voter_id,
                    "Region": selected_region,
                    "Constituency": selected_constituency,
                    "Town/City": location,
                    "Gender": gender,
                    "Date of Birth": dob,
                    "Age": age,
                    "Volunteer": wants_to_volunteer,
                    "Volunteer Role": volunteer_role,
                    "ID Type": id_type,
                    "ID Number": id_number
                }

                df = pd.DataFrame([data])
                os.makedirs("data", exist_ok=True)
                file_path = "data/signups.csv"
                if os.path.exists(file_path):
                    df.to_csv(file_path, mode="a", header=False, index=False)
                else:
                    df.to_csv(file_path, index=False)
if __name__ == "__main__":
    app()