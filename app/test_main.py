from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "Result": "Hello Everyone, This is Archipel Cognitive Python Backend" }


def test_read_main():
    response = client.get("/users/me")
    assert response.status_code == 200
    assert response.json() == {"username": "crew"}