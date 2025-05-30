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
     /* Translucent effect for in-development tools */
    .disabled {
    position: relative; /* Ensure positioning for the tooltip */
    opacity: 0.6;
}

/* Grey overlay */
.disabled::after {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(128, 128, 128, 0.5); /* Grey overlay with transparency */
    pointer-events: none; /* Ensures the overlay doesn’t block interactions */
    border-radius: inherit; /* Inherits the border-radius of the card */
}

/* Tooltip styles */
.disabled::before {
    content: "Feature is being Developed"; /* Tooltip text */
    position: absolute;
    top: 50%; /* Center vertically */
    left: 50%; /* Center horizontally */
    transform: translate(-50%, -50%); /* Ensure perfect centering */
    background: black;
    color: white;
    padding: 8px 12px;
    font-size: 14px;
    border-radius: 4px;
    white-space: nowrap;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.3s ease-in-out;
    z-index: 10; /* Ensure tooltip is above overlay */
}

/* Show tooltip on hover */
.disabled:hover::before {
    opacity: 1;
    visibility: visible;
}

</style>
""", unsafe_allow_html=True)

# Tools data
tools = [
    {
        "name": "AI Curriculum Designer",
        "icon": "📚",
        "url": "https://curriculumgenerator-j3frvbcqdljvpm7krbghvk.streamlit.app/",
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
        "url": "https://qovesiulvn32emgr62h5ch.streamlit.app/",
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
        "url": "https://ai-powered-ppt-jgdfqiet6wej7qvlgxvcnf.streamlit.app/",
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
        "name": "Validate Brochure & Website Data",
        "icon": "📑",  # Bookmark tab symbol for data validation
        "url": "#",
        "description": "In Development",
        "category": "In Development",
        "disabled": True
    },
    {
        "name": "Chat with Session Recording",
        "icon": "💬🎥",  # Chat bubble + video camera for session recording
        "url": "#",
        "description": "In Development",
        "category": "In Development",
        "disabled": True
    },
    {
        "name": "Personalized Roadmap Generator",
        "icon": "🗺️",  # Map icon for roadmap generation
        "url": "#",
        "description": "In Development",
        "category": "In Development",
        "disabled": True
    },
    {
        "name": "Personalized TA",
        "icon": "👨‍🏫",  # Teacher/professor icon representing TA
        "url": "#",
        "description": "In Development",
        "category": "In Development",
        "disabled": True
    },
    {
        "name": "Job Scraper",
        "icon": "💼",  # briefcase icon representing job
        "url": "#",
        "description": "In Development",
        "category": "In Development",
        "disabled": True
    },
    {
        "name": "Interview Question Generator",
        "icon": "💼❓",  # Question mark icon for interview questions
        "url": "https://interviewquestionsgenerator-czxktws989ftkc5vejhkhm.streamlit.app/",
        "description": "Generate interview questions based on Topic",
        "category": "Education"    
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
selected_category = st.session_state.get("selected_category", "All")

# Filter tools based on search and category
filtered_tools = [
    tool for tool in tools
    if (search_query.lower() in tool["name"].lower() or 
        search_query.lower() in tool["description"].lower()) and
    (selected_category == "All" or tool["category"] == selected_category)
]

# --- render ONLY the filtered tools -----------------
cols = st.columns(4)
for i, tool in enumerate(filtered_tools):          # <-- change here
    disabled_class = "disabled" if tool.get("disabled") else ""
    with cols[i % 4]:
        st.markdown(f"""
        <a href="{tool['url']}" target="_blank" class="{disabled_class}" style="text-decoration: none;">
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
