"""Configuration management"""

from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """App-wide settings from .env"""
    
    # LLM Configuration
    llm_provider: str = "mistral"
    mistral_api_key: Optional[str] = None
    mistral_model: str = "mistral-large"
    claude_api_key: Optional[str] = None
    openai_api_key: Optional[str] = None
    
    # App Configuration
    app_debug: bool = False
    max_batch_cvs: int = 20
    feedback_mode: str = "hybrid"
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
