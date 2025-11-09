# 🎯 Inter-Sight - Intelligent Talent Matching Platform

**Status**: MVP for Hack-Nation Global AI Hackathon (Nov 8-9, 2025)

## What is Inter-Sight?

Inter-Sight is a feedback-first talent intelligence platform that uses AI to:

- ✅ Extract soft skills intelligently (semantic, hybrid approach)
- ✅ Match candidates to company culture and values
- ✅ Detect red flags with context and reasoning
- ✅ Generate personalized, actionable feedback for candidates
- ✅ Provide beautiful Tinder-like candidate ranking interface
- ✅ Process batch CVs with comprehensive analysis

## Why Inter-Sight?

**The Problem**: Hiring today is broken.
- Recruiters drown in CVs with no context
- Candidates get rejected without feedback
- Companies miss hidden talent
- Culture mismatches happen months after hire

**The Solution**: Intelligent feedback + soft skills + culture alignment

## Quick Start

### Prerequisites
- Python 3.10+
- Mistral API key (free tier: https://console.mistral.ai)

### Setup

```bash
# Clone or extract this repository
cd inter-sight

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add your MISTRAL_API_KEY
```

### Run Application

```bash
streamlit run ui/streamlit_app.py
```

Open browser to: `http://localhost:8501`

## Project Structure

```
inter-sight/
├── core/                          # Core modules
│   ├── config.py                 # Configuration management
│   ├── llm_provider.py           # LLM abstraction layer
│   └── constants.py              # Constants & schemas
│
├── processors/                    # Processing pipeline
│   ├── company_profiler.py       # Company profile builder
│   ├── cv_parser.py              # CV parsing & structure extraction
│   ├── skill_extractor.py        # Skill extraction (hybrid)
│   ├── culture_analyzer.py       # Culture value matching
│   ├── red_flag_detector.py      # Red flag detection
│   ├── matcher.py                # Multi-layer matching
│   └── feedback_generator.py     # Feedback generation
│
├── ui/                            # Streamlit UI
│   ├── streamlit_app.py          # Main application
│   └── components/               # UI components
│
├── data/                          # Data files
│   ├── sample_cvs/               # Sample CV data
│   └── sample_companies/         # Sample company profiles
│
├── utils/                         # Utility functions
│   ├── logger.py                 # Logging setup
│   ├── validators.py             # Input validation
│   └── formatters.py             # Output formatting
│
├── docs/                          # Documentation
├── requirements.txt              # Python dependencies
├── .env.example                  # Environment template
└── README.md                     # This file
```

## Features

### 1. LLM Abstraction Layer
Support for multiple LLM providers:
- Mistral (default, free tier)
- Claude (Anthropic)
- OpenAI (GPT)
- Local Llama (Ollama)

Just change `LLM_PROVIDER` in `.env`

### 2. Soft Skills Extraction
- Hybrid approach: heuristic + LLM enhancement
- Semantic understanding of implicit skills
- Confidence scoring with evidence trails
- Maps to company value framework

### 3. Comprehensive Red Flags
- Job hopping with context analysis
- Experience gaps detection
- CV quality scoring
- Skill progression tracking
- Overqualification/underqualification assessment
- Context-aware rather than binary

### 4. Hybrid Feedback Generation
- **Template-based**: Fast, structured feedback
- **LLM-enhanced**: Personalized insights and improvements
- **Interview prep**: Suggested talking points for recruiters
- **Growth path**: Actionable next steps for candidates

### 5. Beautiful UI
- Streamlit-powered responsive interface
- Tinder-like candidate cards with match %
- Color-coded matching (🟢 🟡 🔴)
- Expandable detail feedback views
- Company profile customization

## Usage

### Step 1: Set Company Profile
1. Navigate to "🏢 Company Setup" tab
2. Enter mission, values, skills needed, role description
3. Click "Save Company Profile"

### Step 2: Upload CVs
1. Go to "📤 Upload CVs" tab
2. Either upload JSON CV files OR load sample CVs
3. Click "Load and Process CVs"

### Step 3: View Results
1. Navigate to "🎯 Results" tab
2. See candidates ranked by match %
3. Click "View Details" for full feedback breakdown

## API Structure

### Company Profile Format
```json
{
  "name": "Company Name",
  "mission": "...",
  "values": ["Innovation", "Ownership", ...],
  "focus_skills": ["Leadership", "Communication", ...],
  "role_description": "..."
}
```

### CV Format
```json
{
  "name": "Candidate Name",
  "degree": "MS Computer Science",
  "university": "MIT",
  "years_experience": 7,
  "experience": [
    {
      "company": "...",
      "role": "...",
      "duration": "2 years",
      "description": "..."
    }
  ],
  "skills": ["Python", "Leadership", ...]
}
```

### Match Score Components
- **Technical**: 35% - Technical skills match
- **Soft Skills**: 30% - Soft skills alignment  
- **Culture Fit**: 20% - Values alignment
- **CV Quality**: 15% - CV structure & metrics

## Performance

- Batch processing: Up to 20 CVs at once
- LLM abstraction: Supports any provider
- Feedback generation: ~5-10 seconds per CV
- UI response: Real-time feedback with Streamlit

## Next Steps (Post-Hackathon)

- [ ] ATS integration (Workday, Lever, Greenhouse)
- [ ] Coaching recommendations
- [ ] Skill marketplace connection
- [ ] Analytics dashboard
- [ ] Resume optimization suggestions
- [ ] Salary benchmarking
- [ ] Retention prediction

## Technologies Used

- **Backend**: Python, Pydantic
- **LLM**: Mistral API (with abstraction for others)
- **Frontend**: Streamlit
- **Data**: Pandas, JSON
- **Deployment**: Cloud-ready architecture

## Submission Details

**Project**: Inter-Sight  
**Hackathon**: Hack-Nation Global AI Hackathon  
**Date**: November 8-9, 2025  
**Challenge**: SAP SkillSense - AI for Talent Identification

## Authors

Inter-Sight Team - Hack-Nation Hackathon 2025

## License

MIT License - See LICENSE file for details

---

## Support

For issues or questions:
1. Check documentation in `/docs` folder
2. Review code comments
3. Check `.env.example` for configuration help

**Built with ❤️ for Hack-Nation 2025**
