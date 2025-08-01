import streamlit as st
from PIL import Image

def app():
    # You can continue with the rest of your Streamlit app here
    # NPP gradient and glow style
    npp_card_style = """
        background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(215, 26, 40, 0.7);
        text-align: center;
        font-size: 30px;
        font-weight: bold;
        margin-top: 30px;
    """

    st.markdown(f"""
        <div style="{npp_card_style}">
            Welcome to Kennedy Agyapong's Flagbearer Campaign App
        </div>
    """, unsafe_allow_html=True)
    st.markdown("✨ Explore the vision, policies, and progress.")


    # Page Configuration
    st.set_page_config(page_title="Kennedy Agyapong – Portfolio", layout="wide")

    # Custom CSS Styling
    st.markdown("""
        <style>
        body {
            background-color: #eef2f7;
        }
        .card {
            background-color: white;
            border-radius: 16px;
            padding: 25px;
            margin: 15px 0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1), 0 0 12px rgba(0,0,255,0.15);
            border-left: 6px solid #002366;
            transition: all 0.3s ease-in-out;
        }
        .card:hover {
            transform: scale(1.01);
            box-shadow: 0 0 25px rgba(255,0,0,0.3), 0 0 15px rgba(0,0,255,0.3);
        }
        .header {
            font-size: 36px;
            font-weight: 700;
            color: #002366;
            margin-bottom: 10px;
        }
        .subheader {
            font-size: 24px;
            font-weight: 600;
            color: #cc0000;
            margin-bottom: 10px;
        }
        .footer-quote {
            font-size: 22px;
            font-weight: 600;
            text-align: center;
            color: #000;
            font-style: italic;
        }
        .profile-pic {
            border-radius: 16px;
            box-shadow: 0 0 12px rgba(0, 0, 0, 0.25);
            width: 100%;
            max-width: 250px;
        }
        </style>
    """, unsafe_allow_html=True)

    # Layout with image and intro
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("assets/kennedy.jpg", caption="Kennedy Agyapong", use_container_width=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        # NPP gradient and glow style
        npp_card_style = """
            background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
            color: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 0 15px rgba(215, 26, 40, 0.7);
            text-align: center;
            font-size: 30px;
            font-weight: bold;
            margin-top: 30px;
        """

        st.markdown(f"""
            <div style="{npp_card_style}">
                🇬🇭 Kennedy Ohene Agyapong
            </div>
        """, unsafe_allow_html=True)
        st.markdown("""
        - **Date of Birth:** June 16, 1960  
        - **Political Party:** New Patriotic Party (NPP)  
        - **Constituency:** Assin Central  
        - **Education:**  
            - Adisadel College, Cape Coast  
            - Fordham University, New York  
        """)
        
    # Justified text with some styling
    st.markdown("""
    <div style='text-align: justify; font-size: 16px; line-height: 1.6;'>
    Kennedy Ohene Agyapong is a renowned Ghanaian businessman, philanthropist, and political figure known for his bold leadership and outspoken commitment to truth and national development. Although no longer serving as the Member of Parliament for Assin Central—a position he held with distinction for over two decades—his legacy in Ghanaian politics remains impactful.

    Born in Assin Dompim in the Central Region of Ghana, Kennedy Agyapong rose from humble beginnings to become one of the country’s most influential public figures. As a self-made entrepreneur, he has built a vast business empire spanning media, real estate, agriculture, and import/export. Through his media network, including Net2 TV and Oman FM, he has consistently used his platform to advocate for transparency, good governance, and youth empowerment.

    He is widely respected for his philanthropic work, especially in the areas of education, healthcare, and support for grassroots businesses. Notably, he personally funded the construction of a multi-million dollar cardio and dialysis center at the 37 Military Hospital, and has donated hundreds of vehicles to support community and political activities.

    Kennedy Agyapong’s fearless stance on national issues, combined with his deep patriotism, has earned him admiration across political and social divides. As he now focuses on a presidential bid to lead the New Patriotic Party (NPP) into the future, he continues to champion a Ghana built on discipline, honesty, job creation, and self-reliance.
    </div>
    """, unsafe_allow_html=True)

    # Sections
    def section(title, content):
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown(f'<div class="subheader">{title}</div>', unsafe_allow_html=True)
        st.markdown(content)
        st.markdown('</div>', unsafe_allow_html=True)

    # Section Content
    section("🏛️ Political Experience", """
    - Member of Parliament for **Assin Central** since 2001  
    - Committees: Finance, Communications, Trade & Industry  
    - Known for his **bold, outspoken leadership**
    """)

    section("🏆 Achievements", """
    - Built **100+ classroom blocks** across Ghana  
    - Sponsored **thousands of students** to pursue education  
    - Built ICT & vocational centers  
    - Strong **anti-corruption advocate**  
    - **Job creation** through media and real estate ventures  
    """)

    section("👔 Business Background", """
    - CEO of **Kencity Media Ltd.** (Net 2 TV, Oman FM)  
    - Real estate investor & entrepreneur  
    - Created **thousands of private sector jobs**  
    """)

    section("🗳️ Vision for Ghana", """
    - Promote **Discipline & Transparency** in governance  
    - Empower citizens through **natural resource equity**  
    - Focus on **vocational education & youth employment**  
    - Digitize all government services  
    - Enforce **zero tolerance for corruption**  
    """)

    section("🌐 Social Media", """
    - 📘 [Facebook – @KennedyAgyapongGH](https://facebook.com/KennedyAgyapongGH)  
    - 🐦 [Twitter – @Ken4President](https://twitter.com/Ken4President)  
    - 📸 [Instagram – @KenAgyapong2028](https://instagram.com/KenAgyapong2028)  
    """)


if __name__ == "__main__":
    app()