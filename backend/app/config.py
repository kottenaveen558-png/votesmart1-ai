"""Application configuration"""
from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    """Application settings"""
    API_TITLE: str = "VoteSmart Pro"
    DEBUG: bool = False
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]
    GOOGLE_SHEETS_API_KEY: str = ""
    GOOGLE_SERVICE_ACCOUNT_JSON: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()
