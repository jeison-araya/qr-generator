"""
Main utilities for the application.
"""
from fastapi import encoders


def jsonable_encoder(obj):
    """JSON encoder for SQLAlchemy models."""
    return encoders.jsonable_encoder(obj)
