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
            font-size: 24px;
            font-weight: 600;
            color: #3A7D9B;
            text-align: left;  /* Left align subtitle */
            margin-bottom: 10px;
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
            padding: 15px 20px;  /* Smaller padding */
            border-radius: 10px;  /* Smaller border-radius */
            box-shadow: 0px 4px 10px rgba(0,0,0,0.1);  /* Reduced box-shadow */
            margin-bottom: 15px;  /* Reduced margin */
            text-align: left;  /* Left align text inside card */
            max-width: 300px;  /* Set a maximum width to make the card smaller */
            margin-left: auto;
            margin-right: auto;
        }
        .app-card:hover {
            transform: translateY(-5px);
        }
        button {
            background-color: #4A6FA5;
            color: white;
            padding: 10px 20px;  /* Smaller padding */
            border: none;
            border-radius: 8px;
            font-size: 14px;  /* Slightly smaller text size */
            cursor: pointer;
            transition: background-color 0.3s ease;
            text-align: center;  /* Center text inside button */
        }
        button:hover {
            background-color: #3A5C82;
        }
        a {
            text-decoration: none; /* Remove underline from links */
        }
        .cols-wrapper {
            display: flex;
            justify-content: space-between;
            gap: 20px;  /* Adjusted gap between columns */
        }
        .col {
            flex: 0 0 48%;  /* Use 48% width for each column */
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

# Display apps in two columns
st.markdown("<div class='cols-wrapper'>", unsafe_allow_html=True)
for i, (app_name, app_link) in enumerate(apps):
    st.markdown(f"""
        <div class='col'>
            <div class='app-card'>
                <p class='subtitle'>{app_name}</p>
                <a href='{app_link}' target='_blank'>
                    <button>Launch App 🚀</button>
                </a>
            </div>
        </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
