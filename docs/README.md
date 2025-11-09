# 🎯 SkillSense - AI-Powered Talent Matching Platform

**"Intelligent hiring. Actionable feedback. Real impact."**

SkillSense is an AI-powered platform that revolutionizes talent matching by going beyond basic resume screening. It matches candidates to company culture and provides **structured, actionable feedback** explaining why candidates matched or didn't, helping both recruiters and candidates improve.

---

## 🌟 Key Differentiators

### 1. **Structured Feedback for Every Candidate** ⭐
Unlike traditional matching tools, SkillSense provides detailed explanations:
- ✅ **Why they matched**: "Strong technical foundation (Python 90% confidence), demonstrated leadership (5 years managing teams)"
- ❌ **Why they didn't match**: "Critical soft skill gap: Leadership not demonstrated. Company priority: 90%. Red flag: 5 jobs in 1 year suggests instability"
- 💡 **How to improve**: "Add 3 specific improvements: (1) Highlight leadership examples, (2) Add metrics to achievements, (3) Address employment gaps"

### 2. **Soft Skills ↔ Company Values Matching** 🎯
Deep semantic matching between:
- Company mission/vision/values → extracted soft skills profile
- What company needs (weighted) → what candidate has (with confidence scores)
- **Example**: Company values "Innovation" → Matches with candidate's "Self-taught learning" + "Entrepreneurial projects"

### 3. **Intelligent Red Flag Detection** 🚨
Proactively identifies risks:
- Job hopping (5 jobs/year) → 🔴 Critical
- Employment gaps → ⚠️ Minor
- CV quality issues → Actionable: "Add quantified metrics to achievements"
- Missing critical skills → With interview questions: "How would you develop leadership?"

### 4. **Tinder-like UX** 📱
Intuitive candidate card interface:
```
┌──────────────────────────────┐
│ Alice Johnson    Match: 85% 🟢│
│─────────────────────────────  │
│ Most Valuable: "Leadership + Deep Tech"
│                              │
│ Technical: 90% ✅          │
│ Soft Skills: 78% ✅        │
│ Culture Fit: 85% ✅        │
│                              │
│ [📧 Contact] [👉 Details]  │
└──────────────────────────────┘
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│           SKILLSENSE PLATFORM                       │
├─────────────────────────────────────────────────────┤
│                                                     │
│  1. COMPANY SETUP                                  │
│     • Configure mission, vision, values            │
│     • Define soft skills requirements (weighted)   │
│                                                     │
│  2. CV PARSING & EXTRACTION                        │
│     • Extract from PDF/TXT/JSON                    │
│     • Assess CV quality (completeness, metrics)    │
│                                                     │
│  3. SKILL EXTRACTION (Claude API)                  │
│     • Technical skills detection                   │
│     • Soft skills inference from context           │
│     • Unique strengths identification              │
│                                                     │
│  4. RED FLAG DETECTION                             │
│     • Job stability analysis                       │
│     • Career gap detection                         │
│     • CV quality assessment                        │
│                                                     │
│  5. MULTI-LAYER MATCHING                           │
│     • Technical: 35%                               │
│     • Soft Skills: 30% (KEY DIFFERENTIATOR)        │
│     • Culture Fit: 20%                             │
│     • CV Quality: 15%                              │
│                                                     │
│  6. INTELLIGENT FEEDBACK GENERATION                │
│     • Why matched/didn't                           │
│     • Red flags with context                       │
│     • Actionable improvement areas                 │
│     • Interview talking points                     │
│                                                     │
│  7. INTERACTIVE UI                                 │
│     • Tinder-like cards                            │
│     • Detailed analysis dashboards                 │
│     • Analytics & insights                         │
│                                                     │
└─────────────────────────────────────────────────────┘
```

---

## 📋 Features

### For Recruiters 🏢
- **Fast matching**: Upload CVs, get instant matches (🟢/🟡/🔴)
- **Deep insights**: Understand why each candidate matches
- **Risk assessment**: Identify red flags with context
- **Team composition**: See skill gaps in organization
- **Interview prep**: Generated talking points and questions

### For Candidates 👤
- **Constructive feedback**: Learn why you didn't match
- **Improvement roadmap**: Specific, actionable steps to improve
- **Strength highlighting**: Understand your unique value
- **Career guidance**: Recommendations based on profile

---

## 🚀 Quick Start

### Installation

```bash
# Clone or download
cd skillsense

# Install dependencies
pip install -r requirements.txt

# Set up environment (optional, for Claude API)
echo "ANTHROPIC_API_KEY=your_key_here" > .env
```

### Run the App

```bash
streamlit run skillsense_main.py
```

**App opens at**: http://localhost:8501

### First 5 Minutes

1. **Tab 1 - Company Setup** (2 min)
   - Enter company info (name, mission, vision)
   - Set soft skill weights (defaults provided)
   - Click "Save Company Profile"

2. **Tab 2 - Upload CVs** (1 min)
   - Click "Upload CV files"
   - Select sample CVs or your own
   - Click "Process CVs"

3. **Tab 3 - Match Candidates** (1 min)
   - Click "Run Matching Algorithm"
   - View Tinder-style cards
   - Click "Details" to see full feedback

4. **Tab 4 - Analytics** (1 min)
   - See match distribution
   - Identify top candidates
   - Export insights

---

## 📊 Data Format

### Company Profile
```json
{
  "name": "TechStartup XYZ",
  "mission": "Democratize AI",
  "vision": "Scale globally",
  "values": ["Innovation", "Ownership", "Collaboration"],
  "soft_skills_weights": {
    "Leadership": 0.9,
    "Communication": 0.8,
    "Problem-Solving": 0.85,
    "Adaptability": 0.7,
    "Collaboration": 0.75
  }
}
```

### CV Input (JSON)
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "education": "BS Computer Science",
  "experience": [
    {
      "company": "Tech Corp",
      "role": "Senior Engineer",
      "duration": "2020-Present",
      "achievements": "Led team, improved performance 40%"
    }
  ],
  "skills": ["Python", "Leadership", "Communication"]
}
```

### Output - Feedback Report
```json
{
  "overall": 85,
  "match_breakdown": {
    "technical": 90,
    "soft_skills": 78,
    "culture_fit": 85,
    "cv_quality": 75
  },
  "why_matched": [
    "✅ Strong technical foundation: Python, AWS, Docker",
    "✅ Demonstrated soft skills align: Leadership, Communication"
  ],
  "improvement_areas": [
    "Add 3-5 quantified metrics to achievements",
    "Highlight cross-functional collaboration examples",
    "Address employment gaps with explanations"
  ],
  "red_flags": [
    "⚠️ CV lacks quantified achievements: Score 55%"
  ]
}
```

---

## 🔧 Technical Stack

| Component | Technology |
|-----------|-----------|
| **Frontend** | Streamlit |
| **Backend** | Python 3.10+ |
| **AI/ML** | Claude API (optional), Sentence Transformers |
| **Data** | Pandas, JSON |
| **Parsing** | pdfplumber, pypdf |
| **Matching** | scikit-learn (cosine similarity) |
| **Visualization** | Plotly |

---

## 💡 How It Works

### 1. Company Profile Vector
```
Mission: "Democratize AI"
Vision: "Scale globally"
Values: ["Innovation", "Ownership", "Collaboration"]
          ↓
Creates culture profile with semantic embeddings
Innovation → Keywords: create, build, ideas, new, future
Ownership → Keywords: responsible, accountability, own
```

### 2. Candidate Soft Skills Extraction
```
CV: "Led team of 5 engineers. Built ML system from scratch. 
     Mentored juniors. Published on Medium."
          ↓
Claude API (or mock) extracts:
- Leadership: confidence 0.9 (evidence: "Led team of 5")
- Problem-solving: confidence 0.85 (evidence: "Built from scratch")
- Learning mindset: confidence 0.8 (evidence: "Published")
```

### 3. Matching Algorithm
```
Company requires: Leadership (weight: 0.9)
Candidate has:   Leadership (confidence: 0.9)
          ↓
Match score = 0.9 × 0.9 × 100 = 81%

For all soft skills → Average → Soft Skills Score
Combined with technical/culture/cv_quality → Overall Score
```

### 4. Feedback Generation
```
If overall < 60:
- What's missing? → Identify gaps
- Why matters? → Explain business impact
- How to improve? → Specific, actionable steps
- Red flags? → Context + interview questions
```

---

## 📈 Example Output

### High Match (Alice): 85% 🟢
```
✅ STRONG FIT
Alice Johnson is a strong cultural and technical fit. 
Recommend for interview.

MATCH BREAKDOWN:
- Technical: 90% ✅ (Strong ML/Python background)
- Soft Skills: 78% ✅ (Leadership, Communication)
- Culture: 85% ✅ (Mentorship, Innovation passion)
- CV Quality: 75% ✅ (Good structure, metrics present)

WHY MATCHED:
✅ Strong technical foundation: Python 90%, ML 85%, AWS 80%
✅ Demonstrated soft skills align: Leadership (led 5), Communication (published)
✅ Unique strengths: "Mentorship experience"

RED FLAGS:
None detected

RECOMMENDATIONS:
🟢 Schedule technical interview
🟢 Conduct culture fit discussion
💡 Fast-track to hiring manager
```

### Medium Match (Bob): 45% 🟡
```
⚠️ CONDITIONAL MATCH
Bob Martinez has good technical skills but requires soft skills assessment.

MATCH BREAKDOWN:
- Technical: 75% ✅ (React, Node.js good)
- Soft Skills: 35% ❌ (Limited evidence)
- Culture: 40% ⚠️ (Unclear fit)
- CV Quality: 55% ⚠️ (Lacks metrics)

WHY NOT MATCHED:
❌ Critical soft skill gap: Leadership not demonstrated (Company priority: 90%)
❌ CV quality issues: Lacks quantified achievements

TOP IMPROVEMENT AREAS:
1. Soft Skills Development (CRITICAL)
   Current: 35% → Target: 75%
   Actions:
   - Highlight leadership experiences or volunteer leadership roles
   - Demonstrate problem-solving with specific examples
   - Show evidence of learning from failures

2. CV Optimization (MEDIUM)
   Current: 55% → Target: 80%
   Actions:
   - Change "Maintained codebase" → "Refactored 50K lines, improved performance 20%"
   - Add business impact: "Reduced load time from 3s to 1.2s (60% improvement)"
   - Be specific: Show user impact, metrics

RED FLAGS:
🔴 Job Hopping: 5 jobs in 3 years (~1.7 jobs/year)
   Impact: "May indicate instability"
   Interview Q: "Can you walk me through your career transitions?"

RECOMMENDATIONS:
⚠️ Technical assessment needed
⚠️ Culture fit deep dive recommended
💡 Consider for slightly different role
```

### Low Match (David): 25% 🔴
```
❌ DOES NOT MATCH
David Chen does not meet current role requirements. 
Recommend for skills development.

CRITICAL ISSUES:
1. Limited formal technical background
2. No demonstrated soft leadership skills required by company
3. CV lacks structure and quantified achievements
4. Significant gap in Python/ML expertise (required: 80%, has: ~30%)

STRENGTH:
✅ Entrepreneurial experience - started/sold company
✅ Communication skills demonstrated in sales

RECOMMENDATIONS FOR DAVID:
🟡 ALTERNATIVE PATH: Consider for Business Development role
🟡 SKILLS PROGRAM: Recommend Python + ML online courses
🟡 REVISIT: In 6 months after skill development
💡 IDEA: Excellent candidate for Founder/PM track if technical co-founder role available

INTERVIEW QUESTIONS (if interviewing):
🎯 "Tell me about your company and what you learned?"
🎯 "What's your approach to learning new technical skills?"
🎯 "Can you describe your most complex technical problem?"
```

---

## 📹 Demo Video Outline (60 seconds)

```
[0-5s]   "SkillSense: AI-powered talent matching"
         Show: Tinder-like card interface

[5-15s]  "Setup your company once"
         Show: Company profile form with mission/values

[15-30s] "Upload CVs, get instant matches"
         Show: Upload 5 CVs → Processing animation

[30-45s] "See detailed feedback for each candidate"
         Swipe through 3 cards:
         • Green (90%): "Strong technical + culture fit"
         • Yellow (45%): "Good skills, soft skills gap"
         • Red (25%): "Lacks required expertise"
         
[45-55s] "Understand why and how to improve"
         Show: Detailed feedback screen
         "Get actionable feedback → Helps everyone improve"

[55-60s] "Ready to hire smarter? Try SkillSense"
         CTA: "Get matched with your perfect team"
```

---

## 🎯 Metrics & Success Indicators

**What makes SkillSense win:**

| Metric | Target | Why |
|--------|--------|-----|
| **Feedback Clarity** | 95%+ actionable | Candidates/recruiters know next steps |
| **Soft Skills Accuracy** | 85%+ match | Core differentiator from competitors |
| **Red Flag Detection** | 90%+ coverage | Helps avoid bad hires |
| **Matching Precision** | 80%+ accuracy | Reduces false positives |
| **User Satisfaction** | 4.5/5 stars | Easy to use, helpful feedback |

---

## 🔐 Privacy & Compliance

- **Data handling**: All CV data processed locally (no external storage by default)
- **GDPR ready**: Can delete candidate data on request
- **Transparency**: Clear disclosure of how data is used
- **No data selling**: Company data never shared or sold

---

## 🚀 Deployment Options

### Local Development
```bash
streamlit run skillsense_main.py
```

### Streamlit Cloud (Free)
```bash
# Push to GitHub
# Connect Streamlit Cloud
# Auto-deploys on push
```

### Docker (Production)
```bash
docker build -t skillsense .
docker run -p 8501:8501 skillsense
```

---

## 📝 One-Liner Value Prop

**"SkillSense matches candidates to companies based on skills AND culture, then provides actionable feedback explaining every decision—helping both recruiters find the right fit and candidates know how to improve."**

---

## 👥 Team

Built by: [Your Team Names]  
For: Hack-Nation Global AI Hackathon 2025  
Track: SAP Challenge - SkillSense  

---

## 📞 Support & Questions

- **Discord**: [Hackathon Discord]
- **GitHub Issues**: Create an issue
- **Mentors**: Book a slot at [Mentor Calendar]

---

## 📄 License

MIT License - Use freely for learning and commercial purposes

---

**Ready to revolutionize hiring? Let's match people to their perfect opportunities.** 🚀
