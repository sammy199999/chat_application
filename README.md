# FastAPI Chat Application

## Overview

This is a FastAPI-based microservice backend for a chat application that supports message branching.

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

## Authentication

All API endpoints require an API Key for authentication.
Pass the API Key in the request headers:

```
X-API-Key: secret-api-key
```

## API Endpoints

### Chat Endpoints
- `POST   /api/v1/chats/create-chat`  Create a new chat
- `GET    /api/v1/chats/get-chat?chat_id={chat_id}`  Get chat by ID
- `PUT    /api/v1/chats/update-chat?chat_id={chat_id}`  Update chat name
- `DELETE /api/v1/chats/delete-chat?chat_id={chat_id}`  Delete chat

### Message Endpoints
- `POST   /api/v1/messages/add-message`  Add a message to a chat
- `GET    /api/v1/messages/get-messages?chat_id={chat_id}`  Get all messages for a chat

### Branch Endpoints
- `POST   /api/v1/branches/create-branch`  Create a branch for a chat
- `GET    /api/v1/branches/get-branches?chat_id={chat_id}`  Get all branches for a chat
- `PUT    /api/v1/branches/set-active-branch`  Set a branch as active

## Testing

To run all unit tests:
```bash
pytest
```

**Note:**
All test requests must include the `X-API-Key` header.

## Postman Collection

A sample Postman collection is available for all endpoints.
You can import the provided JSON file into Postman for quick testing.
chat_app.postman_collection.json
---