import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI-Powered Tools Hub", page_icon="🎯", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
        }
        .title {
            font-size: 65px;
            font-weight: bold;
            color: #2E3B55;
            text-align: center;
            margin-bottom: 20px;
        }
        .description {
            font-size: 20px;
            text-align: center;
            color: #4A4A4A;
            margin-bottom: 40px;
        }
        .app-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            gap: 20px;
        }
        .app-card {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 4px 4px 15px rgba(0,0,0,0.1);
            text-align: center;
            width: 350px;
            transition: transform 0.3s;
        }
        .app-card:hover {
            transform: scale(1.05);
        }
        .subtitle {
            font-size: 22px;
            font-weight: bold;
            color: #2E3B55;
            margin-bottom: 10px;
        }
        .launch-button {
            background-color: #4A6FA5;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            font-size: 16px;
            cursor: pointer;
            transition: background 0.3s;
        }
        .launch-button:hover {
            background-color: #3b5c85;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<p class='title'>🚀 AI-Powered Productivity Hub</p>", unsafe_allow_html=True)
st.markdown("<p class='description'>Access all your AI-powered applications in one place</p>", unsafe_allow_html=True)

# App Links
apps = [
    ("📚 AI Curriculum Designer", "https://curriculumgenerator-nwbzsv8s3cpmbydkwkmroy.streamlit.app/"),
    ("📝 AI Article & Blog Creator", "https://articlegenerator-3c3a9npfiswj5gv9ecxrnj.streamlit.app/"),
    ("🎥 Quiz Generator from Class Recordings", "https://video-lecture-quiz-automation-wudeyepvkcdzb2m6fv6c48.streamlit.app/"),
    ("📖 AI Brochure Chatbot", "https://brochurechatbot-ytwvbk5ayodlbugzva4npo.streamlit.app/"),
    ("📊 AI Case Study Generator", "https://casestudygenerator-uphjrcnc9x2ydywtgcspgx.streamlit.app/"),
    ("📑 AI PowerPoint Generator", "https://ai-ppt-generator-c7zscfcczqcpybexdror68.streamlit.app/"),
    ("🎨 AI Slide Creator", "https://app-slide-creator-2ttekw79kny684bx27auph.streamlit.app/")
]

# Display apps in a grid layout
st.markdown("<div class='app-container'>", unsafe_allow_html=True)
for app_name, app_link in apps:
    st.markdown(f"""
    <div class='app-card'>
        <p class='subtitle'>{app_name}</p>
        <a href='{app_link}' target='_blank'>
            <button class='launch-button'>Launch App 🚀</button>
        </a>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
