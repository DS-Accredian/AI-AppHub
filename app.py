import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI-Powered Tools Hub", page_icon="🎯", layout="wide")

# Custom Styling for a More Professional Look
st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
        }

        .title {
            font-size: 48px;
            font-weight: 600;
            color: #2E3B55;
            text-align: center;
            margin-top: 40px;
            margin-bottom: 10px;
        }

        .description {
            font-size: 20px;
            color: #6C7C93;
            text-align: center;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
            margin-bottom: 40px;
        }

        /* Card Styling */
        .app-card {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
            text-align: left;
            transition: transform 0.3s ease-in-out;
            max-width: 320px;  /* Fixed width for consistency */
            margin-left: auto;
            margin-right: auto;
        }

        .app-card:hover {
            transform: translateY(-5px);  /* Card lift effect on hover */
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);  /* Enhanced shadow */
        }

        .subtitle {
            font-size: 18px;
            font-weight: 600;
            color: #4A6FA5;
            text-align: center;  /* Centered the subtitle */
            margin-bottom: 15px;
        }

        button {
            background-color: #4A6FA5;
            color: white;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s, transform 0.2s ease-in-out;
            width: 100%;
            margin-top: 10px;
        }

        button:hover {
            background-color: #3A5C82;
            transform: scale(1.05);  /* Slight zoom effect */
        }

        a {
            text-decoration: none;
        }

        /* Adjust spacing between columns */
        .css-1d391kg {
            gap: 30px !important;
        }

        /* Adjust button width and responsiveness */
        .stButton>button {
            width: 100%;
        }

        /* Adjust the two-column layout */
        .stGrid {
            display: flex;
            justify-content: space-evenly;
            flex-wrap: wrap;
        }

        .stGrid > div {
            flex: 1 1 45%;  /* This ensures equal width for both columns */
            max-width: 500px;
            margin-bottom: 30px;  /* Added space between cards */
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

# Display apps in two columns with better alignment
cols = st.columns(2)  # Create two columns with balanced spacing
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
