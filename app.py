import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI-Powered Tools Hub", page_icon="🎯", layout="wide")

# Custom Styling for a Professional Look
st.markdown("""
    <style>
        /* Apply custom font */
        body {
            font-family: 'Arial', sans-serif;
        }
        
        .title {
            font-size: 48px;
            font-weight: 700;
            color: #2E3B55;
            text-align: center;
            margin-top: 40px;
            margin-bottom: 20px;
        }
        
        .subtitle {
            font-size: 22px;
            font-weight: 600;
            color: #4A6FA5;
            text-align: left;
            margin-bottom: 12px;
        }

        .description {
            font-size: 20px;
            font-weight: 400;
            color: #6C7C93;
            text-align: center;
            margin-bottom: 40px;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Card Design */
        .app-card {
            background-color: #FFFFFF;
            padding: 20px;
            border-radius: 15px;  /* Softer, more professional corners */
            box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.1);  /* Subtle shadow */
            margin-bottom: 25px;
            text-align: left;
            max-width: 320px;
            margin-left: auto;
            margin-right: auto;
            transition: all 0.3s ease;  /* Smooth transition for hover effect */
        }

        .app-card:hover {
            transform: translateY(-5px);  /* Hover effect */
            box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.15);  /* Enhance shadow on hover */
        }

        button {
            background-color: #4A6FA5;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            cursor: pointer;
            transition: background-color 0.3s ease, transform 0.3s ease;
            text-align: center;
        }

        button:hover {
            background-color: #3A5C82;
            transform: scale(1.05);  /* Slight zoom on hover */
        }

        a {
            text-decoration: none;
        }

        /* Responsive design for columns */
        .css-1d391kg {
            gap: 2rem !important;  /* Add more gap between columns for spacing */
        }

        /* Adjust container padding for better layout */
        .css-1cpxqw2 {
            padding: 3rem 1rem 1rem 1rem;
        }

        /* Ensure button text is centered */
        .stButton>button {
            width: 100%;
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
cols = st.columns(2)  # Create two columns
for i, (app_name, app_link) in enumerate(apps):
    with cols[i % 2]:  # Distribute the cards between the two columns
        st.markdown(f"""
        <div class='app-card'>
            <p class='subtitle'>{app_name}</p>
            <a href='{app_link}' target='_blank'>
                <button>Launch App 🚀</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
