import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI-Powered Tools Hub", page_icon="🎯", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        body {
            font-family: 'Google Sans', sans-serif;
            background-color: #ffffff;
            margin: 0;
            padding: 0;
        }
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #1D3A5F;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 10px;
        }
        .description {
            font-size: 20px;
            font-weight: 400;
            color: #6C7C93;
            text-align: center;
            margin-bottom: 40px;
        }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 40px;
            justify-content: center;
        }
        .app-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 16px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }
        .app-card:hover {
            transform: translateY(-5px);
            box-shadow: 0px 8px 20px rgba(0,0,0,0.15);
        }
        .app-icon {
            width: 100px;
            height: 100px;
            margin-bottom: 10px;
        }
        .app-name {
            font-size: 18px;
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
        }
        .launch-button {
            background-color: #1A73E8;
            color: white;
            padding: 10px 18px;
            border: none;
            border-radius: 8px;
            font-size: 14px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            text-decoration: none;
            display: inline-block;
        }
        .launch-button:hover {
            background-color: #1558C6;
        }
        a {
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<p class='title'>AI-Powered Productivity Hub</p>", unsafe_allow_html=True)
st.markdown("<p class='description'>Discover and access AI tools seamlessly</p>", unsafe_allow_html=True)

# App Links with Icons
apps = [
    ("AI Curriculum Designer", "https://curriculumgenerator-nwbzsv8s3cpmbydkwkmroy.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/1828/1828765.png"),
    ("AI Article & Blog Creator", "https://articlegenerator-3c3a9npfiswj5gv9ecxrnj.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"),
    ("Quiz Generator from Class Recordings", "https://video-lecture-quiz-automation-wudeyepvkcdzb2m6fv6c48.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3050/3050356.png"),
    ("AI Brochure Chatbot", "https://brochurechatbot-ytwvbk5ayodlbugzva4npo.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/619/619153.png"),
    ("AI Case Study Generator", "https://casestudygenerator-uphjrcnc9x2ydywtgcspgx.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3502/3502743.png"),
    ("AI PowerPoint Generator", "https://ai-ppt-generator-c7zscfcczqcpybexdror68.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3159/3159310.png"),
    ("AI Slide Creator", "https://app-slide-creator-2ttekw79kny684bx27auph.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/2702/2702133.png")
]

# Display apps in a structured grid layout
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
for app_name, app_link, app_icon in apps:
    st.markdown(f"""
        <div class='app-card'>
            <img src='{app_icon}' class='app-icon' />
            <p class='app-name'>{app_name}</p>
            <a href='{app_link}' target='_blank' class='launch-button'>Launch 🚀</a>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
