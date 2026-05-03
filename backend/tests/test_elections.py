"""Election API tests"""
import pytest
from fastapi.testclient import TestClient
from app import create_app

@pytest.fixture
def client():
    """Create test client"""
    app = create_app()
    return TestClient(app)

def test_health_check(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_elections(client):
    """Test get all elections"""
    response = client.get("/api/v1/elections")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_election_by_id(client):
    """Test get election by ID"""
    response = client.get("/api/v1/elections/2026_presidential")
    assert response.status_code == 200
    data = response.json()
    assert data["data"]["id"] == "2026_presidential"

def test_get_nonexistent_election(client):
    """Test get nonexistent election"""
    response = client.get("/api/v1/elections/nonexistent")
    assert response.status_code == 404

def test_get_election_timeline(client):
    """Test get election timeline"""
    response = client.get("/api/v1/elections/2026_presidential/timeline")
    assert response.status_code == 200
    data = response.json()
    assert "timeline" in data
    assert len(data["timeline"]) > 0

def test_get_election_steps(client):
    """Test get election steps"""
    response = client.get("/api/v1/elections/2026_presidential/steps")
    assert response.status_code == 200
    data = response.json()
    assert "steps" in data
    assert len(data["steps"]) > 0
