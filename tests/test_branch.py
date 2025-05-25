from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

@patch("app.routes.branch_routes.create_branch")
def test_create_branch_view_success(mock_create_branch):
    mock_create_branch.return_value = None
    response = client.post("/api/v1/branches/create-branch", json={
        "base_chat_id": "chat1",
        "response_id": "resp1",
        "new_branch_id": "branch2"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200
    assert response.json()["msg"] == "Branch created"

@patch("app.routes.branch_routes.create_branch")
def test_create_branch_view_failure(mock_create_branch):
    mock_create_branch.side_effect = Exception("DB error")
    response = client.post("/api/v1/branches/create-branch", json={
        "base_chat_id": "chat1",
        "response_id": "resp1",
        "new_branch_id": "branch2"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 500
    assert "Failed to create branch" in response.json()["detail"]

def test_create_branch_view_validation_error():
    # Missing required field 'new_branch_id'
    response = client.post("/api/v1/branches/create-branch", json={
        "base_chat_id": "chat1",
        "response_id": "resp1"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 422

@patch("app.routes.branch_routes.get_all_branches")
def test_get_branches_view_success(mock_get_all_branches):
    mock_get_all_branches.return_value = ["branch1", "branch2"]
    response = client.get("/api/v1/branches/get-branches", params={"chat_id": "chat1"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200
    assert "branches" in response.json()
    assert isinstance(response.json()["branches"], list)

@patch("app.routes.branch_routes.get_all_branches")
def test_get_branches_view_failure(mock_get_all_branches):
    mock_get_all_branches.side_effect = Exception("DB error")
    response = client.get("/api/v1/branches/get-branches", params={"chat_id": "chat1"}, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 500
    assert "Failed to get branches" in response.json()["detail"]

def test_get_branches_view_validation_error():
    # Missing required param 'chat_id'
    response = client.get("/api/v1/branches/get-branches", headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 422

def test_set_active_branch_success():
    response = client.put("/api/v1/branches/set-active-branch", json={
        "chat_id": "chat1",
        "branch_id": "branch2"
    }, headers={"X-API-Key": "secret-api-key"})
    assert response.status_code == 200
    assert "set as active" in response.json()["msg"]
