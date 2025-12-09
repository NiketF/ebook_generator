import streamlit as st
import google.generativeai as genai
from datetime import datetime
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="HR E-Book Generator",
    page_icon="📘",
    layout="wide"
)

# --- AUTHENTICATION LOGIC (Cloud Compatible) ---
# This looks for the key in Streamlit's secure storage
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except (FileNotFoundError, KeyError):
    # Fallback for local testing if secrets.toml isn't set up
    # But for cloud deployment, the try block above is what matters
    st.error("⚠️ Security Alert: API Key not found. Please set GEMINI_API_KEY in Streamlit Secrets.")
    st.stop()

# --- CUSTOM CSS FOR APP UI ---
st.markdown("""
<style>
    .reportview-container { background: #f5f5f5; }
    .main-header { font-family: 'Helvetica Neue', sans-serif; color: #2c3e50; font-weight: 700; }
    .stButton>button { background-color: #2c3e50; color: white; border-radius: 5px; height: 3em; width: 100%; font-weight: bold; }
    .stButton>button:hover { background-color: #34495e; border: 1px solid white; }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=50)
    st.title("Settings")
    st.markdown("**System Status:** ✅ API Connected")
    st.markdown("---")
    st.markdown("**Output Format:**\n- HTML 5\n- Publication Ready\n- Mobile Responsive")

# --- PROMPT GENERATION LOGIC ---
def build_prompt(community):
    return f"""
    You are an Expert Industry Analyst and Career Strategist with an IQ of 220. 
    Your task is to write a comprehensive, publication-ready E-Book for a Human Resources (HR) department targeting the specific community: '{community}'.

    **OBJECTIVE:**
    Generate a 10-15 page equivalent professional guide. The tone must be authoritative, motivational, and strictly industry-focused.
    
    **CONSTRAINTS:**
    1. NO storytelling, NO metaphors, NO fictional scenarios.
    2. NO conversational filler.
    3. Output MUST be valid, standalone HTML5 code with embedded CSS.
    4. CSS: Serif fonts for body, distinct headers, good line-height.
    
    **REQUIRED E-BOOK STRUCTURE:**
    1. PREFACE, 2. TABLE OF CONTENTS, 3. INTRODUCTION, 4. INDUSTRY EVALUATION,
    5. ROLES, 6. SKILLS, 7. 10-YEAR GROWTH OUTLOOK, 8. HOW TO PREPARE,
    9. INTERPERSONAL SKILLS, 10. ROADMAP, 11. EXAMPLE PROJECTS,
    12. CERTIFICATIONS, 13. COMPANY EXAMPLES, 14. SALARY, 15. CONCLUSION, 16. APPENDIX.

    **HTML STYLING REQUIREMENTS:**
    - Use <h2>, <h3> for sections.
    - Use <ul> and <li> for lists.
    - Do NOT include markdown blocks (```html). Just return the raw HTML code.
    """

# --- MAIN APP LOGIC ---
st.markdown("<h1 class='main-header'>📘 Professional HR E-Book Generator</h1>", unsafe_allow_html=True)
st.markdown("Generate comprehensive, industry-standard guides for any professional community.")

col1, col2 = st.columns([2, 1])

with col1:
    target_community = st.text_input("Target Community / Job Role", placeholder="e.g., Data Scientists, Nursing Staff")

with col2:
    st.write("") # Spacer
    st.write("") # Spacer
    generate_btn = st.button("Generate E-Book")

# --- GENERATION PROCESS ---
if generate_btn:
    if not target_community:
        st.warning("Please specify a target community.")
    else:
        try:
            # 1. Configure Gemini
            genai.configure(api_key=GEMINI_API_KEY)
            
            # Using 1.5-flash as 2.5 is not yet standard/stable for API
            model = genai.GenerativeModel('gemini-1.5-flash') 

            # 2. UI Feedback
            status_text = st.empty()
            progress_bar = st.progress(0)
            
            status_text.markdown("### 🧠 Analyzing Industry Trends...")
            progress_bar.progress(20)

            # 3. Call API
            prompt = build_prompt(target_community)
            status_text.markdown(f"### ✍️ Drafting content for '{target_community}'... (This may take a moment)")
            progress_bar.progress(50)
            
            response = model.generate_content(prompt)
            
            # 4. Process Response
            ebook_content = response.text
            ebook_content = ebook_content.replace("```html", "").replace("```", "")
            
            progress_bar.progress(100)
            status_text.success("E-Book Generated Successfully!")

            # 5. Display & Download
            st.divider()
            
            st.download_button(
                label="📥 Download E-Book as HTML",
                data=ebook_content,
                file_name=f"{target_community.replace(' ', '_')}_Career_Guide.html",
                mime="text/html"
            )

            with st.expander("📖 Preview E-Book Content", expanded=True):
                st.components.v1.html(ebook_content, height=800, scrolling=True)

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey; font-size: 12px;'>"
    f"Generated by Gemini AI • {datetime.now().year} • HR Professional Suite"
    "</div>", 
    unsafe_allow_html=True
)