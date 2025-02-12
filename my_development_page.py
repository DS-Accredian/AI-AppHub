import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI Tools Hub", page_icon="🚀", layout="wide")

# Header
st.markdown('<div align="center" class="header"><h1>🚀EduAgentX </h1></div>', unsafe_allow_html=True)

# Display a message indicating the app is in development
st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <h2>🚧 This App is Still in Development 🚧</h2>
        <p>We're working hard to bring you the best experience. Stay tuned for updates!</p>
    </div>
""", unsafe_allow_html=True)

# Display icons to indicate development status
st.markdown("""
    <div style="display: flex; justify-content: center; gap: 20px; margin-top: 30px;">
        <span style="font-size: 50px;">🔧</span>
        <span style="font-size: 50px;">🚀</span>
        <span style="font-size: 50px;">🛠️</span>
    </div>
""", unsafe_allow_html=True)
