import pytest
from fastapi.testclient import TestClient
from word_count_service.main import app

client = TestClient(app)

def test_count_words():
    text = "This is a test sentence."
    response = client.post("/analyze", json={"text": text})
    assert response.status_code == 200
    assert response.json() == {"word_count": 5}
