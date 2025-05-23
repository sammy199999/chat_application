from motor.motor_asyncio import AsyncIOMotorClient

async def create_branch(mongo_client: AsyncIOMotorClient, base_chat_id: str, response_id: str, new_branch_id: str):
    db = mongo_client.chat_db
    await db.chats.update_one(
        {"chat_id": base_chat_id, "qa_pairs.response_id": response_id},
        {"$push": {"qa_pairs.$.branches": new_branch_id}}
    )

async def get_all_branches(mongo_client: AsyncIOMotorClient, chat_id: str):
    db = mongo_client.chat_db
    chat = await db.chats.find_one({"chat_id": chat_id})
    branches = []
    if chat:
        for qa in chat.get("qa_pairs", []):
            branches.extend(qa.get("branches", []))
    return branches