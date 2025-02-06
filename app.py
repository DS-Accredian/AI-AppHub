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
        padding: 2rem;
        border-radius: 0.75rem;
        border: 1px solid #e5e7eb;
        text-align: center;
        transition: all 0.3s;
        margin-bottom: 1rem;
        height: 280px;  /* Fixed height */
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
    }
    
    .tool-card:hover {
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transform: translateY(-2px);
    }
    
    .tool-icon {
        font-size: 3rem;
        margin-bottom: 1.5rem;
        height: 60px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .tool-content {
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        width: 100%;
    }
    
    .tool-name {
        font-size: 1.25rem;
        font-weight: 500;
        color: #111827;
        margin-bottom: 0.75rem;
        line-height: 1.4;
    }
    
    .tool-description {
        font-size: 0.875rem;
        color: #6b7280;
        margin-bottom: 1.5rem;
        line-height: 1.5;
        flex-grow: 1;
    }
    
    .learn-more {
        color: #4285f4;
        font-size: 0.875rem;
        font-weight: 500;
        text-decoration: none;
        padding-top: 1rem;
        display: inline-block;
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
        "url": "https://curriculumgenerator-nwbzsv8s3cpmbydkwkmroy.streamlit.app/",
        "description": "Create comprehensive curriculum plans with AI assistance",
        "category": "Education"
    },
    {
        "name": "AI Article & Blog Creator",
        "icon": "📝",
        "url": "https://articlegenerator-3c3a9npfiswj5gv9ecxrnj.streamlit.app/",
        "description": "Generate engaging articles and blog posts with AI",
        "category": "Content"
    },
    {
        "name": "Quiz Generator",
        "icon": "🎥",
        "url": "https://video-lecture-quiz-automation-wudeyepvkcdzb2m6fv6c48.streamlit.app/",
        "description": "Create quizzes from video lecture recordings automatically",
        "category": "Education"
    },
    {
        "name": "AI Brochure Chatbot",
        "icon": "📖",
        "url": "https://brochurechatbot-ytwvbk5ayodlbugzva4npo.streamlit.app/",
        "description": "Interactive chatbot to chat with brochure contents",
        "category": "Marketing"
    },
    {
        "name": "AI Case Study Generator",
        "icon": "📊",
        "url": "https://casestudygenerator-uphjrcnc9x2ydywtgcspgx.streamlit.app/",
        "description": "Generate detailed case studies with AI analysis",
        "category": "Business"
    },
    {
        "name": "AI PowerPoint Generator",
        "icon": "📑",
        "url": "https://ai-ppt-generator-c7zscfcczqcpybexdror68.streamlit.app/",
        "description": "Create professional presentations automatically",
        "category": "Productivity"
    },
    {
        "name": "AI Slide Creator",
        "icon": "🎨",
        "url": "https://app-slide-creator-2ttekw79kny684bx27auph.streamlit.app/",
        "description": "Design beautiful presentation slides with AI",
        "category": "Design"
    }
]

# Header
st.markdown('<div class="header"><h1>🚀 AI Tools</h1></div>', unsafe_allow_html=True)

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

# Filter tools based on category
filtered_tools = [
    tool for tool in tools
    if selected_category == "All" or tool["category"] == selected_category
]

# Display tools in a grid
cols = st.columns(4)
for i, tool in enumerate(filtered_tools):
    with cols[i % 4]:
        st.markdown(f"""
        <a href="{tool['url']}" target="_blank" style="text-decoration: none;">
            <div class="tool-card">
                <div class="tool-icon">{tool['icon']}</div>
                <div class="tool-content">
                    <div>
                        <div class="tool-name">{tool['name']}</div>
                        <div class="tool-description">{tool['description']}</div>
                    </div>
                    <div class="learn-more">Learn more →</div>
                </div>
            </div>
        </a>
        """, unsafe_allow_html=True)

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
