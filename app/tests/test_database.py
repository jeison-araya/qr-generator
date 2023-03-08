"""
This file is used to create a testing MongoDB database.
"""
from mongomock_motor import AsyncMongoMockClient
from app.database import get_db


def override_get_db():
    """Get database."""
    return AsyncMongoMockClient()['tests']


def test_get_db():
    """Testing get database."""
    assert get_db() is not None
