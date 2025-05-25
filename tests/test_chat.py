from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

@patch("app.routes.chat_routes.create_chat")
def test_create_chat_view_success(mock_create_chat):
    mock_create_chat.return_value = {
        "chat_id": "a1419082-17c1-40e2-918d-c3d7fd65c6c5",
        "account_id": "user1",
        "chat_type": "personal",
        "name": "Test Chat",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "active": True
    }
    response = client.post("/api/v1/chats/create-chat", json={
        "account_id": "user1",
        "chat_type": "personal",
        "name": "Test Chat"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Chat"

@patch("app.routes.chat_routes.create_chat")
def test_create_chat_view_failure(mock_create_chat):
    mock_create_chat.side_effect = Exception("DB error")
    response = client.post("/api/v1/chats/create-chat", json={
        "account_id": "user1",
        "chat_type": "personal",
        "name": "Test Chat"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 500
    assert "Failed to create chat" in response.json()["detail"]

@patch("app.routes.chat_routes.get_chat")
def test_get_chat_view_success(mock_get_chat):
    mock_get_chat.return_value = {
        "chat_id": "a1419082-17c1-40e2-918d-c3d7fd65c6c5",
        "account_id": "user1",
        "chat_type": "personal",
        "name": "Test Chat",
        "created_at": "2024-01-01T00:00:00",
        "updated_at": "2024-01-01T00:00:00",
        "active": True
    }
    response = client.get("/api/v1/chats/get-chat", params={"chat_id": "1"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200
    assert response.json()["chat_id"] == "a1419082-17c1-40e2-918d-c3d7fd65c6c5"

@patch("app.routes.chat_routes.get_chat")
def test_get_chat_view_not_found(mock_get_chat):
    mock_get_chat.return_value = None
    response = client.get("/api/v1/chats/get-chat", params={"chat_id": "999"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Chat not found"

@patch("app.routes.chat_routes.get_chat")
def test_get_chat_view_exception(mock_get_chat):
    mock_get_chat.side_effect = Exception("DB error")
    response = client.get("/api/v1/chats/get-chat", params={"chat_id": "1"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 500
    assert "Failed to get chat" in response.json()["detail"]

@patch("app.routes.chat_routes.update_chat")
def test_update_chat_view_success(mock_update_chat):
    mock_update_chat.return_value = {"msg": "Chat updated"}
    response = client.put("/api/v1/chats/update-chat", params={"chat_id": "1"}, json={"name": "Updated Chat"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200

@patch("app.routes.chat_routes.update_chat")
def test_update_chat_view_failure(mock_update_chat):
    mock_update_chat.side_effect = Exception("DB error")
    response = client.put("/api/v1/chats/update-chat", params={"chat_id": "1"}, json={"name": "Updated Chat"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 500
    assert "Failed to update chat" in response.json()["detail"]

@patch("app.routes.chat_routes.delete_chat")
def test_delete_chat_view_success(mock_delete_chat):
    mock_delete_chat.return_value = None
    response = client.delete("/api/v1/chats/delete-chat", params={"chat_id": "1"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200
    assert response.json()["msg"] == "Chat deleted"

@patch("app.routes.chat_routes.delete_chat")
def test_delete_chat_view_failure(mock_delete_chat):
    mock_delete_chat.side_effect = Exception("DB error")
    response = client.delete("/api/v1/chats/delete-chat", params={"chat_id": "1"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 500
    assert "Failed to delete chat" in response.json()["detail"]

def test_create_chat_view_validation_error():
    # Missing required field 'name'
    response = client.post("/api/v1/chats/create-chat", json={
        "account_id": "user1",
        "chat_type": "personal"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 422

def test_update_chat_view_validation_error():
    # Missing required field 'name'
    response = client.put("/api/v1/chats/update-chat", params={"chat_id": "1"}, json={}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 422