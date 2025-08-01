import streamlit as st
from streamlit_option_menu import option_menu
import os
import base64
import streamlit.components.v1 as components
import requests
from datetime import datetime
import Biography, Vision, Achievements, Media, Join_Us, Contact



# NPP Hero layout with gradient and glowing text/button
st.markdown("""
    <div style='
        text-align: center;
        padding: 60px 20px;
        background: linear-gradient(135deg, #002395, #d71a28);
        border-radius: 15px;
        box-shadow: 0 0 25px rgba(0,0,0,0.3);
        color: white;
        margin-bottom: 40px;
    '>
        <h1 style='font-size: 3em; margin-bottom: 10px; text-shadow: 1px 1px 4px #000;'>Welcome to the Campaign Hub</h1>
        <p style='font-size: 1.5em; margin-bottom: 30px; text-shadow: 1px 1px 3px #000;'>The People’s Voice. The People’s Choice</p>
        <img src='https://i.postimg.cc/qqCjkCVW/Kennedy-Ohene-Agyapong.webp' width='140' style='border-radius: 10px; border: 2px solid white; box-shadow: 0 0 10px rgba(255,255,255,0.6);'/>
        <br><br>
        <a href='#' style='
            background-color: white;
            color: #002395;
            padding: 12px 25px;
            font-size: 16px;
            text-decoration: none;
            border-radius: 8px;
            font-weight: bold;
            box-shadow: 0 0 10px rgba(255,255,255,0.6);
            transition: background-color 0.3s, color 0.3s;
        ' onmouseover="this.style.backgroundColor='#d71a28'; this.style.color='white'" onmouseout="this.style.backgroundColor='white'; this.style.color='#002395'">
            🚀 Explore Constituencies
        </a>
    </div>
""", unsafe_allow_html=True)

# Sidebar Banner Image
# Campaign banner HTML
image_url = "https://i.postimg.cc/qqCjkCVW/Kennedy-Ohene-Agyapong.webp"

banner_html = f"""
<div class="banner-container">
  <div class="banner">
    <div class="wave"></div>
    <div class="logo-circle"></div>
    <div class="banner-text">🇬🇭 Kennedy Ohene Agyapong For 2028</div>
  </div>
</div>

<style>
  .banner-container {{
    display: flex;
    align-items: center;
    justify-content: center;
    height: 280px;  /* Reduced from 320px */
    padding: 0 5px;
    margin-top: -20px;  /* Move banner up */
  }}

  .banner {{
    position: relative;
    width: 100%;
    max-width: 320px;
    height: 200px;
    border-radius: 20px;
    overflow: hidden;
    border: 3px solid white;
    background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
    box-shadow: 0 0 25px rgba(215, 26, 40, 0.7);
    text-align: center;
    color: white;
  }}

  .wave {{
    position: absolute;
    width: 300%;
    height: 100%;
    background: linear-gradient(90deg, #e30613, #ffffff, #002868, #e30613);
    animation: waveAnim 6s ease-in-out infinite;
    opacity: 0.2;
  }}

  @keyframes waveAnim {{
    0% {{ transform: translateX(0); }}
    100% {{ transform: translateX(-33.33%); }}
  }}

  .logo-circle {{
    position: absolute;
    top: 35%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 100px;
    height: 100px;
    background: url('{image_url}') no-repeat center center;
    background-size: cover;
    border-radius: 50%;
    border: 4px solid white;
    box-shadow: 0 0 15px rgba(255,255,255,0.7);
  }}

  .banner-text {{
    position: absolute;
    bottom: 15px;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    padding: 0 10px;
    text-shadow: 1px 1px 2px #000000aa;
  }}
</style>
"""


# Render in the sidebar
with st.sidebar:
    components.html(banner_html, height=320)

with st.sidebar:
    # Custom styled title
    st.markdown("""
        <div style="
            background: linear-gradient(135deg, #002395 0%, #d71a28 100%);
            color: white;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
            box-shadow: 0 0 15px rgba(215, 26, 40, 0.7);
            font-size: 20px;
            margin-bottom: 10px;
        ">
            🇬🇭 Kennedy Menu
        </div>
    """, unsafe_allow_html=True)


with st.sidebar:
    app = option_menu(
            menu_title="",
            options=[
                "Biography", "Vision", "Achievements","Media", "Join Us", "Contact"
            ],
            icons=[
                "building", "columns-gap", "graph-up-arrow",
                "droplet-half", "bar-chart-steps", "people-fill"
            ],
            menu_icon="list",
            default_index=0,
            styles={
                "container": {
                    "padding": "5px",
                    "background-color": "#111111",
                    "border-radius": "10px",
                },
                "icon": {
                    "color": "#2b00ffff",
                    "font-size": "22px",
                    "animation": "glow 2s ease-in-out infinite alternate"
                },
                "nav-link": {
                    "color": "#ffffffff",
                    "font-size": "18px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "#ff0000",
                    "transition": "0.3s"
                },
                "nav-link-selected": {
                    "background-color": "#200f8e",
                    "color": "#ffffff",
                    "font-weight": "bold",
                    "box-shadow": "0 0 10px #15ffff",
                    "border-radius": "8px",
                }
            }
        )

    # Google Analytics (optional)
    st.markdown(
        f"""
        <!-- Global site tag (gtag.js) - Google Analytics -->
        <script async src="https://www.googletagmanager.com/gtag/js?id={os.getenv('analytics_tag')}"></script>
        <script>
            window.dataLayer = window.dataLayer || [];
            function gtag(){{ dataLayer.push(arguments); }}
            gtag('js', new Date());
            gtag('config', '{os.getenv('analytics_tag')}');
        </script>
        """, unsafe_allow_html=True
    )

    # Debug print
    print(os.getenv('analytics_tag'))

# Navigation controller
if app == "Biography":
    Biography.app()
elif app == "Vision":
    Vision.app()
elif app == "Achievements":
    Achievements.app()
elif app == "Media":
    Media.app()
elif app == "Join Us":
    Join_Us.app()
elif app == "Contact":
    Contact.app()
    
    
    # Footer Quote
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown(
        """
        <style>
        .footer-quote {
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            padding: 15px 25px;
            border-radius: 12px;
            background: linear-gradient(90deg, #e30613, #ffffff, #002868);
            color: black;
            box-shadow: 0 0 15px rgba(0,0,0,0.4);
            margin-top: 25px;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from {
                box-shadow: 0 0 10px #e30613, 0 0 20px #ffffff, 0 0 30px #002868;
            }
            to {
                box-shadow: 0 0 20px #ffffff, 0 0 30px #e30613, 0 0 40px #002868;
            }
        }
        </style>

        <div class="footer-quote">
            🧭 <span style="font-style: italic;">"Leadership with Action, Not Words."</span> 🚀
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<h5 style='text-align: center; color: #15FFFF'>Created with ❤️ by Shaz Data Consult</h5>", unsafe_allow_html=True)


