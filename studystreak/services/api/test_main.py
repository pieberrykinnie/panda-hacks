from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_health() -> None:
    """Test the /health endpoint returns status ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}