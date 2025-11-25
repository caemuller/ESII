from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_get_history():
    response = client.get("/history?from=USD&to=BRL")
    assert response.status_code == 200
    
    data = response.json()
    assert data["from"] == "USD"
    assert data["to"] == "BRL"
    assert "values" in data
    assert len(data["values"]) > 0
    assert "price" in data["values"][0]