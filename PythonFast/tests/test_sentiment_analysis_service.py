import pytest
from fastapi.testclient import TestClient
from sentiment_analysis_service.main import app

client = TestClient(app)

def test_analyze_sentiment_positive():
    text = "This is a wonderful day!"
    response = client.post("/analyze", json={"text": text})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "positive"}

def test_analyze_sentiment_negative():
    text = "I am feeling very sad."
    response = client.post("/analyze", json={"text": text})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "negative"}

def test_analyze_sentiment_neutral():
    text = "This is an okay movie."
    response = client.post("/analyze", json={"text": text})
    assert response.status_code == 200
    assert response.json() == {"sentiment": "neutral"}
