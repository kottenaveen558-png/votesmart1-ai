"""Election data service"""
from app.models.election import Election, ElectionStep
from typing import List, Optional
from datetime import datetime

class ElectionService:
    """Service for election data management"""
    
    def __init__(self):
        self.elections = self._init_elections()
    
    def _init_elections(self) -> List[Election]:
        """Initialize sample elections"""
        steps_2026 = [
            ElectionStep(
                id="registration",
                title="Voter Registration",
                description="Register to vote in your state",
                date=datetime(2026, 6, 1),
                duration="30 days"
            ),
            ElectionStep(
                id="early_voting",
                title="Early Voting Period",
                description="Vote before election day at polling locations",
                date=datetime(2026, 10, 20),
                duration="2 weeks"
            ),
            ElectionStep(
                id="election_day",
                title="Election Day",
                description="Official voting day",
                date=datetime(2026, 11, 3),
                duration="1 day"
            ),
            ElectionStep(
                id="counting",
                title="Vote Counting",
                description="Election officials count all votes",
                date=datetime(2026, 11, 4),
                duration="3-5 days"
            ),
        ]
        
        return [
            Election(
                id="2026_presidential",
                name="2026 Presidential Election",
                date=datetime(2026, 11, 3),
                type="presidential",
                steps=steps_2026,
                status="upcoming"
            )
        ]
    
    def get_all_elections(self) -> List[Election]:
        """Get all elections"""
        return self.elections
    
    def get_election(self, election_id: str) -> Optional[Election]:
        """Get election by ID"""
        for election in self.elections:
            if election.id == election_id:
                return election
        return None
    
    def get_timeline(self, election_id: str) -> Optional[List[dict]]:
        """Get election timeline"""
        election = self.get_election(election_id)
        if not election:
            return None
        return [
            {
                "step": step.title,
                "date": step.date.isoformat() if step.date else None,
                "description": step.description
            }
            for step in election.steps
        ]
    
    def get_steps(self, election_id: str) -> Optional[List[dict]]:
        """Get all steps for an election"""
        election = self.get_election(election_id)
        if not election:
            return None
        return [step.dict() for step in election.steps]
