from motor.motor_asyncio import AsyncIOMotorClient

async def create_branch(mongo_client: AsyncIOMotorClient, base_chat_id: str, response_id: str, new_branch_id: str):
    """
    Add a new branch to a specific QA pair in a chat document.

    Args:
        mongo_client (AsyncIOMotorClient): MongoDB client.
        base_chat_id (str): The chat ID where the branch will be added.
        response_id (str): The response ID to which the branch is attached.
        new_branch_id (str): The new branch ID to add.

    Raises:
        Exception: If the database operation fails.
    """
    try:
        db = mongo_client.chat_db
        await db.chats.update_one(
            {"chat_id": base_chat_id, "qa_pairs.response_id": response_id},
            {"$push": {"qa_pairs.$.branches": new_branch_id}}
        )
    except Exception as e:
        raise Exception(f"Error creating branch: {str(e)}")

async def get_all_branches(mongo_client: AsyncIOMotorClient, chat_id: str):
    """
    Retrieve all branch IDs for a given chat.

    Args:
        mongo_client (AsyncIOMotorClient): MongoDB client.
        chat_id (str): The chat ID to retrieve branches for.

    Returns:
        list: List of branch IDs.

    Raises:
        Exception: If the database operation fails.
    """
    try:
        db = mongo_client.chat_db
        chat = await db.chats.find_one({"chat_id": chat_id})
        branches = []
        if chat:
            for qa in chat.get("qa_pairs", []):
                branches.extend(qa.get("branches", []))
        return branches
    except Exception as e:
        raise Exception(f"Error retrieving branches: {str(e)}")