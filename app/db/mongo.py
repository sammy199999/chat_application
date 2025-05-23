from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import Depends

def get_mongo_client():
    return AsyncIOMotorClient("mongodb://localhost:27017")