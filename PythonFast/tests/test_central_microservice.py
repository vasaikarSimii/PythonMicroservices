import pytest
from fastapi.testclient import TestClient
from central_microservice.main import app

client = TestClient(app)

def test_register_service():
    service_name = "test_service"
    port = 8080
    response = client.post(f"/register?service_name={service_name}&port={port}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Service '{service_name}' registered successfully."}

def test_analyze_text():
    service_name = "test_service"
    port = 8080
    text = "This is a test text."
    # Register a test service
    client.post(f"/register?service_name={service_name}&port={port}")
    # Analyze text using the test service
    response = client.post("/analyze", json={"service_name": service_name, "text": text})
    assert response.status_code == 200
    