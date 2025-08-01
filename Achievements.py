import streamlit as st
from streamlit_carousel import carousel
from PIL import Image


def app():
    st.set_page_config(page_title="Kennedy Agyapong – Achievements", layout="wide")

    # Banner Image
    st.title("🏆 Achievements of Kennedy Ohene Agyapong")
    st.image("assets/kennedy_banner.jpg", use_container_width=True)

    # Carousel Items
    items = [
        {
            "title": "🚗 Grassroots Empowerment",
            "img": "./Images/hand.jpg",
            "text": "Donated over 600 pickup vehicles and motorbikes to support NPP campaigns and local party organizers across all 16 regions of Ghana."
        },
        {
            "title": "🏥 Healthcare Infrastructure",
            "img": "./Images/hand.jpg",
            "text": "Financed a $6 million cardio and dialysis center at 37 Military Hospital to provide affordable, life-saving treatments to Ghanaians."
        },
        {
            "title": "🎓 Youth & Education Support",
            "img": "./Images/hand.jpg",
            "text": "Sponsored tuition and full educational costs for hundreds of underprivileged students including international talent like Abraham Atta."
        },
        {
            "title": "🏭 Economic Development",
            "img": "./Images/hand.jpg",
            "text": "Built Africa’s largest cold store facility and established a starch processing factory, creating jobs and boosting local agriculture."
        },
        {
            "title": "💰 Party Loyalty & Funding",
            "img": "./Images/hand.jpg",
            "text": "Funded the New Patriotic Party (NPP) since 1992, covering logistics and settling multimillion-dollar campaign loans."
        },
        {
            "title": "🦠 Disaster Relief & Social Support",
            "img": "./Images/hand.jpg",
            "text": "Donated PPEs, beds, and hospital equipment during COVID-19, and funded the evacuation of stranded Ghanaians in Lebanon."
        },
        {
            "title": "🎖️ Military & National Service",
            "img": "./Images/hand.jpg",
            "text": "Provided fish ponds and financed specialist medical training for Ghana Armed Forces personnel to enhance national defense capacity."
        },
        {
            "title": "📣 Grassroots Mobilization",
            "img": "./Images/hand.jpg",
            "text": "Passionately defended grassroots voices, ensuring political decisions represent the will of ordinary Ghanaians."
        },
        {
            "title": "🏗️ Infrastructure Advocacy",
            "img": "./Images/hand.jpg",
            "text": "Led infrastructural development in Assin Central, building schools, roads, clinics, and water systems for underserved communities."
        }
    ]

    # Show Carousel
    carousel(items)

if __name__ == "__main__":
    app()