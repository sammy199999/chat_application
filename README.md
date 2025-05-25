# FastAPI Chat Application

## Overview

This is a FastAPI-based microservice backend for a chat application that supports message branching, multi-user chat, and persistent storage using both PostgreSQL and MongoDB.

---

## Design Decisions

- **FastAPI** was chosen for its speed, async support, and automatic OpenAPI documentation.
- **PostgreSQL** is used for relational data (chats, accounts) to ensure data integrity and support for complex queries.
- **MongoDB** is used for chat content and message branching, as its flexible schema is ideal for storing nested and evolving chat/message structures.
- **Pydantic v2** is used for data validation, ensuring robust input checking and clear error messages.
- **API Key Authentication** is implemented for simplicity and to secure all endpoints.
- **Separation of Concerns**: CRUD logic, schemas, and routes are separated for maintainability and scalability.
- **Testing**: Unit tests use FastAPI's TestClient and MagicMock for isolated, fast, and reliable tests.
- **CORS** is enabled for all origins to simplify frontend integration during development.

---

## Setup Instructions

1. **Clone the repository**
    ```bash
    git clone <repo_url>
    cd chat_app
    ```

2. **Create virtual environment and install dependencies**
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Run migrations**
    ```bash
    alembic upgrade head
    ```

4. **Start the FastAPI server**
    ```bash
    uvicorn app.main:app --reload
    ```

5. **Run with Docker**
    ```bash
    docker build -t chat_app .
    docker run -p 8000:8000 chat_app
    ```

## Environment Variables

Use a `.env` file to define DB connection strings and API keys.

---

## Authentication

All API endpoints require an API Key for authentication.  
Pass the API Key in the request headers:

```
X-API-Key: secret-api-key
```

---

## API Endpoints

### Chat Endpoints

- `POST   /api/v1/chats/create-chat`  
  **Description:** Create a new chat.  
  **Body:**  
  ```json
  {
    "account_id": "user1",
    "chat_type": "personal",
    "name": "Test Chat"
  }
  ```
  **Response:**  
  ```json
  {
    "chat_id": "uuid",
    "account_id": "user1",
    "chat_type": "personal",
    "name": "Test Chat",
    "created_at": "...",
    "updated_at": "...",
    "active": true
  }
  ```

- `GET    /api/v1/chats/get-chat?chat_id={chat_id}`  
  **Description:** Get chat by ID.  
  **Response:** Chat object as above.

- `PUT    /api/v1/chats/update-chat?chat_id={chat_id}`  
  **Description:** Update chat name.  
  **Body:**  
  ```json
  { "name": "New Chat Name" }
  ```
  **Response:** Updated chat object.

- `DELETE /api/v1/chats/delete-chat?chat_id={chat_id}`  
  **Description:** Delete chat by ID.  
  **Response:**  
  ```json
  { "msg": "Chat deleted" }
  ```

---

### Message Endpoints

- `POST   /api/v1/messages/add-message`  
  **Description:** Add a message to a chat.  
  **Body:**  
  ```json
  {
    "chat_id": "chat1",
    "question": "What is AI?",
    "response": "Artificial Intelligence",
    "response_id": "resp1",
    "timestamp": "2024-01-01T00:00:00"
  }
  ```
  **Response:**  
  ```json
  { "msg": "Message added" }
  ```

- `GET    /api/v1/messages/get-messages?chat_id={chat_id}`  
  **Description:** Get all messages for a chat.  
  **Response:**  
  ```json
  {
    "chat_id": "chat1",
    "qa_pairs": [
      {
        "question": "...",
        "response": "...",
        "response_id": "...",
        "timestamp": "...",
        "branches": [...]
      }
    ]
  }
  ```

---

### Branch Endpoints

- `POST   /api/v1/branches/create-branch`  
  **Description:** Create a branch for a chat.  
  **Body:**  
  ```json
  {
    "base_chat_id": "chat1",
    "response_id": "resp1",
    "new_branch_id": "branch2"
  }
  ```
  **Response:**  
  ```json
  { "msg": "Branch created" }
  ```

- `GET    /api/v1/branches/get-branches?chat_id={chat_id}`  
  **Description:** Get all branches for a chat.  
  **Response:**  
  ```json
  { "branches": ["branch1", "branch2"] }
  ```

- `PUT    /api/v1/branches/set-active-branch`  
  **Description:** Set a branch as active.  
  **Body:**  
  ```json
  {
    "chat_id": "chat1",
    "branch_id": "branch2"
  }
  ```
  **Response:**  
  ```json
  { "msg": "Branch branch2 set as active for chat chat1" }
  ```

---

## Testing

To run all unit tests:
```bash
pytest
```

**Note:**  
All test requests must include the `X-API-Key` header.

---

## Postman Collection

A sample Postman collection is available for all endpoints.  
You can import the provided JSON file (`chat_app.postman_collection.json`) into Postman for quick testing.

---

## Further Documentation

- FastAPI auto-generates OpenAPI docs at:  
  [http://localhost:8000/docs](http://localhost:8000/docs)  
  [http://localhost:8000/redoc](http://localhost:8000/redoc)

---