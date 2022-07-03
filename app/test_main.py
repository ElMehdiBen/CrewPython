from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    headers = {
        'Authorization': 'Basic Y3JldzpjcmV3LXNlY3JldA=='
    }
    response = client.get("/", headers = headers)
    assert response.status_code == 200
    assert response.json() == { "Result": "Hello Everyone, This is Archipel Cognitive Python Backend" }


def test_read_user():
    headers = {
        'Authorization': 'Basic Y3JldzpjcmV3LXNlY3JldA=='
    }
    response = client.get("/users/me", headers = headers)
    assert response.status_code == 200
    assert response.json() == { "username": "crew" }