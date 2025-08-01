import streamlit as st
import os
from PIL import Image
from streamlit.components.v1 import html


def show_endorsement_slider():
    st.subheader("🌟 Key Endorsements")

    st.markdown("""
    <style>
    .slider-wrapper {
      overflow: hidden;
      width: 100%;
      padding: 20px;
      border-radius: 12px;
    }

    .slider {
      display: flex;
      animation: scroll 25s linear infinite;
      gap: 30px;
    }

    .endorsement-card {
    flex: none;
    background: #0033cc;  /* NPP Blue */
    color: #ffffff;       /* White text */
    border-radius: 12px;
    padding: 20px;
    width: 300px;
    text-align: center;
    box-shadow: 0 0 20px rgba(255, 0, 0, 0.3);  /* Red glow */
    border: 2px solid #ff0000;
    font-weight: 600;
    }


    .endorsement-card:hover {
      transform: scale(1.05);
      box-shadow: 0 0 25px #0033cc, 0 0 25px #ff0000;
    }

    .endorsement-card img {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      object-fit: cover;
      margin-bottom: 10px;
      border: 3px solid #ff0000;
    }

    .endorsement-card h4 {
      margin: 10px 0 5px;
      color: #0033cc;
    }

    .endorsement-card p {
      font-size: 14px;
      color: #ffffff;
    }

    @keyframes scroll {
      0% { transform: translateX(0); }
      100% { transform: translateX(-150%); }
    }

    .slider-wrapper:hover .slider {
      animation-play-state: paused;
    }
    </style>

    <div class="slider-wrapper">
      <div class="slider">
        <div class="endorsement-card">
          <img src="https://i.imgur.com/VzF9S7M.png" alt="Dr. Kwame Mensah"/>
          <h4>Dr. Kwame Mensah</h4>
          <p>"Kennedy has transformed communities and is a man of action."</p>
        </div>
        <div class="endorsement-card">
          <img src="https://i.imgur.com/Z3ppZbs.png" alt="Hon. Sarah Adjei"/>
          <h4>Hon. Sarah Adjei</h4>
          <p>"His leadership and vision are unmatched in our party."</p>
        </div>
        <div class="endorsement-card">
          <img src="https://i.imgur.com/XN8qvb3.png" alt="Rev. Kofi Anane"/>
          <h4>Rev. Kofi Anane</h4>
          <p>"He puts people first — a servant-leader in every sense."</p>
        </div>
        <div class="endorsement-card">
          <img src="https://i.imgur.com/VzF9S7M.png" alt="Dr. Kwame Mensah"/>
          <h4>Dr. Kwame Mensah</h4>
          <p>"Kennedy has transformed communities and is a man of action."</p>
        </div>
        <div class="endorsement-card">
          <img src="https://i.imgur.com/Z3ppZbs.png" alt="Hon. Sarah Adjei"/>
          <h4>Hon. Sarah Adjei</h4>
          <p>"His leadership and vision are unmatched in our party."</p>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)



def show_timeline():
    st.subheader("📅 Milestones of Hon. Kennedy Agyapong")
    timeline_data = [
        {"year": "2000", "event": "Elected as MP for Assin Central"},
        {"year": "2008", "event": "Established Kencity Media"},
        {"year": "2016", "event": "Donated over 500 vehicles to NPP campaign"},
        {"year": "2020", "event": "Launched grassroots development fund"},
        {"year": "2024", "event": "Flagbearer Aspirant - NPP"},
    ]
    for item in timeline_data:
        st.markdown(f"### {item['year']}")
        st.markdown(f"📌 {item['event']}")
        st.markdown("---")

def app():
    st.set_page_config(page_title="Kennedy Agyapong for NPP 2024", layout="wide")
    st.title("🗳️ Kennedy Agyapong for NPP Flagbearer")
    st.subheader("🇬🇭 Bold Leadership. Proven Results. A New Dawn for Ghana.")
    st.markdown("---")

    # ABOUT
    st.markdown("## 👤 About Kennedy Agyapong")
    qualities = [
        ("🧠", "Visionary leader and seasoned businessman."),
        ("🏗️", "Massive contributor to national development and job creation."),
        ("🚌", "Donated 600+ vehicles for NPP campaigns."),
        ("🏥", "Building a $6M Cardio & Dialysis Centre at the 37 Military Hospital."),
        ("🇬🇭", "Fiercely patriotic and loyal to the New Patriotic Party."),
    ]
    cols = st.columns(3)
    card_style = """
        <div style="
            background-color: #001F5B;
            border-radius: 10px;
            padding: 20px;
            min-height: 200px;
            color: white;
            box-shadow: 0 0 15px #005eff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
        ">
            <div style="font-size: 40px;">{icon}</div>
            <p style="margin-top: 10px; font-size: 16px;">{text}</p>
        </div>
    """
    for i, (icon, text) in enumerate(qualities):
        with cols[i % 3]:
            st.markdown(card_style.format(icon=icon, text=text), unsafe_allow_html=True)

    # CAMPAIGN HIGHLIGHTS
    st.markdown("---")
    st.markdown("### 📸 Highlights from the Campaign Trail")

    image_files = [
        "Images/campaign1.jpg",
        "Images/kennedy.jpg",
        "Images/achievements.jpg"
    ]
    captions = [
        "Donating campaign vehicles",
        "Speaking to the youth",
        "Meeting with NPP executives"
    ]
    IMG_WIDTH, IMG_HEIGHT = 300, 200
    img_cols = st.columns(3)
    for i, col in enumerate(img_cols):
        with col:
            if os.path.exists(image_files[i]):
                img = Image.open(image_files[i])
                img = img.resize((IMG_WIDTH, IMG_HEIGHT))
                st.image(img, caption=captions[i])
            else:
                st.warning(f"Image not found: {image_files[i]}")

    # VIDEO
    st.markdown("---")
    st.markdown("### 🎥 Hear From Kennedy Agyapong Himself")
    st.video("https://youtu.be/WWryRpTDk8I")  # Replace with a real YouTube link

    # TESTIMONIALS


    # Section Divider
    st.markdown("---")
    st.markdown("### 💬 Voices from the Ground – What Delegates Say")

    # Testimonials list
    testimonials = [
        {
            "name": "Alhaji Fuseini – Northern Region Delegate",
            "quote": "Kennedy has always supported the party when others stayed silent. He deserves to lead us."
        },
        {
            "name": "Akosua Mensah – Women’s Organizer, Ashanti Region",
            "quote": "He speaks for the ordinary Ghanaian. I believe in his honesty and strength."
        },
    ]

    # Custom CSS styles for NPP-themed cards
    st.markdown("""
    <style>
    .card {
        background-color:  #002366;
        border-left: 6px solid #ffffff; /* NPP Blue */
        padding: 1rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
    }
    .card h4 {
        margin: 0 0 0.3rem 0;
        color: #cc0000; /* NPP Red */
    }
    .card p {
        margin: 0;
        font-style: italic;
        color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

    # Render each testimonial in a styled card
    for t in testimonials:
        st.markdown(f"""
        <div class="card">
            <h4>{t['name']}</h4>
            <p>"{t['quote']}"</p>
        </div>
        """, unsafe_allow_html=True)


    # PROJECTS / BLOG
    st.markdown("---")
    st.markdown("## 📰 Works of Hon. Kenn")
    posts = [
        {
            "title": "Water Project in Savelugu",
            "category": "Development",
            "description": "The MP launched a water project to serve 5000+ residents.",
            "author": "Hon. KeN",
            "publish_date": "2025-06-20",
            "read_time": "3 min read",
            "background_image": "Images/achievements.jpg",
            "author_image": "Images/kennedy.jpg"
        },
        {
            "title": "Health Center Commissioned",
            "category": "Healthcare",
            "description": "A new health center has been opened to boost healthcare delivery in the area.",
            "author": "Hon. Ken",
            "publish_date": "2025-06-15",
            "read_time": "2 min read",
            "background_image": "Images/achievements.jpg",
            "author_image": "Images/kennedy.jpg"
        },
    ]
    for post in posts:
        with st.container():
            col1, col2 = st.columns([1, 2])
            with col1:
                if os.path.exists(post["background_image"]):
                    st.image(post["background_image"], width=300)
            with col2:
                st.subheader(post["title"])
                st.markdown(f"**Category:** {post['category']}")
                st.markdown(post["description"])
                st.markdown(f"**By {post['author']}** — {post['publish_date']} • {post['read_time']}")
                if os.path.exists(post["author_image"]):
                    st.image(post["author_image"], width=50, caption=post["author"])
        st.markdown("---")

    # ENDORSEMENT SLIDER
    show_endorsement_slider()

    # TIMELINE
    show_timeline()

if __name__ == "__main__":
    app()
