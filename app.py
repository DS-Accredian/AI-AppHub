import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI Tools Hub", page_icon="🚀", layout="wide")

# Custom CSS to match Google's style
st.markdown("""
<style>
    /* Google-style fonts and colors */
    @import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&display=swap');
    
    /* Main container */
    .main {
        font-family: 'Google Sans', sans-serif;
    }
    
    /* Header */
    .header {
        padding: 1.5rem 0;
        border-bottom: 1px solid #e5e7eb;
        display: flex;
        align-items: center;
    }
    
    /* Search bar */
    .stTextInput > div > div > input {
        padding: 1rem 1rem 1rem 3rem !important;
        border-radius: 9999px !important;
        border: 1px solid #e5e7eb !important;
        font-size: 1.125rem !important;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.05) !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #4285f4 !important;
        box-shadow: 0 0 0 2px rgba(66, 133, 244, 0.2) !important;
    }
    
    /* Category buttons */
    .stButton > button {
        background-color: transparent !important;
        color: #6b7280 !important;
        border: none !important;
        border-bottom: 2px solid transparent !important;
        border-radius: 0 !important;
        padding: 1rem 0.5rem !important;
        margin: 0 1rem !important;
        font-weight: 500 !important;
        transition: all 0.2s !important;
    }
    
    .stButton > button:hover {
        color: #374151 !important;
        border-bottom: 2px solid #e5e7eb !important;
    }
    
    .stButton > button.selected {
        color: #4285f4 !important;
        border-bottom: 2px solid #4285f4 !important;
    }
    
    /* Tool cards */
    .tool-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        text-align: center;
        transition: all 0.3s;
        margin-bottom: 1rem;
    }
    
    .tool-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transform: translateY(-2px);
    }
    
    .tool-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .tool-name {
        font-size: 1.125rem;
        font-weight: 500;
        color: #111827;
        margin-bottom: 0.5rem;
    }
    
    .tool-description {
        font-size: 0.875rem;
        color: #6b7280;
        margin-bottom: 1rem;
    }
    
    .learn-more {
        color: #4285f4;
        font-size: 0.875rem;
        font-weight: 500;
        text-decoration: none;
    }
    
    .learn-more:hover {
        color: #1a73e8;
    }
</style>
""", unsafe_allow_html=True)

# Tools data
tools = [
    {
        "name": "AI Curriculum Designer",
        "icon": "📚",
        "url": "https://curriculum-generator-rag-a5u5qr34wnnhu4fq4mm4hj.streamlit.app/",
        "description": "Create comprehensive curriculum plans with AI assistance",
        "category": "Education"
    },
    {
        "name": "AI Article & Blog Creator",
        "icon": "📝",
        "url": "https://articlegenerator-3c3a9npfiswj5gv9ecxrnj.streamlit.app/",
        "description": "Generate engaging articles & blog posts using AI Agents",
        "category": "Content"
    },
    {
        "name": "Quiz Generator",
        "icon": "🎥",
        "url": "https://video-lecture-quiz-automation-uwhmhmrebcfotmnuth6c2j.streamlit.app/",
        "description": "Create quizzes and notes from video lecture recordings transcripts automatically",
        "category": "Education"
    },
    {
        "name": "AI Brochure Chatbot",
        "icon": "📖",
        "url": "https://brochure-n8jkhj2gvjmzvjz8sw2wdb.streamlit.app/",
        "description": "Interactive chatbot to chat with brochure contents",
        "category": "Marketing"
    },
    {
        "name": "AI Case Study Generator",
        "icon": "📊",
        "url": "https://casestudygenerator-uphjrcnc9x2ydywtgcspgx.streamlit.app/",
        "description": "Generate detailed case studies with Solutions using AI Agents",
        "category": "Business"
    },
    {
        "name": "AI PowerPoint Generator",
        "icon": "📑",
        "url": "https://ai-powered-ppt-generator-4rqdhcbd7t97rcg6ypfbpx.streamlit.app/",
        "description": "Create professional presentations automatically using AI Agents",
        "category": "Productivity"
    },
    {
        "name": "Pre-reads Generator",
        "icon": "📖",
        "url": "https://pre-read-generator-9tihairmalelqgt6xzvy4u.streamlit.app/",
        "description": "Generate pre-read materials efficiently using AI Agents",
        "category": "Education"
    },
    {
        "name": "Post-read Generator",
        "icon": "📘",
        "url": "https://post-read-generator-tfifkkxmmmks5y6thvm5ls.streamlit.app/",
        "description": "Generate post-read materials efficiently using AI Agents",
        "category": "Education"
    },
    {
        "name": "Brochure and Website Data Validator",
        "icon": "🔒",
        "url": "https://post-read-generator-tfifkkxmmmks5y6thvm5ls.streamlit.app/",
        "description": "In Development",
        "category": "In Development"
    },
    {
        "name": "Chat with Session Recording",
        "icon": "🔒",
        "url": "https://post-read-generator-tfifkkxmmmks5y6thvm5ls.streamlit.app/",
        "description": "In Development",
        "category": "In Development"
    },
    {
        "name": "Personalized Road-map Generator",
        "icon": "🔒",
        "url": "https://post-read-generator-tfifkkxmmmks5y6thvm5ls.streamlit.app/",
        "description": "In Development",
        "category": "In Development"
    },
    {
        "name": "Personalized TA",
        "icon": "🔒",
        "url": "https://post-read-generator-tfifkkxmmmks5y6thvm5ls.streamlit.app/",
        "description": "In Development",
        "category": "In Development"
    }
]

# Header
st.markdown('<div align="center" class="header"><h1>🚀EduAgentX </h1></div>', unsafe_allow_html=True)

# Search bar
search_query = st.text_input("", placeholder="Search AI tools", key="search")

# Categories
categories = ["All"] + list(set(tool["category"] for tool in tools))
cols = st.columns(len(categories))
selected_category = st.session_state.get("selected_category", "All")

for i, category in enumerate(categories):
    if cols[i].button(
        category,
        key=category,
        help=f"Show {category.lower()} tools",
        type="secondary",
        use_container_width=True,
    ):
        st.session_state.selected_category = category

# Filter tools based on search and category
filtered_tools = [
    tool for tool in tools
    if (search_query.lower() in tool["name"].lower() or 
        search_query.lower() in tool["description"].lower()) and
    (selected_category == "All" or tool["category"] == selected_category)
]

# Display tools in a grid
cols = st.columns(4)
for i, tool in enumerate(filtered_tools):
    with cols[i % 4]:
        st.markdown(f"""
        <a href="{tool['url']}" target="_blank" style="text-decoration: none;">
            <div class="tool-card">
                <div class="tool-icon">{tool['icon']}</div>
                <div class="tool-name">{tool['name']}</div>
                <div class="tool-description">{tool['description']}</div>
                <div class="learn-more">Learn more →</div>
            </div>
        </a>
        """, unsafe_allow_html=True)

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
