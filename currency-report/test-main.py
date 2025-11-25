from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "UP"}

def test_get_quote():
    response = client.get("/quote?from=USD&to=BRL")
    assert response.status_code == 200
    data = response.json()
    assert data["from"] == "USD"
    assert data["to"] == "BRL"
    assert "price" in data
    assert isinstance(data["price"], float)