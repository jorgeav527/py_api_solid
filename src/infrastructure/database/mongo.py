from motor.motor_asyncio import AsyncIOMotorClient
import os
from contextlib import asynccontextmanager

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "solid_example_db")


@asynccontextmanager
async def get_database():
    """Yields a MongoDB database connection (FastAPI dependency style)"""
    client = AsyncIOMotorClient(MONGO_URL)
    db = client[DB_NAME]
    try:
        yield db
    finally:
        client.close()
