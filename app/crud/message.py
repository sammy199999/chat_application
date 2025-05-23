from motor.motor_asyncio import AsyncIOMotorClient
from app.models.mongo_models import ChatContent, QAPair
from datetime import datetime

async def add_message(mongo_client: AsyncIOMotorClient, message_data: dict):
    db = mongo_client.chat_db
    chat = await db.chats.find_one({"chat_id": message_data["chat_id"]})
    new_qa = {
        "question": message_data["question"],
        "response": message_data["response"],
        "response_id": message_data["response_id"],
        "timestamp": message_data["timestamp"],
        "branches": []
    }
    if chat:
        await db.chats.update_one({"chat_id": message_data["chat_id"]}, {"$push": {"qa_pairs": new_qa}})
    else:
        content = {
            "chat_id": message_data["chat_id"],
            "qa_pairs": [new_qa]
        }
        await db.chats.insert_one(content)

async def get_chat_history(mongo_client: AsyncIOMotorClient, chat_id: str):
    db = mongo_client.chat_db
    return await db.chats.find_one({"chat_id": chat_id})