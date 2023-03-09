"""Create QR Schema"""
from dataclasses import dataclass
from datetime import datetime, timezone
from bson import ObjectId

from pydantic import BaseModel, Field, validator

from app.schemas.py_object_id import PyObjectId


class CreateQR(BaseModel):
    """
    # Create QR Schema

    ## Args:

        * url (str): The url to be encoded in the QR code.
        * dark_color (str, optional): The color of the dark modules. Defaults to #000000.
        * light_color (str, optional): The color of the light modules. Defaults to #FFFFFF.
        * scale (int, optional): The scale of the QR code (1-60). Defaults to 10.
    """
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    url: str
    dark_color: str = '#000000'
    light_color: str = '#FFFFFF'
    scale: int = 10
    created_at: str = Field(default=datetime.now(
        timezone.utc))

    @dataclass
    class Config:
        """Pydantic config"""
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            'example': {
                'url': 'https://www.example.com',
                'dark_color': '#000000',
                'light_color': '#FFFFFF',
                'scale': 10
            }
        }

    @validator('dark_color')
    @classmethod
    def _validate_dark_color(cls, value):
        return cls._validate_hex_color(cls, value)

    @validator('light_color')
    @classmethod
    def _validate_light_color(cls, value):
        return cls._validate_hex_color(cls, value)

    @validator('scale')
    @classmethod
    def _validate_scale(cls, value):
        if value < 6 or value > 40:
            raise ValueError('scale must be between 6 and 40')
        return value

    def _validate_hex_color(self, value):
        if value[0] != '#':
            raise ValueError('color must start with #')
        if len(value) != 7:
            raise ValueError('color must be 7 characters long')
        try:
            int(value[1:], 16)
        except ValueError as exc:
            raise ValueError('color must be a valid hex color') from exc

        return value
