import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI Tools Hub", page_icon="🚀", layout="wide")

# Tools data
tools = [
    {"name": "AI Curriculum Designer", "icon": "📚", "url": "https://curriculum-generator-rag-a5u5qr34wnnhu4fq4mm4hj.streamlit.app/", "description": "Create comprehensive curriculum plans with AI assistance", "category": "Education"},
    {"name": "AI Article & Blog Creator", "icon": "📝", "url": "https://articlegenerator-3c3a9npfiswj5gv9ecxrnj.streamlit.app/", "description": "Generate engaging articles & blog posts using AI Agents", "category": "Content"},
    {"name": "Quiz Generator", "icon": "🎥", "url": "https://video-lecture-quiz-automation-uwhmhmrebcfotmnuth6c2j.streamlit.app/", "description": "Create quizzes and notes from video lecture recordings transcripts automatically", "category": "Education"},
    {"name": "AI Brochure Chatbot", "icon": "📚", "url": "https://brochure-n8jkhj2gvjmzvjz8sw2wdb.streamlit.app/", "description": "Interactive chatbot to chat with brochure contents", "category": "Marketing"},
    {"name": "AI Case Study Generator", "icon": "📊", "url": "https://casestudygenerator-uphjrcnc9x2ydywtgcspgx.streamlit.app/", "description": "Generate detailed case studies with Solutions using AI Agents", "category": "Business"},
    {"name": "AI PowerPoint Generator", "icon": "📁", "url": "https://ai-powered-ppt-generator-4rqdhcbd7t97rcg6ypfbpx.streamlit.app/", "description": "Create professional presentations automatically using AI Agents", "category": "Productivity"},
    {"name": "Pre-reads Generator", "icon": "📚", "url": "https://pre-read-generator-9tihairmalelqgt6xzvy4u.streamlit.app/", "description": "Generate pre-read materials efficiently using AI Agents", "category": "Education"},
    {"name": "Post-read Generator", "icon": "📚", "url": "https://post-read-generator-tfifkkxmmmks5y6thvm5ls.streamlit.app/", "description": "Generate post-read materials efficiently using AI Agents", "category": "Education"},
    
    # In Development Tools
    {"name": "AI Video Editor", "icon": "🔒", "url": "#", "description": "In Development", "category": "In Development"},
    {"name": "AI Research Assistant", "icon": "🔒", "url": "#", "description": "In Development", "category": "In Development"},
    {"name": "AI Data Visualizer", "icon": "🔒", "url": "#", "description": "In Development", "category": "In Development"},
    {"name": "AI Chatbot Builder", "icon": "🔒", "url": "#", "description": "In Development", "category": "In Development"},
]

# Header
st.markdown('<h1 align="center">🚀 EduAgentX</h1>', unsafe_allow_html=True)

# Display tools in a grid
cols = st.columns(4)
for i, tool in enumerate(tools):
    with cols[i % 4]:
        st.markdown(f"""
        <div style="background-color: white; padding: 1.5rem; border-radius: 0.75rem; border: 1px solid #e5e7eb; text-align: center; transition: all 0.3s; margin-bottom: 1rem;">
            <div style="font-size: 2.5rem; margin-bottom: 1rem;">{tool['icon']}</div>
            <div style="font-size: 1.125rem; font-weight: 500; color: #111827; margin-bottom: 0.5rem;">{tool['name']}</div>
            <div style="font-size: 0.875rem; color: #6b7280; margin-bottom: 1rem;">{tool['description']}</div>
        </div>
        """, unsafe_allow_html=True)
