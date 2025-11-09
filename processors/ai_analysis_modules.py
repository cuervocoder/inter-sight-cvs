"""Skill Extractor - Intelligent skill detection using LLM"""

import json
import logging
from typing import Dict, List
from core.llm_provider import get_llm

logger = logging.getLogger(__name__)


class SkillExtractor:
    """Extract skills from CV using AI"""
    
    def __init__(self, llm_provider="mistral", api_key=None):
        try:
            self.llm = get_llm(llm_provider, api_key)
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            self.llm = None
    
    def extract_skills(self, cv_data: Dict) -> Dict:
        """
        Extract skills intelligently using AI
        
        Returns:
            {
                "technical_skills": [...],
                "soft_skills": [...],
                "skill_confidence": 0.85,
                "summary": "..."
            }
        """
        
        if not self.llm:
            return self._extract_skills_fallback(cv_data)
        
        try:
            # Prepare context
            cv_text = self._prepare_cv_text(cv_data)
            
            # Use AI to extract skills
            prompt = f"""Analyze this CV and extract ALL skills (both technical and soft).
Return a JSON with:
- technical_skills: list of tech skills found
- soft_skills: list of soft skills found
- evidence: why these skills are present
- confidence: 0-100 score of how clear the skills are

CV Content:
{cv_text}

Return ONLY valid JSON, no markdown."""
            
            response = self.llm.extract_json(prompt)
            
            return {
                "technical_skills": response.get("technical_skills", []),
                "soft_skills": response.get("soft_skills", []),
                "evidence": response.get("evidence", ""),
                "confidence": response.get("confidence", 0),
                "method": "ai"
            }
            
        except Exception as e:
            logger.error(f"Error extracting skills with AI: {e}")
            return self._extract_skills_fallback(cv_data)
    
    def _extract_skills_fallback(self, cv_data: Dict) -> Dict:
        """Fallback to basic extraction"""
        return {
            "technical_skills": cv_data.get("skills", []),
            "soft_skills": cv_data.get("soft_skills", []),
            "evidence": "Basic extraction",
            "confidence": 50,
            "method": "fallback"
        }
    
    def _prepare_cv_text(self, cv_data: Dict) -> str:
        """Prepare CV data as readable text"""
        text = f"""
Name: {cv_data.get('name', 'N/A')}
Degree: {cv_data.get('degree', 'N/A')}
University: {cv_data.get('university', 'N/A')}
Years Experience: {cv_data.get('years_experience', 0)}

Experience:
"""
        for exp in cv_data.get("experience", []):
            text += f"- {exp.get('role', 'N/A')}: {exp.get('description', 'N/A')}\n"
        
        text += f"\nCurrent Skills: {', '.join(cv_data.get('skills', []))}"
        
        return text


class CultureAnalyzer:
    """Analyze culture fit using AI"""
    
    def __init__(self, llm_provider="mistral", api_key=None):
        try:
            self.llm = get_llm(llm_provider, api_key)
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            self.llm = None
    
    def analyze_fit(self, cv_data: Dict, company_data: Dict) -> Dict:
        """
        Analyze how well candidate fits company culture
        
        Returns:
            {
                "culture_score": 75,
                "reasoning": "...",
                "alignments": [...],
                "gaps": [...]
            }
        """
        
        if not self.llm:
            return self._analyze_fit_fallback(cv_data, company_data)
        
        try:
            prompt = f"""Analyze culture fit between candidate and company.

Company Profile:
- Mission: {company_data.get('mission', 'N/A')}
- Values: {', '.join(company_data.get('values', []))}
- Focus Skills: {', '.join(company_data.get('focus_skills', []))}

Candidate:
- Name: {cv_data.get('name', 'N/A')}
- Current Role: {cv_data.get('current_role', 'N/A')}
- Years Experience: {cv_data.get('years_experience', 0)}
- Soft Skills: {', '.join(cv_data.get('soft_skills', []))}
- Tech Skills: {', '.join(cv_data.get('skills', []))}

Return JSON with:
- culture_score: 0-100
- reasoning: why this score
- alignments: list of value alignments
- gaps: list of missing qualities

Return ONLY valid JSON."""
            
            response = self.llm.extract_json(prompt)
            
            return {
                "culture_score": response.get("culture_score", 0),
                "reasoning": response.get("reasoning", ""),
                "alignments": response.get("alignments", []),
                "gaps": response.get("gaps", []),
                "method": "ai"
            }
            
        except Exception as e:
            logger.error(f"Error analyzing culture fit: {e}")
            return self._analyze_fit_fallback(cv_data, company_data)
    
    def _analyze_fit_fallback(self, cv_data: Dict, company_data: Dict) -> Dict:
        """Fallback culture analysis"""
        return {
            "culture_score": 60,
            "reasoning": "Basic analysis only",
            "alignments": [],
            "gaps": [],
            "method": "fallback"
        }


class RedFlagDetector:
    """Detect red flags with context"""
    
    def __init__(self, llm_provider="mistral", api_key=None):
        try:
            self.llm = get_llm(llm_provider, api_key)
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            self.llm = None
    
    def detect_flags(self, cv_data: Dict) -> Dict:
        """
        Detect red flags intelligently
        
        Returns:
            {
                "flags": [...],
                "severity": "low|medium|high",
                "context": "..."
            }
        """
        
        if not self.llm:
            return self._detect_flags_fallback(cv_data)
        
        try:
            cv_text = f"""
Experience Timeline:
{self._get_timeline(cv_data)}

Current Role: {cv_data.get('current_role', 'N/A')}
Years Experience: {cv_data.get('years_experience', 0)}
"""
            
            prompt = f"""Analyze this CV for potential red flags.
Be contextual - job hopping might be OK if roles improved.
Gaps might be justified (education, sabbatical).

CV:
{cv_text}

Return JSON with:
- flags: list of potential issues
- severity: low/medium/high
- context: explanation of flags
- is_concerning: boolean if serious

Return ONLY valid JSON."""
            
            response = self.llm.extract_json(prompt)
            
            return {
                "flags": response.get("flags", []),
                "severity": response.get("severity", "low"),
                "context": response.get("context", ""),
                "is_concerning": response.get("is_concerning", False),
                "method": "ai"
            }
            
        except Exception as e:
            logger.error(f"Error detecting flags: {e}")
            return self._detect_flags_fallback(cv_data)
    
    def _detect_flags_fallback(self, cv_data: Dict) -> Dict:
        """Fallback flag detection"""
        return {
            "flags": [],
            "severity": "low",
            "context": "Basic analysis",
            "is_concerning": False,
            "method": "fallback"
        }
    
    def _get_timeline(self, cv_data: Dict) -> str:
        """Get simplified experience timeline"""
        timeline = ""
        for exp in cv_data.get("experience", []):
            timeline += f"- {exp.get('role', 'N/A')} ({exp.get('duration', 'N/A')})\n"
        return timeline


class FeedbackGenerator:
    """Generate personalized feedback using AI"""
    
    def __init__(self, llm_provider="mistral", api_key=None):
        try:
            self.llm = get_llm(llm_provider, api_key)
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {e}")
            self.llm = None
    
    def generate_feedback(self, analysis: Dict) -> str:
        """
        Generate personalized feedback based on analysis
        
        Args:
            analysis: {
                "candidate": {...},
                "company": {...},
                "match_score": 75,
                "skills_analysis": {...},
                "culture_fit": {...},
                "red_flags": {...}
            }
        """
        
        if not self.llm:
            return self._generate_feedback_fallback(analysis)
        
        try:
            prompt = f"""Generate constructive, actionable feedback for this candidate.
Be specific and helpful. Mention what they did well and what they can improve.

Candidate: {analysis.get('candidate', {}).get('name', 'Unknown')}
Match Score: {analysis.get('match_score', 0)}%

Strengths:
{', '.join(analysis.get('skills_analysis', {}).get('soft_skills', []))}

Culture Alignment:
{analysis.get('culture_fit', {}).get('reasoning', '')}

Red Flags:
{', '.join(analysis.get('red_flags', {}).get('flags', []))}

Generate personalized feedback that:
1. Celebrates their strengths
2. Explains why they match (or don't match)
3. Gives 2-3 specific improvement suggestions
4. Is encouraging and professional

Keep it to 150-200 words."""
            
            feedback = self.llm.generate_text(prompt)
            return feedback
            
        except Exception as e:
            logger.error(f"Error generating feedback: {e}")
            return self._generate_feedback_fallback(analysis)
    
    def _generate_feedback_fallback(self, analysis: Dict) -> str:
        """Fallback feedback"""
        candidate_name = analysis.get('candidate', {}).get('name', 'Candidate')
        score = analysis.get('match_score', 0)
        
        return f"""Thank you for your application, {candidate_name}!

Your profile shows a match score of {score}%. Your experience and skills align well with our requirements.

We encourage you to continue developing your leadership experience and technical depth.

Best of luck with your career!"""
