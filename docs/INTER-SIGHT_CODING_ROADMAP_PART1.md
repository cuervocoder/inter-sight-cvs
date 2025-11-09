# 🔨 INTER-SIGHT - DETAILED CODING ROADMAP

## 📋 BEFORE YOU START

### Prerequisites Checklist
- [ ] Mistral API key obtained (https://console.mistral.ai/)
- [ ] Python 3.10+ installed
- [ ] Git repo initialized
- [ ] `.env` file with MISTRAL_API_KEY
- [ ] Terminal ready
- [ ] Next 24 hours blocked (no distractions)

---

## 🚀 PHASE 0: SETUP (1 hour)

### Step 0.1: Create Project Structure
```bash
mkdir inter-sight
cd inter-sight

# Create directories
mkdir -p core processors ui/components data/sample_cvs data/sample_companies utils

# Initialize files
touch core/__init__.py core/config.py core/llm_provider.py core/constants.py
touch processors/__init__.py
touch ui/__init__.py ui/streamlit_app.py
touch utils/__init__.py
touch requirements.txt .env.example README.md
```

### Step 0.2: Setup requirements.txt
```txt
streamlit==1.28.0
pandas==2.1.0
numpy==1.24.0
anthropic==0.7.0
openai==1.3.0
mistralai==0.0.11
pydantic==2.4.0
python-dotenv==1.0.0
pdfplumber==0.9.0
plotly==5.17.0
streamlit-extras==0.3.0
```

### Step 0.3: Create .env.example
```env
# LLM Configuration
LLM_PROVIDER=mistral
MISTRAL_API_KEY=your_key_here
MISTRAL_MODEL=mistral-large

# App Configuration
APP_DEBUG=false
MAX_BATCH_CVS=20
FEEDBACK_MODE=hybrid
```

### Step 0.4: Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

---

## 🔧 PHASE 1: LLM ABSTRACTION (2 hours)

### Step 1.1: Create core/config.py

```python
"""Configuration management for Inter-Sight"""

from pydantic import BaseSettings
from typing import Optional
import os

class Settings(BaseSettings):
    """App-wide settings from .env"""
    
    # LLM Configuration
    llm_provider: str = "mistral"  # mistral, claude, openai, llama
    mistral_api_key: Optional[str] = None
    mistral_model: str = "mistral-large"
    
    # Claude (optional)
    claude_api_key: Optional[str] = None
    
    # OpenAI (optional)
    openai_api_key: Optional[str] = None
    
    # App Configuration
    app_debug: bool = False
    max_batch_cvs: int = 20
    feedback_mode: str = "hybrid"  # hybrid, template, llm
    
    class Config:
        env_file = ".env"
        case_sensitive = False

# Load settings
settings = Settings()
```

### Step 1.2: Create core/llm_provider.py (THE CORE)

```python
"""LLM Provider Abstraction - Supports any LLM"""

from abc import ABC, abstractmethod
from typing import Optional, Dict, List, Any
import json
from pydantic import BaseModel
import logging

logger = logging.getLogger(__name__)

class LLMConfig(BaseModel):
    """Configuration for LLM provider"""
    provider: str
    api_key: str
    model: str
    temperature: float = 0.7
    max_tokens: int = 1000

class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    def __init__(self, config: LLMConfig):
        self.config = config
        self.name = config.provider
    
    @abstractmethod
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text from prompt"""
        pass
    
    @abstractmethod
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        """Generate structured JSON output"""
        pass
    
    def batch_process(self, prompts: List[str]) -> List[str]:
        """Process multiple prompts (may be implemented per provider)"""
        return [self.generate_text(p) for p in prompts]


class MistralProvider(LLMProvider):
    """Mistral AI - FREE tier available"""
    
    def __init__(self, config: LLMConfig):
        super().__init__(config)
        try:
            from mistralai.client import MistralClient
            self.client = MistralClient(api_key=config.api_key)
        except Exception as e:
            logger.error(f"Failed to initialize Mistral: {e}")
            raise
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        """Generate text using Mistral"""
        try:
            from mistralai.models.chat_message import ChatMessage
            
            messages = [ChatMessage(role="user", content=prompt)]
            response = self.client.chat(
                model=self.config.model,
                messages=messages,
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Mistral generation failed: {e}")
            raise
    
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        """Generate JSON response from Mistral"""
        json_prompt = f"""{prompt}

You MUST return ONLY valid JSON. No markdown, no extra text.
{f"Schema: {json.dumps(schema, indent=2)}" if schema else ""}"""
        
        try:
            response = self.generate_text(json_prompt)
            # Clean up markdown code blocks if present
            response = response.strip()
            if response.startswith("```json"):
                response = response[7:]
            if response.endswith("```"):
                response = response[:-3]
            return json.loads(response.strip())
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {e}. Response: {response}")
            # Return empty dict on failure (will be caught upstream)
            return {}


class ClaudeProvider(LLMProvider):
    """Claude API - Anthropic (optional)"""
    
    def __init__(self, config: LLMConfig):
        super().__init__(config)
        try:
            from anthropic import Anthropic
            self.client = Anthropic(api_key=config.api_key)
        except Exception as e:
            logger.error(f"Failed to initialize Claude: {e}")
            raise
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        try:
            response = self.client.messages.create(
                model=self.config.model or "claude-3-5-sonnet-20241022",
                max_tokens=self.config.max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            logger.error(f"Claude generation failed: {e}")
            raise
    
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        json_prompt = f"""{prompt}

Return ONLY valid JSON.
{f"Schema: {json.dumps(schema, indent=2)}" if schema else ""}"""
        
        response = self.generate_text(json_prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {e}")
            return {}


class OpenAIProvider(LLMProvider):
    """OpenAI GPT API (optional)"""
    
    def __init__(self, config: LLMConfig):
        super().__init__(config)
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=config.api_key)
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI: {e}")
            raise
    
    def generate_text(self, prompt: str, **kwargs) -> str:
        try:
            response = self.client.chat.completions.create(
                model=self.config.model or "gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=self.config.temperature,
                max_tokens=self.config.max_tokens
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI generation failed: {e}")
            raise
    
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        json_prompt = f"""{prompt}

Return ONLY valid JSON.
{f"Schema: {json.dumps(schema, indent=2)}" if schema else ""}"""
        
        response = self.generate_text(json_prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {e}")
            return {}


# Factory function
def get_llm_provider(provider_name: str, api_key: str, 
                    model: str = "default") -> LLMProvider:
    """Factory to get LLM provider"""
    
    providers = {
        "mistral": MistralProvider,
        "claude": ClaudeProvider,
        "openai": OpenAIProvider,
    }
    
    if provider_name not in providers:
        raise ValueError(f"Unknown provider: {provider_name}")
    
    config = LLMConfig(
        provider=provider_name,
        api_key=api_key,
        model=model
    )
    
    return providers[provider_name](config)
```

### Step 1.3: Create core/constants.py

```python
"""Constants and schemas for Inter-Sight"""

# Soft Skills Taxonomy
SOFT_SKILLS_TAXONOMY = {
    "Leadership": {
        "keywords": ["led", "led team", "manage", "director", "head"],
        "weight": 0.9
    },
    "Communication": {
        "keywords": ["present", "communicate", "speak", "write", "article"],
        "weight": 0.8
    },
    "Problem-Solving": {
        "keywords": ["solve", "troubleshoot", "debug", "designed", "architecture"],
        "weight": 0.85
    },
    "Adaptability": {
        "keywords": ["navigate", "transition", "changed", "adjusted", "flexible"],
        "weight": 0.7
    },
    "Collaboration": {
        "keywords": ["team", "partner", "collaborate", "together", "cross-functional"],
        "weight": 0.75
    },
    "Ownership": {
        "keywords": ["owned", "responsible", "drove", "led", "founder"],
        "weight": 0.9
    },
    "Learning Mindset": {
        "keywords": ["learn", "course", "certified", "self-taught", "training"],
        "weight": 0.8
    },
}

# Red Flag Thresholds
RED_FLAG_THRESHOLDS = {
    "job_hopping": 1.5,  # jobs/year
    "employment_gap": 6,  # months
    "cv_quality_low": 0.5,
}

# Match Score Weights
MATCH_WEIGHTS = {
    "technical": 0.35,
    "soft_skills": 0.30,
    "culture_fit": 0.20,
    "cv_quality": 0.15,
}

# Feedback Schemas
SOFT_SKILLS_EXTRACTION_SCHEMA = {
    "type": "object",
    "properties": {
        "soft_skills": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "skill": {"type": "string"},
                    "confidence": {"type": "number"},
                    "evidence": {"type": "string"}
                }
            }
        }
    }
}
```

---

## 📊 PHASE 2: CORE PROCESSORS (6 hours)

> [Continued in next message - too long for single file]

---

## 🎨 PHASE 3: UI/STREAMLIT (4 hours)

> [Will provide UI code in next sections]

---

## 📦 NEXT STEPS

1. **RIGHT NOW**: Create structure + Phase 0/1 files
2. **TEST**: `python -c "from core.llm_provider import get_llm_provider; print('LLM OK')"`
3. **THEN**: Continue with Phase 2 (Processors)

---

## ✅ CHECKPOINT: After Phase 1

You should have:
- ✅ Project structure created
- ✅ Dependencies installed
- ✅ LLM abstraction working (tested with Mistral)
- ✅ Config system working (.env loaded)

**Ready to move to Phase 2?**
