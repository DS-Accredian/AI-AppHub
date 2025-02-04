import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI-Powered Tools Hub", page_icon="🎯", layout="wide")

# Custom Styling
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #2E3B55;
            text-align: center;
        }
        .subtitle {
            font-size: 24px;
            font-weight: bold;
            color: #4A6FA5;
        }
        .app-card {
            background-color: #F4F6F8;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            margin-bottom: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<p class='title'>🚀 AI-Powered Productivity Hub</p>", unsafe_allow_html=True)

st.write("### Access all your AI-powered applications in one place")

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
            <a href='{app_link}' target='_blank'><button style='background-color:#4A6FA5;color:white;padding:10px 20px;border:none;border-radius:5px;'>Launch App 🚀</button></a>
        </div>
        """, unsafe_allow_html=True)
