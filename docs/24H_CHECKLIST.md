# SkillSense - 24 Hour Hackathon Execution Checklist

**START TIME**: [Your start time]  
**END TIME**: [+24 hours]  
**SUBMISSION DEADLINE**: 9:00 AM ET Nov 9  

---

## 🎯 PHASE 0: SETUP (Hour 0 - 1)

### Environment Setup
- [ ] Clone/setup repo structure
- [ ] Create Python virtual environment: `python -m venv venv`
- [ ] Activate: `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows)
- [ ] Install requirements: `pip install -r requirements.txt`
- [ ] Test Streamlit: `streamlit hello` (should work)
- [ ] Create `.env` file for API keys (if needed)
- [ ] Set up GitHub repo (for submission)

### Team Coordination
- [ ] Assign roles:
  - Backend lead: Core algorithms
  - Frontend lead: Streamlit UI
  - Demo lead: Videos + presentation
  - QA lead: Testing + polish
- [ ] Set up communication channel (Discord/Slack)
- [ ] Review submission requirements (rules PDF)
- [ ] Bookmark resources:
  - [ ] Hackathon portal
  - [ ] Mentor calendar
  - [ ] Discord channel
  - [ ] Submission links

---

## 🔧 PHASE 1: CORE DEVELOPMENT (Hour 1 - 10)

### Hour 1-2: Architecture & Setup
- [ ] Review SKILLSENSE_STRATEGY.md
- [ ] Set up project structure:
  ```
  skillsense/
  ├── skillsense_main.py
  ├── company_profiler.py
  ├── cv_parser.py
  ├── skill_extractor.py
  ├── red_flag_detector.py
  ├── matcher.py
  ├── feedback_generator.py
  ├── requirements.txt
  ├── sample_candidates.json
  ├── README.md
  └── data/
      └── sample_cvs/
  ```
- [ ] Confirm all modules created
- [ ] Test imports: `python -c "import streamlit; print('OK')"`

### Hour 2-4: Backend Core Logic
- [ ] **company_profiler.py**: ✅ Already created
  - [ ] Test: Create sample company profile
  - [ ] Verify JSON output
- [ ] **cv_parser.py**: ✅ Already created
  - [ ] Test: Parse sample CVs
  - [ ] Handle PDF/TXT/JSON formats
  - [ ] Extract: name, education, experience, skills
- [ ] **skill_extractor.py**: ✅ Already created
  - [ ] Test with mock data
  - [ ] Verify soft skills extraction
  - [ ] Check confidence scoring

### Hour 4-7: Advanced Algorithms
- [ ] **red_flag_detector.py**: ✅ Already created
  - [ ] Test: Detect job hopping
  - [ ] Test: Detect gaps
  - [ ] Test: CV quality scoring
  - [ ] Verify severity classification
- [ ] **matcher.py**: ✅ Already created
  - [ ] Test: Calculate match scores
  - [ ] Verify weighting (35/30/20/15)
  - [ ] Test soft skills matching (THE KEY DIFFERENTIATOR)
  - [ ] Validate scores 0-100 range
- [ ] **feedback_generator.py**: ✅ Already created
  - [ ] Test: Generate feedback for high match (80%+)
  - [ ] Test: Generate feedback for low match (<50%)
  - [ ] Verify: Why matched + why not + improvements
  - [ ] Check: Red flag analysis

### Hour 7-10: Integration & Testing
- [ ] Create simple test script:
  ```python
  # test_flow.py
  from company_profiler import CompanyProfiler
  from cv_parser import CVParser
  from matcher import Matcher
  from feedback_generator import FeedbackGenerator
  
  # Load sample company
  # Load sample CVs
  # Run matching
  # Generate feedback
  # Verify output
  ```
- [ ] Test end-to-end flow with sample_candidates.json
- [ ] Fix any bugs/issues
- [ ] Verify all imports work

---

## 🎨 PHASE 2: UI/STREAMLIT (Hour 10 - 16)

### Hour 10-12: Main App Structure
- [ ] **skillsense_main.py**: ✅ Already created
- [ ] Test: `streamlit run skillsense_main.py`
- [ ] Verify tabs load:
  - [ ] Tab 1: Company Setup
  - [ ] Tab 2: Upload CVs
  - [ ] Tab 3: Match Candidates
  - [ ] Tab 4: Analytics
- [ ] Fix any rendering issues
- [ ] Test forms/inputs

### Hour 12-14: Tab 1 - Company Setup
- [ ] Form inputs (name, mission, vision, values)
- [ ] Sliders for soft skills weights
- [ ] "Save" button functionality
- [ ] Verify data persists in session state
- [ ] Display saved profile summary
- [ ] Style: Add CSS for card design

### Hour 14-16: Tabs 2-3 - Upload & Match
- [ ] **Tab 2 - Upload CVs**:
  - [ ] File uploader (PDF, TXT, JSON)
  - [ ] Process button
  - [ ] Progress bar
  - [ ] Display loaded candidates
- [ ] **Tab 3 - Match Candidates**:
  - [ ] "Run Matching" button
  - [ ] Progress updates
  - [ ] Display Tinder-style cards
  - [ ] Click to see details
  - [ ] Show feedback breakdown
  - [ ] Color coding (🟢🟡🔴)
  - [ ] Action buttons (Contact, Details, Skip)

### Hour 16: Tab 4 - Analytics
- [ ] Display metrics (total candidates, avg match, top match)
- [ ] Plotly bar chart (match distribution)
- [ ] Any additional insights

### Polish & Styling
- [ ] Add colors/emojis for visual appeal
- [ ] Test responsiveness (mobile + desktop)
- [ ] Fix any layout issues
- [ ] Test with sample data end-to-end

---

## 📹 PHASE 3: DEMO PREPARATION (Hour 16 - 19)

### Hour 16-17: Demo Video (60 sec)
Follow VIDEO_SCRIPTS.md - Demo Video section
- [ ] Write script (already provided)
- [ ] Record screen:
  - [ ] Tool: OBS Studio OR Zoom OR Loom
  - [ ] Setup: Share screen while narrating
  - [ ] Keep under 60 seconds
  - [ ] Include voiceover (clear, engaging)
- [ ] Structure:
  - [ ] 5 sec: Problem
  - [ ] 10 sec: Solution intro
  - [ ] 20 sec: Demo (cards, matching)
  - [ ] 15 sec: Feedback feature
  - [ ] 10 sec: CTA
- [ ] Add captions if possible (Loom auto-captions)
- [ ] Export video (MP4)
- [ ] Upload to Google Drive (public link)
- [ ] Store link for submission

### Hour 17-18: Tech Video (60 sec)
Follow VIDEO_SCRIPTS.md - Tech Video section
- [ ] Write script (already provided)
- [ ] Record screen:
  - [ ] Show code/architecture
  - [ ] Explain matching algorithm
  - [ ] Discuss red flag detection
  - [ ] Highlight feedback generation
  - [ ] Keep under 60 seconds
  - [ ] Speak like CTO giving update
- [ ] Structure:
  - [ ] 10 sec: Tech stack
  - [ ] 15 sec: Algorithm
  - [ ] 15 sec: Red flag detection
  - [ ] 12 sec: Feedback generation
  - [ ] 8 sec: Takeaway
- [ ] Export video (MP4)
- [ ] Upload to Google Drive (public link)
- [ ] Store link for submission

### Hour 18-19: Test Videos
- [ ] Download and watch both videos
- [ ] Check audio/video quality
- [ ] Ensure under 60 seconds each
- [ ] Verify Google Drive links work (open in incognito)
- [ ] Re-record if needed

---

## 📄 PHASE 4: DOCUMENTATION (Hour 19 - 22)

### Hour 19: One-Pager PDF
Use ONE_PAGER.md as template
- [ ] Copy template to new doc
- [ ] Fill in:
  - [ ] Challenge tackled
  - [ ] Tools/models used
  - [ ] What worked well
  - [ ] What was challenging
  - [ ] Time breakdown
  - [ ] Key innovation
  - [ ] Metrics
  - [ ] Future work
- [ ] Format:
  - [ ] Keep to 1 page maximum
  - [ ] Use headers, bullets
  - [ ] Add small diagrams if helpful (but keep brief)
  - [ ] White space for readability
- [ ] Export as PDF: `TeamName_OnePager.pdf`
- [ ] Save to outputs folder

### Hour 20: GitHub Repository
- [ ] Push all code to public GitHub repo
- [ ] Create comprehensive README.md:
  - [ ] What is SkillSense
  - [ ] Key differentiators (already in README.md)
  - [ ] Features
  - [ ] Quick start (how to run)
  - [ ] Data formats
  - [ ] Tech stack
  - [ ] How it works
  - [ ] Usage examples
  - [ ] Future work
- [ ] Create .gitignore:
  ```
  __pycache__/
  *.pyc
  .env
  .venv/
  venv/
  .streamlit/
  ```
- [ ] Verify repo is public
- [ ] Store GitHub URL for submission

### Hour 21: Code Organization & Comments
- [ ] Add docstrings to all functions
- [ ] Add inline comments explaining logic
- [ ] Ensure code is readable
- [ ] Example:
  ```python
  def match(self, company_profile: Dict, candidate: Dict) -> Dict:
      """
      Calculate match scores across multiple dimensions.
      
      Args:
          company_profile: Dict with mission, values, soft_skills_weights
          candidate: Dict with cv_data and extracted skills
          
      Returns:
          Dict with overall, technical, soft_skills, culture_fit scores
      """
  ```
- [ ] Add requirements.txt:
  - [ ] Already created ✅
  - [ ] Verify all packages listed
  - [ ] Test: `pip install -r requirements.txt` works

### Hour 22: Backup Files
- [ ] Create .zip file:
  ```
  skillsense_final.zip
  ├── skillsense_main.py
  ├── *.py (all modules)
  ├── requirements.txt
  ├── sample_candidates.json
  ├── README.md
  ├── ONE_PAGER.pdf
  └── data/
  ```
- [ ] Save to outputs folder
- [ ] Verify .zip extracts properly
- [ ] Test: Extract and `streamlit run skillsense_main.py` works

---

## 📋 PHASE 5: SUBMISSION (Hour 22 - 24)

### Hour 22: Prepare Submission Checklist
Review Submission Guide (Rules__Submission_guide_docx.pdf)

**Required Items**:
- [ ] Short description (150-300 words) - DRAFT COMPLETE
- [ ] Demo video (60 sec max) - RECORDED & TESTED
- [ ] Tech video (60 sec max) - RECORDED & TESTED
- [ ] 1-Page Report (PDF) - COMPLETE
- [ ] GitHub Repository (public) - PUSHED & VERIFIED
- [ ] Zipped code file (.zip) - CREATED & TESTED
- [ ] Dataset/links (if used) - DOCUMENTED

**Optional/Good to Have**:
- [ ] Architecture diagram
- [ ] Sample outputs
- [ ] Deployment instructions

### Hour 23: Fill Out Submission Forms

**Form 1: Official Platform (projects.hack-nation.ai)**
- [ ] Log in with provided code
- [ ] Select "Challenge 1: SkillSense"
- [ ] Fill in:
  - [ ] Team name
  - [ ] Team member names (all members MUST be listed)
  - [ ] Project title
  - [ ] Short description (150-300 words)
  - [ ] Links:
    - [ ] Demo video URL (Google Drive)
    - [ ] Tech video URL (Google Drive)
    - [ ] GitHub repo URL
    - [ ] 1-Pager PDF (Google Drive - PUBLIC)
    - [ ] Zipped code (Google Drive - PUBLIC)
    - [ ] Dataset link (if applicable)
- [ ] Save draft
- [ ] Review everything
- [ ] SUBMIT

**Form 2: Google Form Backup (tinyurl.com/HN-Submission)**
- [ ] Fill out identical information
- [ ] Include all links
- [ ] SUBMIT

### Hour 24: Final Verification

**30 min before deadline**:
- [ ] Download your submissions to verify
- [ ] Open each link (incognito window):
  - [ ] Demo video: Plays, correct duration
  - [ ] Tech video: Plays, correct duration
  - [ ] One-pager PDF: Opens, readable, complete
  - [ ] GitHub: Public, README visible, code complete
  - [ ] Zipped code: Extracts properly, can run `streamlit run skillsense_main.py`
- [ ] Verify team member names are correct
- [ ] Check description for typos/clarity

**5 min before deadline**:
- [ ] ✅ SUBMIT (if you haven't already)
- [ ] Take screenshot of confirmation
- [ ] Screenshot for proof

---

## ✅ QUALITY CHECKLIST

Before submitting, verify:

### Technical Quality (33%)
- [ ] Matching algorithm works correctly (tested with sample data)
- [ ] Soft skills matching is sophisticated (semantic, not just keyword)
- [ ] Red flag detection is intelligent (contextual, not just rules)
- [ ] Feedback generation is helpful (specific, actionable)
- [ ] Code is readable and well-documented
- [ ] No crashes or errors in happy path
- [ ] Performance acceptable (<5 sec per 10 candidates)

### Creativity & Innovation (33%)
- [ ] Soft skills ↔ values matching is unique
- [ ] Tinder-like UX is engaging and appropriate
- [ ] Feedback generation is novel (not just scores)
- [ ] Red flag analysis is thoughtful
- [ ] Use case scenarios are compelling
- [ ] Demo shows wow factor

### Communication (33%)
- [ ] Demo video is clear and engaging (60 sec)
- [ ] Tech video explains approach well (60 sec)
- [ ] One-pager is well-structured and readable
- [ ] README is comprehensive
- [ ] GitHub code is clean and commented
- [ ] Description is compelling and clear
- [ ] All links work (tested)

---

## 🎬 FINAL REMINDERS

⚠️ **CRITICAL**:
- [ ] **Make Google Drive links PUBLIC** (not just shared)
- [ ] **Include ALL team members in submission**
- [ ] **Use BOTH platforms** (website + Google Form)
- [ ] **Verify videos are <60 seconds**
- [ ] **Test all links before submitting**

💡 **TIPS**:
- Prioritize **one hero feature** (soft skills matching + feedback)
- Don't try to do everything - MVP with depth beats bloated feature set
- Make sure your **differentiator is CLEAR** in videos
- **Practice your story**: What makes this special?

🚀 **YOU'VE GOT THIS!**

---

## 📊 ESTIMATED TIME ALLOCATION

| Phase | Hours | Percentage |
|-------|-------|-----------|
| Setup | 1 | 4% |
| Backend Core | 6 | 25% |
| Algorithms | 3 | 13% |
| UI/Streamlit | 6 | 25% |
| Demo Prep | 3 | 13% |
| Documentation | 3 | 13% |
| Submission | 2 | 8% |
| **TOTAL** | **24** | **100%** |

---

## 🆘 TROUBLESHOOTING

**Issue**: Streamlit not starting
- [ ] Verify virtual env activated
- [ ] Run: `pip install streamlit`
- [ ] Try: `streamlit run --logger.level=debug skillsense_main.py`

**Issue**: Import errors
- [ ] Run: `pip install -r requirements.txt --upgrade`
- [ ] Check: All .py files in same directory

**Issue**: Video too long
- [ ] Use Loom: Built-in trimming
- [ ] Use OBS: Edit in post
- [ ] Re-record faster-paced

**Issue**: GitHub access
- [ ] Ensure repo is PUBLIC
- [ ] Test with incognito browser
- [ ] Share link to verify

**Issue**: Last-minute bugs
- [ ] Have 1 hour buffer
- [ ] Focus on happy path
- [ ] Polish > perfection

---

## 🎯 SUCCESS METRICS

You've succeeded if:
- ✅ App runs without crashing
- ✅ Matching algorithm produces sensible scores
- ✅ Feedback is clear and helpful
- ✅ Videos are engaging and clear
- ✅ All submissions are on time
- ✅ Demo shows clear wow factor (soft skills matching + feedback)

---

**Good luck! You're building something that actually helps people. That's real impact.** 🚀

