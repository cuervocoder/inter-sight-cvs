"""LLM Provider Abstraction - Supports Mistral, Claude, OpenAI"""

from abc import ABC, abstractmethod
from typing import Optional, Dict
import json
import logging

logger = logging.getLogger(__name__)


class LLMProvider(ABC):
    """Abstract base class for LLM providers"""
    
    @abstractmethod
    def generate_text(self, prompt: str) -> str:
        """Generate text from prompt"""
        pass
    
    @abstractmethod
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        """Generate structured JSON output"""
        pass


class MistralProvider(LLMProvider):
    """Mistral AI - FREE tier available"""
    
    def __init__(self, api_key: str, model: str = "mistral-large"):
        try:
            from mistralai.client import MistralClient
            self.client = MistralClient(api_key=api_key)
            self.model = model
        except Exception as e:
            logger.error(f"Failed to initialize Mistral: {e}")
            raise
    
    def generate_text(self, prompt: str) -> str:
        """Generate text using Mistral"""
        try:
            from mistralai.models.chat_message import ChatMessage
            
            messages = [ChatMessage(role="user", content=prompt)]
            response = self.client.chat(
                model=self.model,
                messages=messages,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Mistral generation failed: {e}")
            raise
    
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        """Generate JSON response from Mistral"""
        json_prompt = f"""{prompt}

You MUST return ONLY valid JSON. No markdown, no extra text.
{f"Schema: {json.dumps(schema, indent=2)}" if schema else ""}"""
        
        try:
            response = self.generate_text(json_prompt)
            response = response.strip()
            if response.startswith("```"):
                response = response.split("```")[1]
                if response.startswith("json"):
                    response = response[4:]
            return json.loads(response.strip())
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {e}")
            return {}


class ClaudeProvider(LLMProvider):
    """Claude API - Anthropic"""
    
    def __init__(self, api_key: str):
        try:
            from anthropic import Anthropic
            self.client = Anthropic(api_key=api_key)
        except Exception as e:
            logger.error(f"Failed to initialize Claude: {e}")
            raise
    
    def generate_text(self, prompt: str) -> str:
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text
        except Exception as e:
            logger.error(f"Claude generation failed: {e}")
            raise
    
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        json_prompt = f"""{prompt}

Return ONLY valid JSON.
{f"Schema: {json.dumps(schema, indent=2)}" if schema else ""}"""
        
        response = self.generate_text(json_prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {e}")
            return {}


class OpenAIProvider(LLMProvider):
    """OpenAI GPT API"""
    
    def __init__(self, api_key: str):
        try:
            from openai import OpenAI
            self.client = OpenAI(api_key=api_key)
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI: {e}")
            raise
    
    def generate_text(self, prompt: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"OpenAI generation failed: {e}")
            raise
    
    def extract_json(self, prompt: str, schema: Optional[Dict] = None) -> Dict:
        json_prompt = f"""{prompt}

Return ONLY valid JSON.
{f"Schema: {json.dumps(schema, indent=2)}" if schema else ""}"""
        
        response = self.generate_text(json_prompt)
        try:
            return json.loads(response)
        except json.JSONDecodeError as e:
            logger.error(f"JSON parsing failed: {e}")
            return {}


def get_llm(provider_name: str, api_key: str) -> LLMProvider:
    """Factory to get LLM provider"""
    
    providers = {
        "mistral": lambda key: MistralProvider(key),
        "claude": lambda key: ClaudeProvider(key),
        "openai": lambda key: OpenAIProvider(key),
    }
    
    if provider_name not in providers:
        raise ValueError(f"Unknown provider: {provider_name}")
    
    return providers[provider_name](api_key)
