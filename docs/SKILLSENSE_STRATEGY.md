# 🎯 SKILLSENSE - ESTRATEGIA GANADORA

## DIFERENCIADORES CLAVE

### 1️⃣ FEEDBACK ESTRUCTURADO POR RECHAZO
En lugar de "No match", el sistema da:
- **Por qué no matcheo**
- **Cómo mejorar específicamente**
- **Red flags detectadas** (con contexto)

**Ejemplo de feedback:**
```
❌ MATCH: 35% (Low)

Razones del rechazo:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. ⚠️ RED FLAG: Job Stability
   • 5 trabajos en 1 año (promedio 2.4 meses/job)
   • Causas posibles: sector volatile, búsqueda activa, despidos
   • Recomendación: Contactar para entender contexto

2. 🔴 Habilidad Crítica Faltante: Leadership
   • Empresa busca: "Proven leader managing teams"
   • CV muestra: Individual contributor roles
   • GAP: Leadership experience
   • Sugerencia: Buscar candidatos con "Managed X team"

3. 📄 CV Estructura Débil
   • Falta: Impacto cuantificable en logros
   • Mejora: Cambiar "Responsable de reporting"
                → "Implementé dashboard, 30% faster reports"
   • Detectado: Vago, sin métricas

4. 💡 Misalign Cultural
   • Empresa: "Ágil, innovación, startup mindset"
   • CV indica: Estructurado, corporativo, estable
   • GAP: Valores fundamentales

Puntuación Desglosada:
├─ Technical Match:        75% ✅
├─ Leadership Match:       25% ❌ (CRÍTICO)
├─ Cultural Alignment:     40% ⚠️
├─ CV Quality:            55% ⚠️
└─ Risk Factors:          35% 🚨

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 INSIGHT: "Buen técnico, pero no es líder. Considerar para IC roles."
```

---

### 2️⃣ SOFT SKILLS MATCHING (EMPRESA ↔ CV)

**Mapeo semántico profundo:**

```
EMPRESA "TechStarup XYZ" dice:
┌─────────────────────────────────┐
│ Misión: Democratizar IA         │
│ Visión: Escala global           │
│ Valores:                        │
│ • Curiosidad e innovación       │
│ • Ownership y accountability    │
│ • Colaboración inclusiva        │
│ • Humildad y aprendizaje        │
│                                 │
│ Soft Skills buscados:           │
│ • Communication (Crítico)       │
│ • Problem-solving (Alto)        │
│ • Adaptability (Alto)           │
│ • Leadership by example (Medio) │
└─────────────────────────────────┘

EXTRACTOR AI ANALIZA CV:
┌─────────────────────────────────┐
│ "Led cross-functional team"     │
│  → Leadership ✅ (Strong)       │
│                                 │
│ "Navigated COVID disruption"    │
│  → Adaptability ✅ (Strong)     │
│                                 │
│ "Presented quarterly reviews"   │
│  → Communication ✅ (Medium)    │
│                                 │
│ "Struggled with deadlines"      │
│  → Reliability ❌ (Weak)        │
│                                 │
│ "Self-taught Python in 3 months"│
│  → Learning mindset ✅ (Strong) │
└─────────────────────────────────┘

MATCHING RESULT:
┌─────────────────────────────────┐
│ Soft Skills Alignment: 78%      │
│                                 │
│ ✅ Match:                       │
│ • Learning mindset             │
│ • Leadership by example        │
│ • Adaptability                 │
│                                 │
│ ⚠️  Partial:                   │
│ • Communication (Medium needed) │
│                                 │
│ ❌ Mismatch:                   │
│ • Reliability/Accountability   │
│   (Red flag: missed deadlines) │
└─────────────────────────────────┘
```

---

## ARQUITECTURA TÉCNICA DETALLADA

### COMPONENTES CORE

```
┌────────────────────────────────────────────────────────────┐
│           SKILLSENSE INTELLIGENT MATCHER                   │
└────────────────────────────────────────────────────────────┘

╔═══════════════════════════════════════════════════════════╗
║  LAYER 1: COMPANY PROFILING                              ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Input: Mission, Vision, Values, Soft Skills Required    ║
║                                                           ║
║  Processing:                                             ║
║  • Vectorize company culture (Claude embedding)          ║
║  • Extract soft skills taxonomy                          ║
║  • Weight soft skills by criticality                     ║
║  • Create "ideal candidate persona"                      ║
║                                                           ║
║  Output: Company Profile Vector + Rubric                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  LAYER 2: CV PARSING & EXTRACTION                        ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Input: PDF/TXT CV                                       ║
║                                                           ║
║  Step 1: Structure Extraction                            ║
║  • Name, contact, degree                                 ║
║  • Experience timeline (dates, companies, roles)         ║
║  • Skills explicit (listed section)                      ║
║                                                           ║
║  Step 2: Quality Assessment                              ║
║  • Format score (clarity, organization)                  ║
║  • Quantification score (metrics present?)               ║
║  • Coherence check (timeline gaps, job stability)        ║
║                                                           ║
║  Step 3: Implicit Skill Extraction (Claude API)          ║
║  • Read job descriptions → infer technical skills        ║
║  • Analyze achievements → extract soft skills            ║
║  • Detect red flags (gaps, job hopping, etc)            ║
║                                                           ║
║  Output: Candidate Profile (structured JSON)             ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  LAYER 3: SOFT SKILLS SEMANTIC MATCHING                  ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Input:                                                  ║
║  • Company soft skills taxonomy (weighted)               ║
║  • Candidate soft skills detected (with evidence)        ║
║                                                           ║
║  Algorithm:                                              ║
║  1. Vectorize each soft skill mentioned in CV            ║
║  2. Compare with company requirements                    ║
║  3. Weight by:                                           ║
║     - Importance to company                              ║
║     - Evidence strength in CV                            ║
║     - Criticality for role                               ║
║  4. Calculate alignment score                            ║
║                                                           ║
║  Output: Soft Skills Match Matrix                        ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  LAYER 4: RED FLAG DETECTION                             ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Detects:                                                ║
║  • Job Stability: # jobs / years (flag if > 1.5/year)   ║
║  • Experience Gaps: > 6 months unexplained              ║
║  • Skill Decay: Old tech, no updates                    ║
║  • Resume Quality: Vague descriptions, no metrics        ║
║  • Overqualification: Roles waaaay below seniority      ║
║  • Underqualification: Too junior for role              ║
║  • Mismatch Type: "Developer → Designer → PM"           ║
║                                                           ║
║  Output: Red Flags List (severity: 🔴❌⚠️✅)            ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  LAYER 5: INTELLIGENT FEEDBACK GENERATION                ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Generates for EACH candidate:                           ║
║                                                           ║
║  A. MATCH SCORE (Visual: 🟢 / 🟡 / 🔴)                 ║
║     - Overall %                                          ║
║     - Technical match                                    ║
║     - Soft skills alignment                              ║
║     - Cultural fit                                       ║
║                                                           ║
║  B. STRUCTURED FEEDBACK (Why no match?)                  ║
║     For each mismatch:                                   ║
║     • What's the gap?                                    ║
║     • Why it matters for company?                        ║
║     • How can candidate improve?                         ║
║                                                           ║
║  C. RED FLAG ANALYSIS (Risk assessment)                  ║
║     • What flags detected?                               ║
║     • Severity level                                     ║
║     • Questions to ask in interview                      ║
║                                                           ║
║  D. PERSONALIZED RECOMMENDATIONS                         ║
║     • "Consider for..." role suggestions                 ║
║     • "Improve CV by..."                                 ║
║     • "Strong in X, develop Y"                           ║
║                                                           ║
║  Output: Feedback Report (readable + actionable)         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

╔═══════════════════════════════════════════════════════════╗
║  LAYER 6: UI/UX - TINDER-LIKE INTERFACE                 ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Card View:                                              ║
║  ┌──────────────────────────────┐                        ║
║  │ 📷 Name | Match: 85% 🟢      │                        ║
║  │─────────────────────────────  │                        ║
║  │ Role sought: Senior Dev      │                        ║
║  │                              │                        ║
║  │ Most Valuable:               │                        ║
║  │ → "Leadership + Deep Tech"   │                        ║
║  │                              │                        ║
║  │ Quick Stats:                 │                        ║
║  │ • Technical: 90% ✅          │                        ║
║  │ • Soft Skills: 78% ✅        │                        ║
║  │ • Culture Fit: 85% ✅        │                        ║
║  │ • Red Flags: ⚠️ 1 minor     │                        ║
║  │                              │                        ║
║  │ [📧 Contact] [👉 Details]   │                        ║
║  └──────────────────────────────┘                        ║
║                                                           ║
║  Details View:                                           ║
║  • Full feedback breakdown                               ║
║  • Why matched / rejected                                ║
║  • Soft skills radar chart                               ║
║  • Red flags with context                                ║
║  • Action items (hire/interview/skip)                    ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## FLUJO DE PROMPTS CLAUDE (CORE LOGIC)

### PROMPT 1: Soft Skills Extraction from CV

```
You are an expert HR consultant analyzing CVs for skill assessment.

Given this CV section:
{cv_section}

Extract the following soft skills with evidence and confidence:
1. Leadership (evidence: specific example from CV)
2. Communication (evidence: ...)
3. Adaptability (evidence: ...)
4. Problem-solving (evidence: ...)
5. Collaboration (evidence: ...)
6. Work ethic / Reliability (evidence: ...)
7. Learning mindset (evidence: ...)

For each skill:
- Confidence: High/Medium/Low
- Evidence: Quote from CV
- Interpretation: What does this say about the candidate?

Return as JSON:
{
  "soft_skills": [
    {
      "skill": "Leadership",
      "confidence": "High",
      "evidence": "Led team of 5 engineers...",
      "interpretation": "Shows hands-on technical leadership"
    }
  ]
}
```

### PROMPT 2: Red Flag Detection

```
Analyze this CV for red flags and concerns:

CV Info:
- Years in workforce: {years}
- Job history: {jobs}
- Skills progression: {skills_timeline}
- Experience gaps: {gaps}

Detect these red flags:
1. Job Hopping (> 1.5 jobs/year)
2. Experience Gaps (> 6 months)
3. Skill Relevance (outdated tech, no growth)
4. Resume Quality (vague, no metrics)
5. Role Coherence (random job changes)
6. Overqualification / Underqualification

For each red flag found:
- Name
- Severity: 🔴 Critical / ❌ Major / ⚠️ Minor / ✅ None
- Evidence
- Context needed
- Interview question suggestion

Return as JSON.
```

### PROMPT 3: Soft Skills ↔ Company Values Matching

```
Company Profile:
- Mission: {mission}
- Values: {values}
- Soft Skills Required (weighted):
  {
    "Leadership": 0.9 (Critical),
    "Communication": 0.8 (High),
    "Adaptability": 0.7 (Medium),
    ...
  }

Candidate Soft Skills Profile:
{candidate_skills}

Match each company soft skill requirement with candidate's demonstrated skills:

For each required skill:
1. Is it present in candidate? Yes/No/Partial
2. Strength of evidence: High/Medium/Low
3. Gap analysis: What's missing?
4. Improvement suggestion: How can candidate develop this?

Return:
{
  "matches": [
    {
      "company_skill": "Leadership",
      "candidate_has": "Yes",
      "strength": "High",
      "evidence": "...",
      "gap": "None",
      "alignment_score": 0.9
    }
  ],
  "overall_soft_skills_match": 0.78,
  "cultural_alignment": 0.85
}
```

### PROMPT 4: Feedback Generation (Why No Match?)

```
Generate personalized feedback for candidate {name}:

Match Details:
- Overall: 35%
- Technical: 75%
- Soft Skills: 40%
- Culture Fit: 30%

Rejection Reasons:
{rejection_reasons}

Create structured feedback that:
1. Explains why they didn't match (specific, not generic)
2. Identifies critical gaps
3. Provides actionable improvement suggestions
4. Acknowledges their strengths
5. Suggests alternative roles/companies

Format as readable report with:
- Executive summary (1 line)
- Detailed breakdown (bullet points)
- Top 3 improvement areas
- "Consider for:" suggestions
- Encouragement + next steps
```

---

## FLUJO DE 24 HORAS (REFINED)

```
00:00 - 01:00  Setup + Architecture (DONE: env ready)
01:00 - 03:00  Company Profile Builder (DONE: form + storage)
03:00 - 05:00  CV Parser (DONE: extract structure)
05:00 - 08:00  Soft Skills Extraction (DONE: Claude integration)
08:00 - 10:00  Red Flag Detection (DONE: algorithm)
10:00 - 12:00  Matching Algorithm (DONE: scoring logic)
12:00 - 14:00  Feedback Generator (DONE: LLM prompts)
14:00 - 16:00  UI/Tinder Cards (DONE: Streamlit)
16:00 - 18:00  Testing + Polish (DONE: all features working)
18:00 - 20:00  Demo + Videos (DONE: 2 vids recorded)
20:00 - 22:00  One-Pager + Docs (DONE: submission ready)
22:00 - 24:00  Buffer + Final checks (DONE: submit)
```

---

## EVALUACIÓN vs RUBRICA

### Profundidad Técnica (33%)
✅ Multi-layer NLP (parsing + extraction + semantic matching)
✅ Advanced algorithms (red flag detection, soft skills matching)
✅ Claude API integration (reasoning, feedback generation)
✅ Structured data processing (JSON, vectorization)

### Creatividad e Innovación (33%)
✅ **Tinder-like UX** (different from typical HR tools)
✅ **Feedback for rejection** (unique: helps candidates improve)
✅ **Soft skills ↔ values matching** (novel semantic approach)
✅ **Red flag detection** (proactive risk assessment)
✅ **Actionable insights** (not just scores)

### Comunicación (33%)
✅ **Clear feedback** (explains why, not just score)
✅ **Structured reports** (easy to understand)
✅ **Visual indicators** (🟢🟡🔴 semaphore)
✅ **Compelling story** ("AI Career Coach for candidates + HR Intelligence for companies")
✅ **Demo video** (see the tool in action - intuitive)

---

## DIFERENCIADORES vs COMPETENCIA

| Aspecto | Typical HR Tools | SkillSense |
|---------|-----------------|-----------|
| Match Score | ✓ Generic % | ✓ Multi-layer breakdown |
| Feedback | ✗ None | ✓ Structured, actionable |
| Soft Skills | ✗ Ignored | ✓ Deep semantic matching |
| Red Flags | ✗ Not detected | ✓ Automated detection |
| Culture Fit | ✗ Not evaluated | ✓ Values alignment |
| UX | ✓ Dashboard | ✓ **Tinder-like** |
| Candidate Help | ✗ Rejected quietly | ✓ Improvement suggestions |

