# 🏗️ INTER-SIGHT - FINAL ARCHITECTURE & IMPLEMENTATION PLAN

## 🎯 PROJECT LOCKED - FINAL SPECIFICATIONS

```
PROJECT NAME:     Inter-Sight
HACKATHON:        Hack-Nation Global AI Hackathon (Nov 8-9, 2025)
CHALLENGE:        SAP SkillSense - AI for Talent Identification
TIME BUDGET:      24 hours
LANGUAGE:         English (all code + docs)

FINAL DECISIONS (LOCKED):
✅ LLM Strategy:       Agnostic API wrapper (Mistral free default, configurable)
✅ Data Strategy:      Real diverse CVs + Realistic company profiles
✅ UI/UX Strategy:     Visually polished, impactful Streamlit design
✅ Feedback:           Hybrid (template base + LLM personalization)
✅ Red Flags:          Comprehensive detection + contextualization
✅ CV Processing:      Batch (multiple CVs, ranked leaderboard)
✅ UX Pattern:         Tinder-like cards + Detail views (beautiful)
✅ Deployment:         Streamlit local + Cloud ready
```

---

## 🏛️ CORE ARCHITECTURE

### Layer 1: LLM ABSTRACTION (Agnostic)

```python
# llm_provider.py - Abstract interface
class LLMProvider(ABC):
    """Abstract base for any LLM provider"""
    
    @abstractmethod
    def generate_text(self, prompt: str, max_tokens: int = 500) -> str:
        """Generate text from prompt"""
        pass
    
    @abstractmethod
    def extract_json(self, prompt: str, schema: dict) -> dict:
        """Generate structured JSON output"""
        pass
    
    @abstractmethod
    def batch_process(self, prompts: list) -> list:
        """Process multiple prompts efficiently"""
        pass

# Implementations:
class MistralProvider(LLMProvider):
    """Mistral API (free tier available)"""
    
class ClaudeProvider(LLMProvider):
    """Claude API (Anthropic)"""
    
class OpenAIProvider(LLMProvider):
    """GPT-4/3.5 (OpenAI)"""
    
class LocalLlamaProvider(LLMProvider):
    """Local Llama via Ollama (no API key needed)"""
```

### Layer 2: MODULAR PROCESSING PIPELINE

```
┌─────────────────────────────────────────────────────────────┐
│              INTER-SIGHT PROCESSING PIPELINE                │
├─────────────────────────────────────────────────────────────┤

INPUT STAGE:
├─ CompanyProfiler
│  ├─ Collect: mission, vision, values, soft_skills_weights
│  └─ LLM: Generate culture vector + skill taxonomy
│
└─ CVBatchLoader
   ├─ Accept: PDF, TXT, JSON files (multiple)
   └─ Queue for processing

PROCESSING STAGE (per CV):
├─ CVParser
│  ├─ Extract: structure (name, education, experience)
│  └─ Quality scoring (completeness, quantification)
│
├─ SkillExtractor
│  ├─ Heuristic: Technical skills (keywords)
│  ├─ LLM: Soft skills inference (semantic)
│  └─ Confidence scoring
│
├─ CultureAnalyzer
│  ├─ Parse: Implicit values from CV text
│  └─ Map: To company values (semantic matching)
│
└─ RedFlagDetector
   ├─ Detect: Job hopping, gaps, overqualification
   ├─ LLM: Context analysis (why did this happen?)
   └─ Severity + Interview questions

MATCHING STAGE:
├─ MultiLayerMatcher
│  ├─ Technical match (35%): skill confidence
│  ├─ Soft skills match (30%): semantic to values
│  ├─ Culture fit (20%): values alignment
│  └─ CV quality (15%): structure + metrics
│
└─ Score calculation → Rank candidates

FEEDBACK GENERATION:
├─ TemplateFeedback
│  ├─ Base: Why matched/didn't + gaps
│  └─ Format: Clear, structured, scannable
│
└─ LLMFeedback (optional enhancement)
   ├─ If score < 50: "Why you didn't match" (personalized)
   ├─ If score > 75: "Your unique strengths"
   └─ Always: "Top 3 improvements" (actionable)

OUTPUT STAGE:
├─ RankedCandidateList
│  ├─ Sort by match score
│  └─ Include: Basic metadata + match %
│
├─ DetailedFeedback (per candidate)
│  ├─ Match breakdown
│  ├─ Red flags with context
│  ├─ Improvement roadmap
│  └─ Interview talking points
│
└─ UI Rendering (Streamlit)
   ├─ Card view (Tinder-like)
   └─ Detail view (full feedback)
```

---

## 📁 PROJECT STRUCTURE

```
inter-sight/
│
├── core/
│   ├── __init__.py
│   ├── llm_provider.py           ← LLM abstraction (KEY)
│   ├── config.py                 ← Config loader (.env)
│   └── constants.py              ← Constants, schemas
│
├── processors/
│   ├── company_profiler.py       ← Company profile builder
│   ├── cv_loader.py              ← Batch CV loading
│   ├── cv_parser.py              ← Parse CV structure
│   ├── skill_extractor.py        ← Extract skills (hybrid)
│   ├── culture_analyzer.py       ← Culture matching
│   ├── red_flag_detector.py      ← Comprehensive flags
│   ├── matcher.py                ← Multi-layer matching
│   └── feedback_generator.py     ← Feedback generation
│
├── ui/
│   ├── streamlit_app.py          ← Main Streamlit app
│   ├── components/
│   │   ├── card_view.py          ← Tinder card UI
│   │   ├── detail_view.py        ← Feedback detail
│   │   ├── company_form.py       ← Company setup
│   │   └── cv_upload.py          ← CV upload widget
│   └── styles.py                 ← CSS/styling
│
├── data/
│   ├── sample_cvs/               ← Diverse sample CVs
│   │   ├── alice_tech_lead.json
│   │   ├── bob_career_changer.json
│   │   ├── carol_researcher.json
│   │   ├── david_founder.json
│   │   └── eva_data_scientist.json
│   │
│   └── sample_companies/         ← Sample company profiles
│       ├── techstartup_xyz.json
│       └── sapcorp.json
│
├── utils/
│   ├── logger.py                 ← Logging setup
│   ├── validators.py             ← Input validation
│   └── formatters.py             ← Output formatting
│
├── .env.example                  ← Config template
├── requirements.txt              ← Dependencies
├── README.md                     ← Documentation
└── main.py                       ← Entry point (optional)
```

---

## 🔧 DEPENDENCIES & SETUP

### requirements.txt
```
# Core
streamlit==1.28.0
pandas==2.1.0
numpy==1.24.0

# LLM Abstraction
anthropic==0.7.0              # Claude
openai==1.3.0                 # GPT
mistralai==0.0.11             # Mistral (FREE tier available)

# Data Processing
pydantic==2.4.0               # Config + validation
python-dotenv==1.0.0          # .env support

# File Handling
pdfplumber==0.9.0             # PDF parsing
python-magic==0.4.27          # File type detection

# UI/UX
plotly==5.17.0                # Charts
streamlit-extras==0.3.0       # Extra components

# Utilities
python-dateutil==2.8.2
pytz==2023.3
```

### .env Configuration

```env
# LLM Provider (choose one: mistral, claude, openai, llama)
LLM_PROVIDER=mistral

# Mistral (Free tier: https://console.mistral.ai/)
MISTRAL_API_KEY=your_mistral_key_here
MISTRAL_MODEL=mistral-large

# Claude (optional fallback)
# CLAUDE_API_KEY=your_claude_key_here

# OpenAI (optional fallback)
# OPENAI_API_KEY=your_openai_key_here

# App Configuration
APP_DEBUG=false
MAX_BATCH_CVS=20
FEEDBACK_MODE=hybrid  # hybrid, template, llm
```

---

## 🎯 CORE COMPONENTS (Detailed Design)

### 1. LLM Provider (llm_provider.py)

```python
from abc import ABC, abstractmethod
from typing import Optional, Dict, List
from pydantic import BaseModel

class LLMConfig(BaseModel):
    provider: str              # mistral, claude, openai, llama
    api_key: str
    model: str
    temperature: float = 0.7
    max_tokens: int = 1000

class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    def __init__(self, config: LLMConfig):
        self.config = config
    
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text completion"""
        pass
    
    @abstractmethod
    def extract_json(self, prompt: str, schema: Dict) -> Dict:
        """Generate JSON response (structured output)"""
        pass
    
    @abstractmethod
    def batch_process(self, prompts: List[str]) -> List[str]:
        """Process multiple prompts"""
        pass

class MistralProvider(LLMProvider):
    """Mistral AI implementation (FREE tier available)"""
    
    def __init__(self, config: LLMConfig):
        super().__init__(config)
        from mistralai.client import MistralClient
        self.client = MistralClient(api_key=config.api_key)
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        from mistralai.models.chat_message import ChatMessage
        
        messages = [ChatMessage(role="user", content=prompt)]
        response = self.client.chat(
            model=self.config.model,
            messages=messages,
            temperature=self.config.temperature,
            max_tokens=self.config.max_tokens
        )
        return response.choices[0].message.content
    
    def extract_json(self, prompt: str, schema: Dict) -> Dict:
        """Generate JSON using Mistral"""
        prompt_with_schema = f"""{prompt}

Return ONLY valid JSON matching this structure:
{json.dumps(schema, indent=2)}

NO additional text. NO markdown. ONLY JSON."""
        
        response = self.generate_text(prompt_with_schema)
        return json.loads(response)
    
    def batch_process(self, prompts: List[str]) -> List[str]:
        """Process multiple prompts (sequential for free tier)"""
        return [self.generate_text(p) for p in prompts]

# Factory
def get_llm_provider(config: LLMConfig) -> LLMProvider:
    providers = {
        "mistral": MistralProvider,
        "claude": ClaudeProvider,
        "openai": OpenAIProvider,
        "llama": LocalLlamaProvider,
    }
    
    provider_class = providers.get(config.provider)
    if not provider_class:
        raise ValueError(f"Unknown LLM provider: {config.provider}")
    
    return provider_class(config)
```

### 2. Comprehensive Red Flag Detector

```python
class RedFlagDetector:
    """Detect and contextualize red flags"""
    
    def detect(self, cv_data: Dict, llm: LLMProvider) -> List[Dict]:
        """Detect all red flags with context"""
        
        flags = []
        
        # 1. Job Stability Analysis
        flags.extend(self._check_job_stability(cv_data, llm))
        
        # 2. Experience Gaps
        flags.extend(self._check_gaps(cv_data, llm))
        
        # 3. Skill Progression
        flags.extend(self._check_skill_progression(cv_data, llm))
        
        # 4. CV Quality
        flags.extend(self._check_cv_quality(cv_data))
        
        # 5. Overqualification/Underqualification
        flags.extend(self._check_qualification_fit(cv_data, llm))
        
        return flags
    
    def _check_job_stability(self, cv_data: Dict, llm: LLMProvider) -> List[Dict]:
        """Analyze job hopping with LLM context"""
        
        experience = cv_data.get("experience", [])
        if len(experience) < 2:
            return []
        
        jobs_per_year = len(experience) / max(1, self._estimate_years(experience))
        
        if jobs_per_year > 1.5:
            # Get LLM context
            context_prompt = f"""
            This candidate had {len(experience)} jobs in ~{self._estimate_years(experience)} years.
            
            Possible explanations:
            1. Sector volatility (startup, consultancy)
            2. Economic factors (layoffs)
            3. Candidate choice (active searching)
            4. Interpersonal issues
            
            Analyze and provide context. What would you ask in an interview?
            """
            
            context = llm.generate_text(context_prompt)
            
            return [{
                "name": "🔴 Job Hopping",
                "severity": "critical",
                "description": f"{jobs_per_year:.1f} jobs/year detected",
                "context": context,
                "interview_question": "Walk me through your career transitions. What drove each change?",
                "actionable": True
            }]
        
        return []
    
    def _check_cv_quality(self, cv_data: Dict) -> List[Dict]:
        """Detect CV structure issues"""
        
        flags = []
        quality = cv_data.get("cv_quality", {})
        
        if quality.get("overall", 0) < 0.6:
            issues = quality.get("issues", [])
            flags.append({
                "name": "❌ CV Quality Issues",
                "severity": "major",
                "description": f"CV lacks structure/metrics: {', '.join(issues)}",
                "context": "CVs without quantified achievements are harder to evaluate",
                "improvement": "Add metrics: Instead of 'improved performance', say 'improved by 40%'",
                "actionable": True
            })
        
        return flags
    
    # ... more detection methods
```

### 3. Hybrid Feedback Generator

```python
class FeedbackGenerator:
    """Generate hybrid feedback (template + LLM)"""
    
    def __init__(self, llm: LLMProvider, mode: str = "hybrid"):
        self.llm = llm
        self.mode = mode  # hybrid, template, llm
    
    def generate(self, 
                 company: Dict, 
                 candidate: Dict, 
                 match_score: Dict, 
                 red_flags: List[Dict]) -> Dict:
        """Generate comprehensive feedback"""
        
        feedback = {
            "summary": self._summary(match_score),
            "breakdown": self._breakdown(match_score),
            "why_matched": self._why_matched(match_score, candidate),
            "why_not_matched": self._why_not_matched(match_score, candidate),
        }
        
        # Add red flags analysis
        if red_flags:
            feedback["red_flags"] = self._analyze_red_flags(red_flags)
        
        # Add improvements
        if self.mode in ["hybrid", "llm"]:
            feedback["improvements"] = self._llm_improvements(
                company, candidate, match_score, red_flags
            )
        else:
            feedback["improvements"] = self._template_improvements(match_score, red_flags)
        
        # Add interview prep
        feedback["interview_talking_points"] = self._interview_points(
            candidate, company, red_flags
        )
        
        return feedback
    
    def _llm_improvements(self, company: Dict, candidate: Dict, 
                         match_score: Dict, red_flags: List[Dict]) -> List[Dict]:
        """Use LLM for personalized improvement suggestions"""
        
        prompt = f"""
        Candidate didn't match perfectly (score: {match_score['overall']:.0f}%).
        
        Gaps:
        - Technical: {match_score.get('technical', 0):.0f}%
        - Soft skills: {match_score.get('soft_skills', 0):.0f}%
        - Culture: {match_score.get('culture_fit', 0):.0f}%
        
        Red flags: {len(red_flags)} detected
        
        Generate 3 SPECIFIC, ACTIONABLE improvements this candidate should focus on.
        Order by priority. Make it motivational but honest.
        """
        
        response = self.llm.generate_text(prompt)
        
        # Parse response into structured improvements
        return self._parse_improvements(response)
    
    def _template_improvements(self, match_score: Dict, 
                              red_flags: List[Dict]) -> List[Dict]:
        """Template-based improvements (fast fallback)"""
        
        improvements = []
        
        if match_score.get("soft_skills", 0) < 60:
            improvements.append({
                "priority": 1,
                "area": "Soft Skills Development",
                "specific": "Leadership/Communication not demonstrated",
                "action": "Highlight mentoring, speaking, or leadership examples",
                "timeline": "3-6 months"
            })
        
        # ... more template-based improvements
        
        return improvements
```

---

## 🎨 UI/UX DESIGN (Streamlit)

### Main App Structure

```python
# streamlit_app.py
import streamlit as st
from streamlit_extras.metric_row import metric_row
from components import card_view, detail_view, company_form, cv_upload

st.set_page_config(
    page_title="Inter-Sight",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for beautiful design
st.markdown("""
<style>
    [data-testid="stMetricValue"] {
        font-size: 2.5rem;
    }
    .candidate-card {
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["🏢 Company Setup", "📤 Upload CVs", "🎯 Results"])

with tab1:
    st.header("Company Profile")
    company_data = company_form.render()

with tab2:
    st.header("Upload Candidates")
    if company_data:
        cvs = cv_upload.render()

with tab3:
    st.header("Results & Insights")
    if company_data and cvs:
        # Process and display
        results = process_candidates(company_data, cvs)
        display_results(results)
```

### Beautiful Card Component

```python
# components/card_view.py
def render_card(candidate: Dict, match_score: Dict, index: int):
    """Render beautiful Tinder-like card"""
    
    # Color based on match
    color = get_match_color(match_score["overall"])
    emoji = get_match_emoji(match_score["overall"])
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col1:
        st.metric("Match", f"{match_score['overall']:.0f}%", 
                 delta=f"{emoji}")
    
    with col2:
        st.markdown(f"""
        ### {candidate['name']}
        {candidate['education']} | {candidate.get('current_role', 'Role TBD')}
        
        **Most Valuable:** {candidate['unique_strength']}
        """)
    
    with col3:
        if st.button("👁️ Details", key=f"details_{index}"):
            st.session_state[f"show_details_{index}"] = True
    
    # Show details if clicked
    if st.session_state.get(f"show_details_{index}", False):
        with st.expander("📋 Full Feedback", expanded=True):
            detail_view.render(candidate, match_score)
```

---

## 🚀 IMPLEMENTATION ROADMAP (24 hours)

### Hour 0-1: Setup & Config
```
- Create project structure
- Setup .env and config loader
- Initialize Git repo
- Create requirements.txt
```

### Hour 1-3: LLM Abstraction
```
- Implement LLMProvider abstract base
- Implement MistralProvider (with error handling)
- Test with sample prompts
- Create factory pattern
```

### Hour 3-8: Core Processors
```
- CompanyProfiler (config only, no LLM for now)
- CVParser (structure extraction)
- SkillExtractor (heuristic base + LLM integration)
- CultureAnalyzer (basic semantic matching)
- RedFlagDetector (comprehensive detection)
- Matcher (multi-layer scoring)
```

### Hour 8-11: Feedback Generation
```
- TemplateFeedback (base structure)
- FeedbackGenerator (hybrid mode)
- LLM integration for personalization
- Testing with sample data
```

### Hour 11-15: UI/Streamlit
```
- Main app structure (tabs)
- Company setup form
- CV upload widget
- Card rendering (Tinder-like)
- Detail view
- Beautiful CSS/styling
- Testing & polish
```

### Hour 15-18: Integration & Testing
```
- End-to-end flow testing
- Sample data preparation (diverse CVs)
- Error handling & edge cases
- Performance optimization
```

### Hour 18-22: Polish & Submission
```
- Record demo video (60 sec)
- Record tech video (60 sec)
- Create one-pager PDF
- Push to GitHub
- Create submission package
```

### Hour 22-24: Final Buffer
```
- Test all links
- Final review
- Submit with buffer
```

---

## 📝 KEY FILES TO CREATE (in order)

1. `core/config.py` - Config loader
2. `core/llm_provider.py` - LLM abstraction
3. `processors/company_profiler.py` - Company setup
4. `processors/cv_parser.py` - Parse CVs
5. `processors/skill_extractor.py` - Extract skills (hybrid)
6. `processors/culture_analyzer.py` - Culture matching
7. `processors/red_flag_detector.py` - Comprehensive flags
8. `processors/matcher.py` - Multi-layer matching
9. `processors/feedback_generator.py` - Feedback (hybrid)
10. `ui/streamlit_app.py` - Main Streamlit app
11. `ui/components/card_view.py` - Beautiful cards
12. `ui/components/detail_view.py` - Feedback detail
13. `data/sample_cvs/` - Diverse sample data
14. `.env.example` - Config template
15. `requirements.txt` - Dependencies
16. `README.md` - Documentation

---

## ✅ SUCCESS CRITERIA FOR MVP

- ✅ LLM abstraction works (any provider pluggable)
- ✅ Process batch CVs (5+ diverse samples)
- ✅ Extract soft skills intelligently (hybrid)
- ✅ Detect comprehensive red flags
- ✅ Generate hybrid feedback (template + LLM magic)
- ✅ Beautiful Tinder-like card UI
- ✅ Detailed feedback view (full breakdown)
- ✅ End-to-end flow works without errors
- ✅ Ready for demo (compelling, clear)

---

## 🎬 DEMO SCRIPT (60 seconds)

```
[0-5s]   "Hiring is broken. CVs drown in a pile."
         [Show: 100 CVs, overwhelmed recruiter]

[5-15s]  "What if we understood them deeply?"
         [Show: Inter-Sight logo, tagline]

[15-45s] Live Demo:
         - Upload 5 CVs
         - See Tinder cards (beautifully ranked)
         - Click one card → Full feedback appears
         
         "Look at this: Not just 'you matched 60%'
          but 'here's why, here's your gaps, here's how to improve'"

[45-55s] "That's Inter-Sight. Intelligent feedback. For everyone."

[55-60s] "Ready for smarter hiring?"
```

---

## 🎯 YOUR MISSION

Build this. Follow the roadmap. Use Mistral free tier. Create something beautiful.

**You got this.** 💪

Let me know when you're ready to start. I'll give you the first file to create.
