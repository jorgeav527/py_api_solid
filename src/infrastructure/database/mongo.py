from motor.motor_asyncio import AsyncIOMotorClient
import os

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "solid_example_db")

# Global client reference (singleton)
client: AsyncIOMotorClient | None = None

async def connect_to_mongo():
    """Initialize global MongoDB connection"""
    global client
    if client is None:
        client = AsyncIOMotorClient(MONGO_URL)
        await client.admin.command("ping")
        print("✅ Connected to MongoDB!")

async def close_mongo_connection():
    """Close global MongoDB connection"""
    global client
    if client:
        client.close()
        print("🛑 MongoDB connection closed")
        client = None

async def get_database():
    """Return the database instance (used as FastAPI dependency)"""
    global client
    if client is None:
        # Auto-reconnect if not initialized (shouldn’t happen if lifespan is used)
        await connect_to_mongo()
    return client[DB_NAME]
