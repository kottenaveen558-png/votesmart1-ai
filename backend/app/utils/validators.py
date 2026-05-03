"""Input validators"""
from typing import Optional
import re

class Validators:
    """Input validation utilities"""
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_valid_election_id(election_id: str) -> bool:
        """Validate election ID format"""
        pattern = r'^[a-z0-9_]+$'
        return re.match(pattern, election_id) is not None
    
    @staticmethod
    def is_valid_date_format(date_str: str) -> bool:
        """Validate date format YYYY-MM-DD"""
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        return re.match(pattern, date_str) is not None
