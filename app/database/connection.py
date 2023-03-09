"""
This file is used to connect to the MongoDB database.
"""
import os

from dotenv import load_dotenv
import motor.motor_asyncio

load_dotenv()

_client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])


def get_db():
    """Get database."""
    return _client[os.environ["MONGODB_DATABASE"]]
