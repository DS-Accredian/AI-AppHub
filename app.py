import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI-Powered Tools Hub", page_icon="🎯", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #1D3A5F;
            text-align: center;
            margin-top: 20px;
            margin-bottom: 20px;
        }
        .subtitle {
            font-size: 28px;
            font-weight: 600;
            color: #3A7D9B;
            text-align: center;
            margin-bottom: 15px;
        }
        .description {
            font-size: 20px;
            font-weight: 400;
            color: #6C7C93;
            text-align: center;
            margin-bottom: 40px;
        }
        .app-card {
            background-color: #F9F9FB;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
            margin-bottom: 20px;
            transition: transform 0.3s ease;
        }
        .app-card:hover {
            transform: translateY(-5px);
        }
        button {
            background-color: #4A6FA5;
            color: white;
            padding: 12px 25px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #3A5C82;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<p class='title'>🚀 AI-Powered Productivity Hub</p>", unsafe_allow_html=True)
st.markdown("<p class='description'>Access all your AI-powered applications in one place</p>", unsafe_allow_html=True)

# App Links
apps = [
    ("📚 AI Curriculum Designer:", "https://curriculumgenerator-nwbzsv8s3cpmbydkwkmroy.streamlit.app/"),
    ("📝 AI Article & Blog Creator:", "https://articlegenerator-3c3a9npfiswj5gv9ecxrnj.streamlit.app/"),
    ("🎥 Quiz Generator from Class Recordings:", "https://video-lecture-quiz-automation-wudeyepvkcdzb2m6fv6c48.streamlit.app/"),
    ("📖 AI Brochure Chatbot:", "https://brochurechatbot-ytwvbk5ayodlbugzva4npo.streamlit.app/"),
    ("📊 AI Case Study Generator:", "https://casestudygenerator-uphjrcnc9x2ydywtgcspgx.streamlit.app/"),
    ("📑 AI PowerPoint Generator:", "https://ai-ppt-generator-c7zscfcczqcpybexdror68.streamlit.app/"),
    ("🎨 AI Slide Creator:", "https://app-slide-creator-2ttekw79kny684bx27auph.streamlit.app/")
]

# Display apps in a grid layout
cols = st.columns(2)
for i, (app_name, app_link) in enumerate(apps):
    with cols[i % 2]:
        st.markdown(f"""
        <div class='app-card'>
            <p class='subtitle'>{app_name}</p>
            <a href='{app_link}' target='_blank'><button>Launch App 🚀</button></a>
        </div>
        """, unsafe_allow_html=True)
