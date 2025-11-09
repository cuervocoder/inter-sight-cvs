"""Simplified AI Matcher - Direct implementation"""

import os
import logging
import json
from typing import Dict, List

logger = logging.getLogger(__name__)


def get_llm_instance(provider="mistral"):
    """Get LLM instance directly"""
    try:
        from core.llm_provider import get_llm
        api_key = os.getenv(f"{provider.upper()}_API_KEY")
        return get_llm(provider, api_key)
    except Exception as e:
        logger.error(f"Failed to get LLM: {e}")
        return None


class SimpleMatcher:
    """Simple AI matcher"""
    
    def __init__(self, company_profile: Dict):
        self.company_profile = company_profile
        self.llm = get_llm_instance()
    
    def analyze_candidate(self, cv_data: Dict) -> Dict:
        """Analyze candidate with AI"""
        
        if not self.llm:
            return self._basic_analysis(cv_data)
        
        try:
            # Build CV summary
            cv_summary = f"""
Name: {cv_data.get('name', 'N/A')}
Email: {cv_data.get('email', 'N/A')}
Degree: {cv_data.get('degree', 'N/A')}
Years Experience: {cv_data.get('years_experience', 0)}
Skills: {', '.join(cv_data.get('skills', []))}
Soft Skills: {', '.join(cv_data.get('soft_skills', []))}
Experience: {', '.join([e.get('role', 'N/A') for e in cv_data.get('experience', [])])}
"""
            
            company_summary = f"""
Mission: {self.company_profile.get('mission', 'N/A')}
Values: {', '.join(self.company_profile.get('values', []))}
Focus Skills: {', '.join(self.company_profile.get('focus_skills', []))}
"""
            
            # Get AI analysis
            prompt = f"""Analyze this candidate for the company.
Return JSON with:
- overall_score: 0-100
- technical_score: 0-100
- culture_score: 0-100
- cv_quality_score: 0-100
- strengths: list of 3 strengths
- improvements: list of 2 improvements
- feedback: 100 word personalized feedback
- ranking: "🟢 Excellent" / "🟡 Good" / "🟠 Fair" / "🔴 Poor"

CANDIDATE:
{cv_summary}

COMPANY:
{company_summary}

Return ONLY valid JSON."""
            
            response = self.llm.extract_json(prompt)
            
            if response:
                return {
                    "overall_score": response.get("overall_score", 65),
                    "technical_score": response.get("technical_score", 65),
                    "culture_score": response.get("culture_score", 65),
                    "cv_quality_score": response.get("cv_quality_score", 65),
                    "strengths": response.get("strengths", []),
                    "improvements": response.get("improvements", []),
                    "feedback": response.get("feedback", ""),
                    "ranking": response.get("ranking", "🟠 Fair"),
                    "method": "ai"
                }
            else:
                return self._basic_analysis(cv_data)
                
        except Exception as e:
            logger.error(f"Error analyzing with AI: {e}")
            return self._basic_analysis(cv_data)
    
    def _basic_analysis(self, cv_data: Dict) -> Dict:
        """Basic analysis without AI"""
        score = 60
        
        if cv_data.get("skills"):
            score += 10
        if cv_data.get("soft_skills"):
            score += 10
        if cv_data.get("years_experience", 0) > 3:
            score += 5
        
        return {
            "overall_score": score,
            "technical_score": score,
            "culture_score": score,
            "cv_quality_score": 70,
            "strengths": ["Professional background", "Clear CV structure"],
            "improvements": ["Add more metrics", "Show leadership examples"],
            "feedback": f"Basic profile analysis. Score: {score}%",
            "ranking": "🟡 Good" if score >= 70 else "🟠 Fair",
            "method": "basic"
        }


def match_candidates(company_profile: Dict, candidates: List[Dict]) -> List[Dict]:
    """Match all candidates"""
    
    matcher = SimpleMatcher(company_profile)
    results = []
    
    for candidate in candidates:
        analysis = matcher.analyze_candidate(candidate)
        analysis["name"] = candidate.get("name", "Unknown")
        results.append(analysis)
    
    # Sort by overall score
    results = sorted(results, key=lambda x: x.get("overall_score", 0), reverse=True)
    
    for idx, result in enumerate(results, 1):
        result["rank"] = idx
    
    return results