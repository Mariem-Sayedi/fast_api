# Test des routes 'track' et 'events'


from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_track_event():
    response = client.post("/track", json={
        "user_id": "user123",
        "product_id": "prod456",
        "event_type": "view"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "success"

def test_get_events():
    response = client.get("/events")
    assert response.status_code == 200
    assert isinstance(response.json(), list)  
