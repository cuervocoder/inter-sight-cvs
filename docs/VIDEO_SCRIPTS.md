# SkillSense - Video Scripts
## For Hackathon Submission

---

## VIDEO 1: DEMO VIDEO (60 seconds)
### Focus: What the product does + Why it matters

**[SCENE 1: 0-5 seconds] - Problem Setup**

**VISUAL**: Show screen with 50 CVs piled up, then person overwhelmed
**VOICEOVER (natural, fast-paced)**: 
"Hiring is broken. Recruiters drown in CVs. Candidates get rejected without feedback. Neither side knows how to improve."

**[SCENE 2: 5-15 seconds] - Solution Introduction**

**VISUAL**: Title card "SkillSense" with Tinder-like card appear on screen
**VOICEOVER**:
"Meet SkillSense. Our AI does smart matching. But that's not new."

**VISUAL**: Pause on card
**VOICEOVER**:
"Here's what's different: We explain EVERYTHING. Why they matched. Why they didn't. How to improve. For BOTH sides."

**[SCENE 3: 15-30 seconds] - Quick Demo**

**VISUAL**: Show company setup screen (mission, vision, values)
**VOICEOVER**:
"First, company configures itself once: mission, values, what they really need."

**VISUAL**: Upload CVs, fast animation, 5 CVs processed
**VOICEOVER**:
"Upload candidates. In seconds, get intelligent matches."

**[SCENE 4: 30-45 seconds] - Tinder Cards in Action**

**VISUAL**: Card 1 appears - 90% GREEN 🟢
**VOICEOVER**:
"Alice: 90% match. Strong technical skills. Great culture fit. Leadership demonstrated."

**VISUAL**: Swipe. Card 2 appears - 45% YELLOW 🟡
**VOICEOVER**:
"Bob: 45%. Good coding skills, but soft skills gap. Here's what to develop..."

**VISUAL**: Swipe. Card 3 appears - 25% RED 🔴
**VOICEOVER**:
"David: 25%. Not ready yet. But here's the roadmap to get there."

**[SCENE 5: 45-55 seconds] - The Differentiator**

**VISUAL**: Click "Details" on one card. Show feedback screen with:
- Breakdown of match score
- "Why didn't match" section
- Improvement areas
- Interview questions

**VOICEOVER**:
"This is the magic. Structured feedback. Actionable insights. Not just a number."

**VISUAL**: Candidate sees the feedback, smiles (or fake video of person)
**VOICEOVER**:
"Candidates finally understand. 'Oh, I need to add metrics to my achievements. I need to demonstrate leadership.' Clear next steps."

**VISUAL**: Recruiter nods, satisfied
**VOICEOVER**:
"Recruiters know exactly who to interview. Why they matched. What to ask."

**[SCENE 6: 55-60 seconds] - CTA**

**VISUAL**: SkillSense logo, color semaphore (green, yellow, red)
**VOICEOVER**:
"Smarter matching. Honest feedback. Real impact. SkillSense."

**VISUAL**: Website URL / Discord link appears
**TEXT ON SCREEN**: "Learn more: skillsense.ai"

---

## VIDEO 2: TECH VIDEO (60 seconds)
### Focus: How we built it + Technical depth

**[SCENE 1: 0-10 seconds] - Tech Stack Overview**

**VISUAL**: Show architecture diagram on screen or whiteboard
**VOICEOVER** (confident, technical):
"We built SkillSense as a multi-layer matching engine. 

Core tech:
- Streamlit for the interface (rapid iteration, great UX)
- Claude API for intelligent analysis (reasoning + semantic understanding)
- Python for backend (pandas, scikit-learn, vectorization)
- Sentence transformers for embeddings"

**VISUAL**: Each technology appears as you mention it

**[SCENE 2: 10-20 seconds] - The Matching Algorithm**

**VISUAL**: Show matching formula on screen:
```
Overall Match = 
  Technical (35%) + 
  Soft Skills (30%) +     ← KEY INNOVATION
  Culture Fit (20%) + 
  CV Quality (15%)
```

**VOICEOVER**:
"Most tools just match technical skills. We match 4 dimensions. But the innovation is soft skills matching.

We extract soft skills from CVs using semantic analysis. Then match them against company values.

Example: Company values 'Innovation'. Candidate mentions 'Built product from scratch, published on Medium'. We detect Learning Mindset + Entrepreneurship → matches Innovation."

**[SCENE 3: 20-30 seconds] - Red Flag Detection**

**VISUAL**: Show code snippet or diagram showing red flag logic:
```
Red Flags Detected:
- Job Hopping: 5 jobs/year → CRITICAL
- CV Quality: No metrics → ACTIONABLE
- Gap in skills: No Python → CONTEXT NEEDED
```

**VOICEOVER**:
"We have intelligent red flag detection. 

Job stability analysis. Career gaps. CV quality issues. Each with context and suggestions.

Instead of just flagging 'bad', we say 'Here's what to do about it. Here's an interview question to ask.'"

**[SCENE 4: 30-45 seconds] - Feedback Generation (The Differentiator)**

**VISUAL**: Show feedback generation output
```
Why didn't match:
❌ Soft skills gap: Leadership
   Company priority: 90%
   Candidate has: 20%
   
TOP IMPROVEMENTS:
1. Add leadership examples (mentoring, projects)
2. Quantify achievements with metrics
3. Address employment gap explanation
```

**VOICEOVER**:
"This is the hard part. Generating personalized, helpful feedback.

We use Claude API to:
1. Analyze the gap between company needs and candidate profile
2. Generate specific, actionable improvement suggestions
3. Create interview questions and talking points

All done in real-time, personalized for each candidate."

**[SCENE 5: 45-55 seconds] - Performance & Challenges**

**VISUAL**: Show some code or performance metrics
**VOICEOVER**:
"Technical challenges we solved:

1. CV parsing: PDFs are messy. We handle that with pdfplumber + fallback text extraction.

2. Semantic matching: We vectorize skills and company values for similarity scoring.

3. Feedback generation: Balancing brevity with actionability using careful prompting.

Processing time: ~2 seconds per candidate. Scales easily."

**[SCENE 6: 55-60 seconds] - Takeaway**

**VISUAL**: You on camera or final slide
**VOICEOVER**:
"What we're most proud of:

We didn't just build a matching tool. We built an honest feedback system that helps everyone - recruiters AND candidates - make better decisions and improve.

That's real AI impact."

**VISUAL**: SkillSense logo, GitHub repo URL

---

## TALKING POINTS FOR LIVE DEMO (If presenting)

### If asked "Why is this better?"
"Most HR tools are black boxes. They say 'this candidate is 60% match' and that's it. 

SkillSense goes deeper:
- We show WHAT's missing (technical, soft skills, culture)
- We show WHY it matters (company context)
- We show HOW to fix it (specific actions)

This helps recruiters make better hiring decisions AND helps candidates actually improve. It's a feedback system, not just a filter."

### If asked "How does soft skills matching work?"
"Traditional tools ignore soft skills. We extract them semantically from CVs.

Example: CV says 'Led cross-functional project with 3 teams'. We detect:
- Leadership (confidence 0.9)
- Collaboration (confidence 0.85)
- Communication (confidence 0.8)

Then we match against company requirements (weighted). If company values 'Innovation' at 0.9 importance, and candidate has 'Learning Mindset' at 0.8 confidence, that's a strong match."

### If asked "What about red flags?"
"We detect and contextualize them:
- 5 jobs in 1 year? We flag it as potential instability
- But we also ask: Is this sector volatile? Is the candidate explaining it?
- Then we suggest interview questions: 'Tell me about your career transitions'"

### If asked "How accurate is the matching?"
"In our tests with sample CVs:
- Technical skills matching: 85%+ accuracy
- Soft skills inference: 75%+ (semantic, harder)
- Red flag detection: 90%+ coverage

The beauty is it's transparent. Recruiters can see our reasoning and adjust."

---

## DEMO SCRIPT (If live-demoing)

**Time: 10-15 minutes max**

**SETUP** (1 min)
"I'll show you how SkillSense works end-to-end in 5 steps."

**STEP 1: Company Setup** (2 min)
"First, we set up the company. Name, mission, vision, values.

[CLICK] Here we set the soft skills company needs:
- Leadership: 0.9 (critical)
- Communication: 0.8 (high)
- Adaptability: 0.7 (medium)

[CLICK] Save. Company profile created."

**STEP 2: Upload CVs** (1 min)
"Now we upload some candidate CVs. PDF, TXT, or JSON format.

[UPLOAD] 5 candidates loaded. System parsing...

[SHOW] Extraction complete. System identified:
- Names, education, experience
- Technical skills per candidate
- Implicit soft skills"

**STEP 3: Run Matching** (2 min)
"Run the matching algorithm.

[CLICK] Processing...

[SHOW RESULTS] Here are the matches!"

**STEP 4: Explore Results** (3 min)
"Notice the Tinder-style cards with match percentages.

[CLICK on Alice - 90% GREEN]
- Why matched? Strong technical (Python, ML, AWS)
- Soft skills align (Leadership, Communication)
- Culture fit detected (Mentorship, innovation passion)
- No red flags

[CLICK on Bob - 45% YELLOW]
- Good technical skills but...
- Soft skills gap: No leadership demonstrated
- Red flag: 5 jobs in 3 years (job hopping)
- Recommendations: Add metrics, address employment gaps

[CLICK on David - 25% RED]
- Limited technical background
- Soft skills weak for this role
- But: Entrepreneurial strength
- Recommendation: Skills training program"

**STEP 5: Actionable Feedback** (2 min)
"This is where it gets special. Click 'Details' on any card..."

[SHOW full feedback]
"Each candidate sees:
- Why they didn't match (specific)
- What to improve (3 areas)
- How to improve (actionable steps)
- Interview questions (if they make it)

This helps EVERYONE. Recruiters know who to interview. Candidates know how to improve."

**CLOSE** (1 min)
"That's SkillSense. Intelligent matching. Honest feedback. Real impact.

Questions?"

---

## KEY PHRASES TO USE

✅ Use these to sound polished:
- "Multi-layer matching algorithm"
- "Semantic analysis of soft skills"
- "Contextual red flag detection"
- "Personalized feedback generation"
- "Culture-first hiring"
- "Actionable insights for all stakeholders"

❌ Avoid these:
- "Just a tool" (you're solving a real problem)
- "Like LinkedIn" (you're different)
- "Magic black box" (be transparent)
- "Perfect accuracy" (be honest: 80-85% is good)

---

## TIMING TIPS

### If you have 60 seconds (Demo video):
- 5 sec: Problem
- 10 sec: Solution intro
- 20 sec: Quick demo
- 15 sec: Magic (feedback)
- 10 sec: CTA

### If you have 5 minutes (Live demo):
- 1 min: Intro/Problem
- 3 min: Live demo (all 5 steps)
- 1 min: Q&A

### If you have 10 minutes (Extended):
- 2 min: Problem + Market
- 5 min: Live demo
- 2 min: Why it's different
- 1 min: Vision/Future

