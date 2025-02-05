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
            padding: 20px;
            justify-content: center;
        }
        .app-card {
            background-color: #F9F9FB;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 6px 15px rgba(0,0,0,0.1);
            text-align: center;
            transition: transform 0.3s ease-in-out;
        }
        .app-card:hover {
            transform: translateY(-5px);
        }
        .app-icon {
            width: 60px;
            height: 60px;
            margin-bottom: 10px;
        }
        button {
            background-color: #4A6FA5;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        button:hover {
            background-color: #3A5C82;
        }
        a {
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown("<p class='title'>🚀 AI-Powered Productivity Hub</p>", unsafe_allow_html=True)
st.markdown("<p class='description'>Access all your AI-powered applications in one place</p>", unsafe_allow_html=True)

# App Links with Icons
apps = [
    ("📚 AI Curriculum Designer", "https://curriculumgenerator-nwbzsv8s3cpmbydkwkmroy.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/1828/1828765.png"),
    ("📝 AI Article & Blog Creator", "https://articlegenerator-3c3a9npfiswj5gv9ecxrnj.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3135/3135715.png"),
    ("🎥 Quiz Generator from Class Recordings", "https://video-lecture-quiz-automation-wudeyepvkcdzb2m6fv6c48.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3050/3050356.png"),
    ("📖 AI Brochure Chatbot", "https://brochurechatbot-ytwvbk5ayodlbugzva4npo.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/619/619153.png"),
    ("📊 AI Case Study Generator", "https://casestudygenerator-uphjrcnc9x2ydywtgcspgx.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3502/3502743.png"),
    ("📑 AI PowerPoint Generator", "https://ai-ppt-generator-c7zscfcczqcpybexdror68.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/3159/3159310.png"),
    ("🎨 AI Slide Creator", "https://app-slide-creator-2ttekw79kny684bx27auph.streamlit.app/", "https://cdn-icons-png.flaticon.com/512/2702/2702133.png")
]

# Display apps in a grid layout
st.markdown("<div class='grid-container'>", unsafe_allow_html=True)
for app_name, app_link, app_icon in apps:
    st.markdown(f"""
        <div class='app-card'>
            <img src='{app_icon}' class='app-icon' />
            <p><strong>{app_name}</strong></p>
            <a href='{app_link}' target='_blank'>
                <button>Launch App 🚀</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
