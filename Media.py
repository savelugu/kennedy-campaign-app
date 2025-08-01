import streamlit as st
from gtts import gTTS
import tempfile


def speak(text):
    tts = gTTS(text)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        st.audio(fp.name, format="audio/mp3")
def app():
    st.title("📸 Media Gallery")
    
    # Optional search/filter bar
    search_query = st.text_input("Search media by title or keyword:")
    
    media_items = [
        {"type": "video", "url": "https://www.youtube.com/watch?v=mXLJu9RSCbI", "title": "Speech at Event"},
        {"type": "video", "url": "https://www.youtube.com/watch?v=DparTMrcyp8", "title": "Kennedy Debate"},
        {"type": "video", "url": "https://www.youtube.com/watch?v=fyHS8b2W5VU", "title": "Community Visit"},
        {"type": "video", "url": "https://youtu.be/N9BblpfgZbY", "title": "NPP Flag"},
        {"type": "video", "url": "https://youtu.be/zB8VDZ7oTUU", "title": "Campaign Song"},
        {"type": "audio", "url": "./audio/kennedy_bio_ha.mp3", "title": "Interview Clip"},
    ]

    if search_query:
        media_items = [m for m in media_items if search_query.lower() in m["title"].lower()]

    cols = st.columns(2)
    for idx, media in enumerate(media_items):
        with cols[idx % 2]:
            st.markdown(f"**{media['title']}**")
            if media["type"] == "video":
                st.video(media["url"])
            elif media["type"] == "image":
                st.image(media["url"], use_container_width=True)
            elif media["type"] == "audio":
                st.audio(media["url"], format="audio/mpeg")  
                
                
    audio_clips = [
    {"title": "Campaign Theme", "path": "audio/kese.mp3"},
    {"title": "Interview Clip", "path": "audio/kennedy_bio_ha.mp3"}
    ]

    st.title("🎤 Kennedy Agyapong Endorsements")

    endorsements = [
                "Kennedy Agyapong is a visionary leader with a proven track record.",
                "He has donated over 600 vehicles to support NPP campaigns.",
                "Building a $6 million cardio and dialysis center at 37 Military Hospital.",
                "Kennedy stands for honesty, patriotism, and development."
            ]

    for i, msg in enumerate(endorsements):
                with st.container():
                    st.markdown(f"**📣 Endorsement {i + 1}:** {msg}")
                    if st.button(f"🔊 Play Voice {i + 1}", key=f"btn{i}"):
                        speak(msg)

        

 

if __name__ == "__main__":
    app()
