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

Pass the API Key in the request headers:

```
X-API-Key: secret-api-key
```

## API Endpoints

- `/api/v1/chats/create-chat`
- `/api/v1/messages/add-message`
- `/api/v1/branches/create-branch`
