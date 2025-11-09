"""Enhanced AI Matcher - Better prompts and fallback analysis"""

import os
import logging
import json
from typing import Dict, List
import re

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


class EnhancedMatcher:
    """Enhanced AI matcher with detailed analysis"""
    
    def __init__(self, company_profile: Dict):
        self.company_profile = company_profile
        self.llm = get_llm_instance()
    
    def analyze_candidate(self, cv_data: Dict) -> Dict:
        """Analyze candidate with detailed AI analysis"""
        
        if self.llm:
            # Try AI analysis first
            ai_analysis = self._ai_analysis(cv_data)
            if ai_analysis:
                return ai_analysis
        
        # Fallback to enhanced manual analysis
        return self._enhanced_manual_analysis(cv_data)
    
    def _ai_analysis(self, cv_data: Dict) -> Dict:
        """Try to get AI analysis"""
        try:
            # Step 1: Extract and analyze skills
            skills_analysis = self._ai_analyze_skills(cv_data)
            
            # Step 2: Analyze soft skills
            soft_skills_analysis = self._ai_analyze_soft_skills(cv_data)
            
            # Step 3: Culture fit
            culture_analysis = self._ai_analyze_culture_fit(cv_data)
            
            # Step 4: Generate comprehensive feedback
            feedback = self._ai_generate_feedback(
                cv_data, 
                skills_analysis, 
                soft_skills_analysis, 
                culture_analysis
            )
            
            # Calculate scores
            technical_score = min(100, 50 + len(cv_data.get("skills", [])) * 8)
            culture_score = culture_analysis.get("score", 65)
            cv_quality = self._calculate_cv_quality(cv_data)
            overall_score = int((technical_score * 0.35 + culture_score * 0.30 + cv_quality * 0.35))
            
            return {
                "overall_score": overall_score,
                "technical_score": technical_score,
                "culture_score": culture_score,
                "cv_quality_score": cv_quality,
                "strengths": skills_analysis.get("strengths", []) + soft_skills_analysis.get("strengths", []),
                "improvements": soft_skills_analysis.get("gaps", []),
                "feedback": feedback,
                "ranking": self._get_ranking(overall_score),
                "method": "ai",
                "skills_detail": skills_analysis,
                "soft_skills_detail": soft_skills_analysis,
                "culture_detail": culture_analysis
            }
            
        except Exception as e:
            logger.error(f"AI analysis failed: {e}")
            return None
    
    def _ai_analyze_skills(self, cv_data: Dict) -> Dict:
        """Analyze technical skills with AI"""
        try:
            skills_list = cv_data.get("skills", [])
            experience_text = "\n".join([e.get("description", "") for e in cv_data.get("experience", [])])
            
            prompt = f"""Analyze the technical skills of this candidate:

Skills: {', '.join(skills_list)}

Experience:
{experience_text}

Company focus skills: {', '.join(self.company_profile.get('focus_skills', []))}

Provide JSON with:
- matched_skills: list of skills that match company needs
- missing_skills: list of important skills missing
- strengths: list of 3 technical strengths
- proficiency_level: junior/mid/senior

Return ONLY JSON."""
            
            response = self.llm.extract_json(prompt)
            
            if response:
                return {
                    "matched_skills": response.get("matched_skills", []),
                    "missing_skills": response.get("missing_skills", []),
                    "strengths": response.get("strengths", []),
                    "proficiency": response.get("proficiency_level", "mid")
                }
        except Exception as e:
            logger.error(f"Skills analysis error: {e}")
        
        return self._manual_skills_analysis(cv_data)
    
    def _ai_analyze_soft_skills(self, cv_data: Dict) -> Dict:
        """Analyze soft skills with AI"""
        try:
            soft_skills = cv_data.get("soft_skills", [])
            experience_text = "\n".join([e.get("description", "") for e in cv_data.get("experience", [])])
            role = cv_data.get("current_role", "")
            years = cv_data.get("years_experience", 0)
            
            prompt = f"""Analyze the soft skills of this candidate:

Current soft skills: {', '.join(soft_skills)}
Current role: {role}
Years of experience: {years}

Experience highlights:
{experience_text}

Company values: {', '.join(self.company_profile.get('values', []))}

Provide JSON with:
- identified_soft_skills: list of soft skills demonstrated
- leadership_level: none/junior/mid/senior
- communication_score: 1-100
- collaboration_score: 1-100
- adaptability_score: 1-100
- strengths: list of 3 soft skill strengths
- gaps: list of 2 areas to develop

Return ONLY JSON."""
            
            response = self.llm.extract_json(prompt)
            
            if response:
                return {
                    "identified_skills": response.get("identified_soft_skills", []),
                    "leadership": response.get("leadership_level", "junior"),
                    "communication": response.get("communication_score", 65),
                    "collaboration": response.get("collaboration_score", 65),
                    "adaptability": response.get("adaptability_score", 65),
                    "strengths": response.get("strengths", []),
                    "gaps": response.get("gaps", [])
                }
        except Exception as e:
            logger.error(f"Soft skills analysis error: {e}")
        
        return self._manual_soft_skills_analysis(cv_data)
    
    def _ai_analyze_culture_fit(self, cv_data: Dict) -> Dict:
        """Analyze culture fit with AI"""
        try:
            prompt = f"""Analyze culture fit:

Candidate:
- Name: {cv_data.get('name', 'N/A')}
- Role: {cv_data.get('current_role', 'N/A')}
- Years exp: {cv_data.get('years_experience', 0)}
- Soft skills: {', '.join(cv_data.get('soft_skills', []))}

Company:
- Mission: {self.company_profile.get('mission', 'N/A')}
- Values: {', '.join(self.company_profile.get('values', []))}

Provide JSON with:
- score: 0-100 culture fit score
- aligned_values: list of matching values
- misaligned_values: list of conflicting values
- assessment: brief assessment

Return ONLY JSON."""
            
            response = self.llm.extract_json(prompt)
            
            if response:
                return {
                    "score": response.get("score", 65),
                    "aligned": response.get("aligned_values", []),
                    "misaligned": response.get("misaligned_values", []),
                    "assessment": response.get("assessment", "")
                }
        except Exception as e:
            logger.error(f"Culture analysis error: {e}")
        
        return {"score": 65, "aligned": [], "misaligned": [], "assessment": ""}
    
    def _ai_generate_feedback(self, cv_data: Dict, skills: Dict, soft_skills: Dict, culture: Dict) -> str:
        """Generate comprehensive AI feedback"""
        try:
            prompt = f"""Generate detailed, actionable feedback for this candidate:

Name: {cv_data.get('name', 'N/A')}
Years exp: {cv_data.get('years_experience', 0)}

Technical strengths: {', '.join(skills.get('strengths', []))}
Soft skill strengths: {', '.join(soft_skills.get('strengths', []))}
Culture fit: {culture.get('assessment', '')}

Areas to improve:
- Technical: {', '.join(skills.get('missing_skills', [])[:2])}
- Soft: {', '.join(soft_skills.get('gaps', [])[:2])}

Write personalized, encouraging feedback (150 words) that:
1. Celebrates their strengths
2. Explains why they're a good fit
3. Gives 2-3 specific improvements

Be professional but warm."""
            
            feedback = self.llm.generate_text(prompt)
            if feedback:
                return feedback
        except Exception as e:
            logger.error(f"Feedback generation error: {e}")
        
        return self._generate_manual_feedback(cv_data, skills, soft_skills, culture)
    
    def _enhanced_manual_analysis(self, cv_data: Dict) -> Dict:
        """Enhanced manual analysis when AI fails"""
        
        skills_analysis = self._manual_skills_analysis(cv_data)
        soft_skills_analysis = self._manual_soft_skills_analysis(cv_data)
        culture_analysis = self._manual_culture_analysis(cv_data)
        
        technical_score = min(100, 50 + len(cv_data.get("skills", [])) * 8)
        culture_score = culture_analysis.get("score", 60)
        cv_quality = self._calculate_cv_quality(cv_data)
        overall_score = int((technical_score * 0.35 + culture_score * 0.30 + cv_quality * 0.35))
        
        feedback = self._generate_manual_feedback(cv_data, skills_analysis, soft_skills_analysis, culture_analysis)
        
        return {
            "overall_score": overall_score,
            "technical_score": technical_score,
            "culture_score": culture_score,
            "cv_quality_score": cv_quality,
            "strengths": skills_analysis.get("strengths", []) + soft_skills_analysis.get("strengths", []),
            "improvements": soft_skills_analysis.get("gaps", []),
            "feedback": feedback,
            "ranking": self._get_ranking(overall_score),
            "method": "enhanced_manual",
            "skills_detail": skills_analysis,
            "soft_skills_detail": soft_skills_analysis,
            "culture_detail": culture_analysis
        }
    
    def _manual_skills_analysis(self, cv_data: Dict) -> Dict:
        """Manual technical skills analysis"""
        skills = cv_data.get("skills", [])
        focus_skills = self.company_profile.get("focus_skills", [])
        
        matched = [s for s in skills if s.lower() in [f.lower() for f in focus_skills]]
        missing = [f for f in focus_skills if f.lower() not in [s.lower() for s in skills]]
        
        years = cv_data.get("years_experience", 0)
        proficiency = "senior" if years > 5 else "mid" if years > 2 else "junior"
        
        strengths = []
        if len(matched) > 0:
            strengths.append(f"Strong match in {', '.join(matched[:2])}")
        if len(skills) > 5:
            strengths.append("Diverse technical skill set")
        if years > 3:
            strengths.append(f"{years}+ years of proven experience")
        
        return {
            "matched_skills": matched,
            "missing_skills": missing,
            "strengths": strengths[:3],
            "proficiency": proficiency
        }
    
    def _manual_soft_skills_analysis(self, cv_data: Dict) -> Dict:
        """Manual soft skills analysis"""
        soft_skills = cv_data.get("soft_skills", [])
        role = cv_data.get("current_role", "").lower()
        years = cv_data.get("years_experience", 0)
        
        # Infer soft skills from role and experience
        inferred = []
        if any(word in role for word in ["manager", "lead", "director", "head"]):
            inferred.extend(["Leadership", "Decision-making"])
        if years > 3:
            inferred.extend(["Mentoring", "Strategic thinking"])
        
        all_soft_skills = set(soft_skills + inferred)
        
        communication_score = 60 + (10 if len(soft_skills) > 0 else 0) + (10 if "communication" in [s.lower() for s in soft_skills] else 0)
        collaboration_score = 60 + (10 if "collaboration" in [s.lower() for s in soft_skills] else 0)
        adaptability_score = 60 + (10 if "adaptability" in [s.lower() for s in soft_skills] else 0)
        
        strengths = []
        if "leadership" in [s.lower() for s in all_soft_skills]:
            strengths.append("Demonstrated leadership capabilities")
        if len(all_soft_skills) > 3:
            strengths.append("Well-rounded interpersonal skills")
        if years > 5:
            strengths.append("Seasoned professional with proven track record")
        
        gaps = []
        company_values = self.company_profile.get("values", [])
        for value in company_values:
            if value.lower() not in [s.lower() for s in all_soft_skills]:
                gaps.append(f"Could demonstrate more {value}")
        
        return {
            "identified_skills": list(all_soft_skills),
            "leadership": "senior" if years > 5 else "mid" if years > 2 else "junior",
            "communication": min(100, communication_score),
            "collaboration": min(100, collaboration_score),
            "adaptability": min(100, adaptability_score),
            "strengths": strengths[:3],
            "gaps": gaps[:2]
        }
    
    def _manual_culture_analysis(self, cv_data: Dict) -> Dict:
        """Manual culture fit analysis"""
        soft_skills = set([s.lower() for s in cv_data.get("soft_skills", [])])
        company_values = [v.lower() for v in self.company_profile.get("values", [])]
        
        aligned = [v for v in company_values if any(v_part in soft_skills for v_part in v.split())]
        misaligned = [v for v in company_values if not any(v_part in soft_skills for v_part in v.split())]
        
        score = 60 + (len(aligned) * 10)
        
        return {
            "score": min(100, score),
            "aligned": aligned,
            "misaligned": misaligned,
            "assessment": f"Good fit with focus on {', '.join(aligned[:2])}" if aligned else "Promising candidate"
        }
    
    def _generate_manual_feedback(self, cv_data: Dict, skills: Dict, soft_skills: Dict, culture: Dict) -> str:
        """Generate manual feedback"""
        name = cv_data.get("name", "Candidate")
        years = cv_data.get("years_experience", 0)
        
        feedback = f"""Dear {name},

Thank you for your application. We've conducted a thorough analysis of your profile:

**TECHNICAL STRENGTHS:**
{chr(10).join(['• ' + s for s in skills.get('strengths', [])[:2]])}

**SOFT SKILLS ASSESSMENT:**
- Leadership level: {soft_skills.get('leadership', 'mid')}
- Communication: {soft_skills.get('communication', 65)}%
- Collaboration: {soft_skills.get('collaboration', 65)}%
- Adaptability: {soft_skills.get('adaptability', 65)}%

Key strengths: {', '.join(soft_skills.get('strengths', [])[:2])}

**CULTURE FIT:**
{culture.get('assessment', 'Good alignment with company values')}

**AREAS FOR GROWTH:**
{chr(10).join(['• ' + s for s in soft_skills.get('gaps', [])[:2]])}

**RECOMMENDATIONS:**
1. Enhance {soft_skills.get('gaps', ['collaboration'])[0].lower()} through additional projects
2. Build skills in {', '.join(skills.get('missing_skills', ['cloud technology'])[:1]).lower()}
3. Consider mentorship roles to strengthen leadership

You have solid potential for this role. We'd like to move forward with the next steps.

Best regards,
Inter-Sight Team"""
        
        return feedback
    
    def _calculate_cv_quality(self, cv_data: Dict) -> int:
        """Calculate CV quality score"""
        score = 50
        
        if cv_data.get("name"):
            score += 10
        if cv_data.get("email"):
            score += 10
        if cv_data.get("degree"):
            score += 10
        if cv_data.get("university"):
            score += 5
        if cv_data.get("experience"):
            score += 10
        if cv_data.get("skills"):
            score += 10
        if cv_data.get("years_experience", 0) > 0:
            score += 10
        
        return min(100, score)
    
    def _get_ranking(self, score: int) -> str:
        """Get ranking label"""
        if score >= 85:
            return "🟢 Excellent Match"
        elif score >= 70:
            return "🟡 Good Match"
        elif score >= 50:
            return "🟠 Fair Match"
        else:
            return "🔴 Not Recommended"


def match_candidates(company_profile: Dict, candidates: List[Dict]) -> List[Dict]:
    """Match all candidates"""
    
    matcher = EnhancedMatcher(company_profile)
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