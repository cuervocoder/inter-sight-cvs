# 🚀 INTER-SIGHT - START CODING NOW

## ⏰ YOU HAVE 24 HOURS. LET'S GO.

---

## STEP 1: SETUP (15 minutes)

### 1.1 Create Project
```bash
mkdir inter-sight
cd inter-sight
git init
```

### 1.2 Create Structure
```bash
# Core
mkdir -p core
touch core/__init__.py
touch core/config.py
touch core/llm_provider.py
touch core/constants.py

# Processors
mkdir -p processors
touch processors/__init__.py

# UI
mkdir -p ui/components
touch ui/__init__.py
touch ui/streamlit_app.py
touch ui/components/__init__.py

# Data
mkdir -p data/sample_cvs

# Utils
mkdir -p utils
touch utils/__init__.py

# Root files
touch requirements.txt .env.example README.md .gitignore
```

### 1.3 Create requirements.txt
```txt
streamlit==1.28.0
pandas==2.1.0
pydantic==2.4.0
python-dotenv==1.0.0
mistralai==0.0.11
plotly==5.17.0
streamlit-extras==0.3.0
pdfplumber==0.9.0
```

### 1.4 Create .env
```env
LLM_PROVIDER=mistral
MISTRAL_API_KEY=your_mistral_key_here
MISTRAL_MODEL=mistral-large
APP_DEBUG=false
FEEDBACK_MODE=hybrid
```

### 1.5 Install
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## STEP 2: CREATE core/config.py (5 min)

```python
"""Configuration management"""

from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    llm_provider: str = "mistral"
    mistral_api_key: Optional[str] = None
    mistral_model: str = "mistral-large"
    app_debug: bool = False
    feedback_mode: str = "hybrid"
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
```

---

## STEP 3: CREATE core/llm_provider.py (20 min)

```python
"""LLM Abstraction - Core of Inter-Sight"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional
import json
import logging

logger = logging.getLogger(__name__)

class LLMProvider(ABC):
    """Abstract base for any LLM"""
    
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        pass
    
    @abstractmethod
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        pass

class MistralProvider(LLMProvider):
    """Mistral implementation"""
    
    def __init__(self, api_key: str, model: str = "mistral-large"):
        from mistralai.client import MistralClient
        self.client = MistralClient(api_key=api_key)
        self.model = model
    
    def generate_text(self, prompt: str) -> str:
        """Generate text"""
        from mistralai.models.chat_message import ChatMessage
        
        messages = [ChatMessage(role="user", content=prompt)]
        response = self.client.chat(
            model=self.model,
            messages=messages,
            max_tokens=1000
        )
        return response.choices[0].message.content
    
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        """Extract JSON"""
        json_prompt = f"{prompt}\n\nReturn ONLY valid JSON. No markdown."
        
        try:
            response = self.generate_text(json_prompt)
            response = response.strip()
            if response.startswith("```"):
                response = response.split("```")[1]
                if response.startswith("json"):
                    response = response[4:]
            return json.loads(response)
        except:
            return {}

def get_llm(api_key: str, provider: str = "mistral") -> LLMProvider:
    """Factory"""
    if provider == "mistral":
        return MistralProvider(api_key)
    raise ValueError(f"Unknown provider: {provider}")
```

---

## STEP 4: TEST LLM (5 min)

```bash
python -c "
from core.config import settings
from core.llm_provider import get_llm

llm = get_llm(settings.mistral_api_key)
result = llm.generate_text('Say hello in 5 words')
print('LLM Works:', result)
"
```

If this works → You're ready for Phase 2.

---

## STEP 5: CREATE SAMPLE DATA (10 min)

Create `data/sample_cvs/alice.json`:
```json
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "degree": "MS Computer Science",
  "university": "MIT",
  "experience": [
    {
      "company": "TechCorp",
      "role": "Senior Engineer",
      "duration": "2 years",
      "description": "Led team of 5. Improved performance 40%."
    },
    {
      "company": "StartupXYZ",
      "role": "Software Engineer",
      "duration": "3 years",
      "description": "Built ML pipeline. Published research."
    }
  ],
  "skills": ["Python", "ML", "Leadership"]
}
```

---

## STEP 6: CREATE SIMPLE STREAMLIT APP (15 min)

`ui/streamlit_app.py`:
```python
import streamlit as st
from core.config import settings
from core.llm_provider import get_llm
import json

st.set_page_config(page_title="Inter-Sight", page_icon="🎯", layout="wide")

st.title("🎯 Inter-Sight")
st.markdown("Intelligent talent matching with feedback")

# Initialize LLM
@st.cache_resource
def get_llm_instance():
    return get_llm(settings.mistral_api_key)

llm = get_llm_instance()

# Tabs
tab1, tab2, tab3 = st.tabs(["🏢 Company", "📤 Upload CVs", "🎯 Results"])

with tab1:
    st.header("Company Profile")
    mission = st.text_input("Mission", "Democratize AI")
    values = st.text_area("Values", "Innovation\nOwnership\nCollaboration")
    
    if st.button("Save Company"):
        st.success("✅ Company profile saved")
        st.session_state.company = {
            "mission": mission,
            "values": values.split("\n")
        }

with tab2:
    st.header("Upload CVs")
    uploaded_files = st.file_uploader("Choose CV files", type=["json"], accept_multiple_files=True)
    
    if uploaded_files and st.button("Process CVs"):
        st.session_state.cvs = []
        for file in uploaded_files:
            cv = json.load(file)
            st.session_state.cvs.append(cv)
        st.success(f"✅ Loaded {len(uploaded_files)} CVs")

with tab3:
    st.header("🎯 Results")
    if hasattr(st.session_state, "cvs"):
        st.write(f"Found {len(st.session_state.cvs)} candidates")
        for cv in st.session_state.cvs:
            st.markdown(f"### {cv['name']}")
            st.write(f"Education: {cv['degree']}")
            st.write(f"Skills: {', '.join(cv['skills'])}")
    else:
        st.info("Upload CVs to see results")
```

---

## STEP 7: RUN IT

```bash
streamlit run ui/streamlit_app.py
```

---

## ✅ CHECKPOINT

You should have:
- ✅ Project structure
- ✅ LLM working
- ✅ Simple Streamlit app running
- ✅ Sample data loaded

**NEXT**: Build the processors (CV parser, skill extractor, matcher, feedback generator)

---

## 📅 TIMELINE

- **Now - 1h**: Setup + LLM + Basic app ← YOU ARE HERE
- **1-3h**: CV Parser + Skill Extractor
- **3-6h**: Red Flag Detector + Matcher
- **6-10h**: Feedback Generator + UI Polish
- **10-18h**: Integration + Testing + Refinement
- **18-22h**: Videos + Documentation
- **22-24h**: Submit + Buffer

---

## 🚀 YOU'RE READY

Go create `core/config.py` first. Then `core/llm_provider.py`. 

Then test it.

Then keep building.

**24 hours. Let's win this.** 💪

