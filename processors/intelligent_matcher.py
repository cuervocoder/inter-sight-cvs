"""Intelligent Matcher - Comprehensive candidate matching using AI"""

import logging
from typing import Dict, List
import os

logger = logging.getLogger(__name__)


class IntelligentMatcher:
    """
    Main matcher that combines all AI modules
    Scores candidates based on:
    - Technical skills (35%)
    - Soft skills & culture (30%)
    - Red flags context (20%)
    - CV quality (15%)
    """
    
    def __init__(self, company_profile: Dict, llm_provider="mistral"):
        """Initialize matcher with company profile"""
        self.company_profile = company_profile
        self.llm_provider = llm_provider
        
        # Import modules only when needed
        try:
            from ai_analysis_modules import (
                SkillExtractor,
                CultureAnalyzer,
                RedFlagDetector,
                FeedbackGenerator
            )
            
            api_key = os.getenv(f"{llm_provider.upper()}_API_KEY")
            
            self.skill_extractor = SkillExtractor(llm_provider, api_key)
            self.culture_analyzer = CultureAnalyzer(llm_provider, api_key)
            self.red_flag_detector = RedFlagDetector(llm_provider, api_key)
            self.feedback_generator = FeedbackGenerator(llm_provider, api_key)
            
            self.modules_ready = True
        except Exception as e:
            logger.warning(f"AI modules not available: {e}")
            self.modules_ready = False
    
    def match_candidate(self, cv_data: Dict) -> Dict:
        """
        Match candidate against company profile
        
        Returns comprehensive matching analysis
        """
        
        if not self.modules_ready:
            return self._match_candidate_basic(cv_data)
        
        try:
            # Step 1: Extract skills intelligently
            skills_analysis = self.skill_extractor.extract_skills(cv_data)
            
            # Step 2: Analyze culture fit
            culture_fit = self.culture_analyzer.analyze_fit(cv_data, self.company_profile)
            
            # Step 3: Detect red flags
            red_flags = self.red_flag_detector.detect_flags(cv_data)
            
            # Step 4: Calculate combined score
            technical_score = self._score_technical_skills(cv_data, skills_analysis)
            soft_skills_score = culture_fit.get("culture_score", 60)
            red_flag_penalty = self._calculate_red_flag_penalty(red_flags)
            cv_quality_score = self._score_cv_quality(cv_data)
            
            # Weighted scoring: Tech(35%) + Soft(30%) + RedFlags(20%) + Quality(15%)
            overall_score = (
                technical_score * 0.35 +
                soft_skills_score * 0.30 +
                (100 - red_flag_penalty) * 0.20 +
                cv_quality_score * 0.15
            )
            
            # Step 5: Generate feedback
            analysis_data = {
                "candidate": cv_data,
                "company": self.company_profile,
                "match_score": int(overall_score),
                "skills_analysis": skills_analysis,
                "culture_fit": culture_fit,
                "red_flags": red_flags
            }
            
            feedback = self.feedback_generator.generate_feedback(analysis_data)
            
            return {
                "name": cv_data.get("name", "Unknown"),
                "overall_score": int(overall_score),
                "technical_score": int(technical_score),
                "soft_skills_score": int(soft_skills_score),
                "cv_quality_score": int(cv_quality_score),
                "red_flag_severity": red_flags.get("severity", "low"),
                "skills": skills_analysis,
                "culture_fit": culture_fit,
                "red_flags": red_flags,
                "feedback": feedback,
                "ranking": self._get_ranking_label(overall_score)
            }
            
        except Exception as e:
            logger.error(f"Error matching candidate: {e}")
            return self._match_candidate_basic(cv_data)
    
    def _score_technical_skills(self, cv_data: Dict, skills_analysis: Dict) -> int:
        """Score technical skills match"""
        try:
            candidate_tech_skills = [s.lower() for s in skills_analysis.get("technical_skills", [])]
            company_focus_skills = [s.lower() for s in self.company_profile.get("focus_skills", [])]
            
            if not company_focus_skills:
                return 70  # Default if no focus skills defined
            
            matches = len([s for s in company_focus_skills if s in candidate_tech_skills])
            score = (matches / len(company_focus_skills)) * 100
            
            # Bonus for extra skills
            extra_skills = len([s for s in candidate_tech_skills if s not in company_focus_skills])
            score = min(100, score + (extra_skills * 5))
            
            return int(score)
            
        except Exception as e:
            logger.error(f"Error scoring technical skills: {e}")
            return 60
    
    def _calculate_red_flag_penalty(self, red_flags: Dict) -> int:
        """Calculate penalty based on red flags severity"""
        severity = red_flags.get("severity", "low")
        
        penalties = {
            "low": 5,
            "medium": 15,
            "high": 30
        }
        
        return penalties.get(severity, 5)
    
    def _score_cv_quality(self, cv_data: Dict) -> int:
        """Score CV quality and completeness"""
        score = 50
        
        # Check for key information
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
    
    def _get_ranking_label(self, score: int) -> str:
        """Get ranking label based on score"""
        if score >= 85:
            return "🟢 Excellent Match"
        elif score >= 70:
            return "🟡 Good Match"
        elif score >= 50:
            return "🟠 Fair Match"
        else:
            return "🔴 Not Recommended"
    
    def _match_candidate_basic(self, cv_data: Dict) -> Dict:
        """Basic matching without AI (fallback)"""
        score = 60
        
        if cv_data.get("skills"):
            score += 10
        if cv_data.get("soft_skills"):
            score += 10
        
        return {
            "name": cv_data.get("name", "Unknown"),
            "overall_score": score,
            "technical_score": 60,
            "soft_skills_score": 60,
            "cv_quality_score": self._score_cv_quality(cv_data),
            "red_flag_severity": "low",
            "feedback": "Basic matching - Full AI analysis not available",
            "ranking": self._get_ranking_label(score),
            "method": "fallback"
        }
    
    def rank_candidates(self, candidates_analysis: List[Dict]) -> List[Dict]:
        """Rank candidates by overall score"""
        sorted_candidates = sorted(
            candidates_analysis,
            key=lambda x: x.get("overall_score", 0),
            reverse=True
        )
        
        for idx, candidate in enumerate(sorted_candidates, 1):
            candidate["rank"] = idx
        
        return sorted_candidates
