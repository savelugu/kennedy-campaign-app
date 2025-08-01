import streamlit as st

def app():

    st.set_page_config(page_title="Contact Kennedy Agyapong", layout="wide")
    st.markdown("<style>body {background-color: #ffffff;}</style>", unsafe_allow_html=True)

    st.title("📞 Contact the Campaign")

    # NPP color gradient and glowing card style
    card_style = """
        background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 0 15px rgba(215, 26, 40, 0.6);
        margin-bottom: 20px;
    """

    link_style = "color: #ffffff; text-decoration: underline;"

    # Two main layout columns
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("./assets/kennedy.jpg", caption="Kennedy Agyapong", use_container_width=True)

    with col2:
        st.subheader("Get in Touch")

        card1, card2 = st.columns(2)
        with card1:
            st.markdown(f"""
            <div style="{card_style}">
                📧 <b>Email</b><br>
                <span>teamkennedy2024@npp.org</span>
            </div>
            """, unsafe_allow_html=True)

        with card2:
            st.markdown(f"""
            <div style="{card_style}">
                📱 <b>Phone</b><br>
                <span>+233 20 123 4567</span>
            </div>
            """, unsafe_allow_html=True)

        card3, card4 = st.columns(2)
        with card3:
            st.markdown(f"""
            <div style="{card_style}">
                🌐 <b>Facebook</b><br>
                <a href="https://facebook.com/kennedyagyapong" target="_blank" style="{link_style}">
                    facebook.com/kennedyagyapong
                </a>
            </div>
            """, unsafe_allow_html=True)

        with card4:
            st.markdown(f"""
            <div style="{card_style}">
                📍 <b>Campaign HQ</b><br>
                <span>Accra, Ghana</span>
            </div>
            """, unsafe_allow_html=True)
if __name__ == "__main__":
    app()