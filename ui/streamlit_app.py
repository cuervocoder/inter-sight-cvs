"""Inter-Sight - Intelligent Talent Matching Platform"""

import streamlit as st
from core.config import settings
from core.llm_provider import get_llm
from processors.cv_parser import parse_cv_streamlit
import json
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Inter-Sight",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .title-gradient {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: bold;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    
    .candidate-card {
        border: 2px solid #667eea;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        background: #f8f9fa;
    }
    
    .match-high { color: #10b981; font-weight: bold; }
    .match-medium { color: #f59e0b; font-weight: bold; }
    .match-low { color: #ef4444; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# Initialize LLM
@st.cache_resource
def get_llm_instance():
    try:
        return get_llm(settings.llm_provider, settings.mistral_api_key)
    except Exception as e:
        st.error(f"Failed to initialize LLM: {e}")
        return None

# Initialize session state
if "company" not in st.session_state:
    st.session_state.company = None
if "cvs" not in st.session_state:
    st.session_state.cvs = []
if "results" not in st.session_state:
    st.session_state.results = None

# Header
st.markdown("<div class='title-gradient'>🎯 Inter-Sight</div>", unsafe_allow_html=True)
st.markdown("**Intelligent Talent Matching with AI-Powered Feedback**")
st.markdown("---")

# Main tabs
tab1, tab2, tab3 = st.tabs(["🏢 Company Setup", "📤 Upload CVs", "🎯 Results"])

# TAB 1: Company Setup
with tab1:
    st.header("Company Profile")
    
    col1, col2 = st.columns(2)
    
    with col1:
        mission = st.text_area(
            "Company Mission",
            value="Democratize AI and talent intelligence",
            height=100,
            help="What is your company's core mission?"
        )
        
        values = st.text_area(
            "Core Values (one per line)",
            value="Innovation\nOwnership\nCollaboration\nExcellence",
            height=120,
            help="List the values that matter most"
        )
    
    with col2:
        focus_skills = st.text_area(
            "Key Skills Needed",
            value="Leadership\nProblem-Solving\nCommunication\nAdaptability",
            height=100,
            help="What soft skills are most important?"
        )
        
        role_description = st.text_area(
            "Role Description",
            value="We're looking for someone who can drive innovation and lead teams",
            height=120,
            help="Describe the ideal candidate"
        )
    
    if st.button("💾 Save Company Profile", use_container_width=True):
        st.session_state.company = {
            "mission": mission,
            "values": [v.strip() for v in values.split("\n") if v.strip()],
            "focus_skills": [s.strip() for s in focus_skills.split("\n") if s.strip()],
            "role_description": role_description,
            "created_at": datetime.now().isoformat()
        }
        st.success("✅ Company profile saved!")
        st.balloons()


# TAB 2: Upload CVs
with tab2:
    st.header("Upload Candidate CVs")
    
    if st.session_state.company is None:
        st.warning("⚠️ Please create a company profile first (Tab 1)")
    else:
        st.success("✅ Company profile loaded")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Upload CV Files")
            st.markdown("**Accepted formats:** PDF, DOCX, TXT, JSON")
            
            uploaded_files = st.file_uploader(
                "Choose CV files",
                type=["pdf", "docx", "doc", "txt", "json"],
                accept_multiple_files=True,
                help="Upload CV files in any format (PDF, Word, TXT, JSON)"
            )
            
            if uploaded_files:
                # Handle both single file and multiple files
                files_list = uploaded_files if isinstance(uploaded_files, list) else [uploaded_files]
                st.write(f"📤 {len(files_list)} file(s) selected")
                
                if st.button("🔄 Load and Process CVs", use_container_width=True):
                    st.session_state.cvs = []
                    progress_bar = st.progress(0)
                    status_text = st.empty()
                    
                    for idx, file in enumerate(files_list):
                        try:
                            status_text.text(f"Processing {file.name}...")
                            cv_data = parse_cv_streamlit(file)
                            
                            if cv_data and "name" in cv_data:
                                st.session_state.cvs.append(cv_data)
                                st.success(f"✅ {file.name} - Extracted: {cv_data.get('name', 'Unknown')}")
                            else:
                                st.warning(f"⚠️ {file.name} - Could not parse")
                        except Exception as e:
                            st.error(f"❌ Error loading {file.name}: {e}")
                        
                        progress_bar.progress((idx + 1) / len(files_list))
                    
                    status_text.empty()
                    progress_bar.empty()
                    
                    if st.session_state.cvs:
                        st.success(f"✅ Successfully loaded {len(st.session_state.cvs)} CVs")
                        st.balloons()
        
        with col2:
            st.subheader("Sample CVs")
            if st.button("📋 Load Sample CVs", use_container_width=True):
                # Load sample data
                sample_cvs = [
                    {
                        "name": "Alice Johnson",
                        "degree": "MS Computer Science",
                        "education": "MIT",
                        "years_experience": 7,
                        "experience": [
                            {"role": "Senior Engineer", "company": "TechCorp", "duration": "2y", "impact": "Led team of 5, improved performance 40%"},
                            {"role": "ML Engineer", "company": "StartupXYZ", "duration": "3y", "impact": "Built ML pipeline, published research"}
                        ],
                        "skills": ["Python", "ML", "Leadership"]
                    },
                    {
                        "name": "Bob Chen",
                        "degree": "BS Computer Science",
                        "education": "Stanford",
                        "years_experience": 5,
                        "experience": [
                            {"role": "Software Engineer", "company": "Google", "duration": "3y", "impact": "Built infrastructure serving 1M+ users"},
                            {"role": "Junior Engineer", "company": "Startup", "duration": "2y", "impact": "MVP development"}
                        ],
                        "skills": ["Python", "Go", "Systems Design"]
                    },
                    {
                        "name": "Carol Rodriguez",
                        "degree": "MBA",
                        "education": "Harvard",
                        "years_experience": 8,
                        "experience": [
                            {"role": "Product Manager", "company": "Meta", "duration": "3y", "impact": "Led $50M product line"},
                            {"role": "Strategy", "company": "Consulting", "duration": "5y", "impact": "Advisory roles"}
                        ],
                        "skills": ["Strategy", "Communication", "Leadership"]
                    }
                ]
                st.session_state.cvs = sample_cvs
                st.success(f"✅ Loaded {len(sample_cvs)} sample CVs")


# TAB 3: Results
with tab3:
    st.header("Results & Intelligent Matching")
    
    if not st.session_state.company:
        st.info("👈 Create company profile first")
    elif not st.session_state.cvs:
        st.info("👈 Upload CVs first")
    else:
        st.success(f"✅ Analyzing {len(st.session_state.cvs)} candidates with AI...")
        
        # Run intelligent matching
        try:
            from processors.simple_matcher import match_candidates
            
            st.success(f"🤖 Running AI analysis on {len(st.session_state.cvs)} candidates...")
            
            ranked = match_candidates(st.session_state.company, st.session_state.cvs)
            
            st.markdown("### 🏆 Ranked Candidates")
            
            for candidate in ranked:
                col1, col2, col3 = st.columns([1, 3, 1])
                score = candidate.get("overall_score", 0)
                
                with col1:
                    if score >= 80:
                        st.markdown(f"<div class='match-high'>{score}%</div>", unsafe_allow_html=True)
                    elif score >= 60:
                        st.markdown(f"<div class='match-medium'>{score}%</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='match-low'>{score}%</div>", unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"### #{candidate.get('rank')} - {candidate.get('name')}")
                    st.write(candidate.get('ranking'))
                
                with col3:
                    if st.button("👁️ Details", key=f"details_{candidate.get('name')}"):
                        st.session_state[f"show_{candidate.get('name')}"] = not st.session_state.get(f"show_{candidate.get('name')}", False)
                
                if st.session_state.get(f"show_{candidate.get('name')}"):
                    with st.expander("📋 Analysis"):
                        col_a, col_b, col_c, col_d = st.columns(4)
                        col_a.metric("Tech", f"{candidate.get('technical_score')}%")
                        col_b.metric("Culture", f"{candidate.get('culture_score')}%")
                        col_c.metric("CV", f"{candidate.get('cv_quality_score')}%")
                        col_d.metric("Overall", f"{candidate.get('overall_score')}%")
                        
                        st.write("**Strengths:**")
                        for s in candidate.get('strengths', []):
                            st.write(f"✅ {s}")
                        
                        st.write("**Feedback:**")
                        st.write(candidate.get('feedback'))

        except Exception as e:
            st.error(f"Error: {str(e)}")
            
            # Fallback to basic display
            st.subheader("Candidate Rankings")
            
            for idx, cv in enumerate(st.session_state.cvs, 1):
                match_score = 75 + (idx % 25) - 10
                
                col1, col2 = st.columns([1, 3])
                
                with col1:
                    if match_score >= 80:
                        st.markdown(f"<div class='match-high'>{match_score}%</div>", unsafe_allow_html=True)
                    elif match_score >= 60:
                        st.markdown(f"<div class='match-medium'>{match_score}%</div>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<div class='match-low'>{match_score}%</div>", unsafe_allow_html=True)
                
                with col2:
                    st.markdown(f"### {cv.get('name', 'N/A')}")
                    st.write(f"📚 {cv.get('degree', 'N/A')} | ⏱️ {cv.get('years_experience', 0)} years")


st.markdown("---")
st.markdown("🚀 **Inter-Sight** - Intelligent feedback for smarter hiring")
st.markdown(f"*Version 1.0 | Built for Hack-Nation 2025*")
