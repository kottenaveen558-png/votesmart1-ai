"""Election data models"""
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ElectionStep(BaseModel):
    """Election process step"""
    id: str
    title: str
    description: str
    date: Optional[datetime] = None
    duration: Optional[str] = None
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "registration",
                "title": "Voter Registration",
                "description": "Register to vote in your state",
                "date": "2026-06-01T00:00:00",
                "duration": "30 days"
            }
        }

class Election(BaseModel):
    """Election information"""
    id: str
    name: str
    date: datetime
    type: str  # presidential, midterm, local, etc.
    steps: List[ElectionStep]
    status: str = "upcoming"
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": "2026_presidential",
                "name": "2026 Presidential Election",
                "date": "2026-11-03T00:00:00",
                "type": "presidential",
                "steps": [],
                "status": "upcoming"
            }
        }

class ElectionResponse(BaseModel):
    """API response for elections"""
    success: bool = True
    data: Election
    message: Optional[str] = None
