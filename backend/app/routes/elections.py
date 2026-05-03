"""Election endpoints"""
from fastapi import APIRouter, HTTPException
from app.models.election import Election, ElectionResponse, ElectionStep
from app.services.election_service import ElectionService
from datetime import datetime
from typing import List

router = APIRouter(tags=["elections"])
election_service = ElectionService()

@router.get("/elections", response_model=List[Election])
async def get_elections():
    """
    Get all elections
    - Returns list of elections with timelines and steps
    """
    return election_service.get_all_elections()

@router.get("/elections/{election_id}", response_model=ElectionResponse)
async def get_election(election_id: str):
    """
    Get election details by ID
    - Includes full timeline and process steps
    """
    election = election_service.get_election(election_id)
    if not election:
        raise HTTPException(status_code=404, detail="Election not found")
    return ElectionResponse(data=election)

@router.get("/elections/{election_id}/timeline")
async def get_election_timeline(election_id: str):
    """Get election process timeline"""
    timeline = election_service.get_timeline(election_id)
    if not timeline:
        raise HTTPException(status_code=404, detail="Timeline not found")
    return {"timeline": timeline}

@router.get("/elections/{election_id}/steps")
async def get_election_steps(election_id: str):
    """Get all steps in election process"""
    steps = election_service.get_steps(election_id)
    if not steps:
        raise HTTPException(status_code=404, detail="Steps not found")
    return {"steps": steps}
