"""Security utilities"""
from typing import Optional
import hashlib
import secrets

class SecurityManager:
    """Security utilities for input validation and data protection"""
    
    @staticmethod
    def hash_data(data: str) -> str:
        """Hash sensitive data using SHA-256"""
        return hashlib.sha256(data.encode()).hexdigest()
    
    @staticmethod
    def generate_token(length: int = 32) -> str:
        """Generate secure random token"""
        return secrets.token_hex(length // 2)
    
    @staticmethod
    def sanitize_input(data: str, max_length: int = 1000) -> str:
        """Sanitize user input"""
        if not isinstance(data, str):
            return ""
        return data.strip()[:max_length]
