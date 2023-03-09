"""
This file is used to create a testing MongoDB database.
"""
from mongomock_motor import AsyncMongoMockClient
from app.database.connection import get_db

test_db = AsyncMongoMockClient()['tests']


def override_get_db():
    """Get database."""
    return test_db


def test_get_db():
    """Testing get database."""
    assert get_db() is not None
