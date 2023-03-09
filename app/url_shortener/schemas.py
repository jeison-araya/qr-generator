"""URL schemas"""
from datetime import datetime, timezone
from dataclasses import dataclass

from pydantic import BaseModel, Field

from app.database.schemas import PyObjectId, BaseConfig
from app.url_shortener.util import generate_key


class _URLBase(BaseModel):
    target_url: str
    is_active: bool


class CreateURL(_URLBase):
    """Create URL schema"""
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    key: str = Field(default=generate_key(length=8))
    secret_key: str = Field(default=generate_key(length=16))
    clicks: int = Field(default=0)
    created_at: str = Field(default=datetime.now(timezone.utc))

    @dataclass
    class Config(BaseConfig):
        """Pydantic config"""
        schema_extra = {
            'example': {
                'target_url': 'https://www.example.com',
                'is_active': True
            }
        }


class URL(CreateURL):
    """URL schema"""
    clicks: int
    key: str
    secret_key: str
