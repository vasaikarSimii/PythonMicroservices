import pytest
from fastapi.testclient import TestClient
from entity_recognition_service.main import app

client = TestClient(app)

def test_recognize_entities():
    text = "Apple is looking at buying U.K. startup for $1 billion"
    response = client.post("/analyze", json={"text": text})
    assert response.status_code == 200
    assert len(response.json()["entities"]) == 4  # Assuming 4 entities are recognized
