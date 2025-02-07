import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="AI Tools Hub", page_icon="🚀", layout="wide")

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
        "description": "Generate engaging articles and blog posts with AI",
        "category": "Content"
    },
    {
        "name": "Quiz Generator",
        "icon": "🎥",
        "url": "https://video-lecture-quiz-automation-uwhmhmrebcfotmnuth6c2j.streamlit.app/",
        "description": "Create quizzes from video lecture recordings automatically",
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
        "description": "Generate detailed case studies with AI analysis",
        "category": "Business"
    },
    {
        "name": "AI PowerPoint Generator",
        "icon": "📑",
        "url": "https://ai-powered-ppt-generator-hljimuo9pwpp6sucjekbds.streamlit.app/",
        "description": "Create professional presentations automatically",
        "category": "Productivity"
    },
    {
        "name": "AI Slide Creator",
        "icon": "🎨",
        "url": "https://app-slide-creator-2ttekw79kny684bx27auph.streamlit.app/",
        "description": "Design beautiful presentation slides with AI",
        "category": "Design"
    },
    {
        "name": "Pre-reads Generator",
        "icon": "📖",
        "url": "https://pre-read-generator-9tihairmalelqgt6xzvy4u.streamlit.app/",
        "description": "Generate pre-reading materials efficiently",
        "category": "Education"
    },
    {
        "name": "Post-read Generator",
        "icon": "📘",
        "url": "https://post-read-generator-tfifkkxmmmks5y6thvm5ls.streamlit.app/",
        "description": "Create post-reading summaries and insights",
        "category": "Education"
    }
]

# Header
st.markdown('<h1>🚀 AI Tools</h1>', unsafe_allow_html=True)

# Search bar
search_query = st.text_input("", placeholder="Search AI tools", key="search")

# Categories
categories = ["All"] + list(set(tool["category"] for tool in tools))
cols = st.columns(len(categories))
selected_category = st.session_state.get("selected_category", "All")

for i, category in enumerate(categories):
    if cols[i].button(category, key=category):
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
            <div style="
                background-color: white; padding: 20px; border-radius: 10px;
                border: 1px solid #e5e7eb; text-align: center;
                transition: all 0.3s; margin-bottom: 10px;
                height: 280px; display: flex; flex-direction: column;
                justify-content: space-between; align-items: center;">
                <div style="font-size: 3rem; margin-bottom: 15px;">{tool['icon']}</div>
                <div style="flex-grow: 1; width: 100%; text-align: center;">
                    <div style="font-size: 1.25rem; font-weight: 500; color: #111827;">
                        {tool['name']}
                    </div>
                    <div style="font-size: 0.875rem; color: #6b7280; margin-bottom: 10px;">
                        {tool['description']}
                    </div>
                </div>
                <div style="color: #4285f4; font-size: 0.875rem; font-weight: 500;">
                    Learn more →
                </div>
            </div>
        </a>
        """, unsafe_allow_html=True)

# Add some spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)
