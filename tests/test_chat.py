from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_chat():
    response = client.post("/api/v1/chats/create-chat", json={
        "account_id": "user1",
        "chat_type": "personal",
        "name": "Test Chat"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Chat"