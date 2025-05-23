from fastapi import FastAPI
from app.routes import chat_routes, message_routes, branch_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(chat_routes.router, prefix="/api/v1/chats", tags=["Chats"])
app.include_router(message_routes.router, prefix="/api/v1/messages", tags=["Messages"])
app.include_router(branch_routes.router, prefix="/api/v1/branches", tags=["Branches"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)