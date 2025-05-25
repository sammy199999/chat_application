from motor.motor_asyncio import AsyncIOMotorClient
from app.models.mongo_models import ChatContent, QAPair
from datetime import datetime

async def add_message(mongo_client: AsyncIOMotorClient, message_data: dict):
    """
    Add a new message (QA pair) to a chat document in MongoDB.
    If the chat does not exist, create a new chat document.

    Args:
        mongo_client (AsyncIOMotorClient): MongoDB client.
        message_data (dict): Dictionary containing message details.

    Raises:
        Exception: If the database operation fails.
    """
    try:
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
    except Exception as e:
        raise Exception(f"Error adding message: {str(e)}")

async def get_chat_history(mongo_client: AsyncIOMotorClient, chat_id: str):
    """
    Retrieve the chat document (including all QA pairs) for a given chat ID.

    Args:
        mongo_client (AsyncIOMotorClient): MongoDB client.
        chat_id (str): The chat ID to retrieve history for.

    Returns:
        dict or None: The chat document if found, else None.

    Raises:
        Exception: If the database operation fails.
    """
    try:
        db = mongo_client.chat_db
        return await db.chats.find_one({"chat_id": chat_id})
    except Exception as e:
        raise Exception(f"Error retrieving chat history: {str(e)}")