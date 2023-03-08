"""Create QR Schema"""
from pydantic import BaseModel, validator


class CreateQR(BaseModel):
    """
    Create QR Schema
    
    Args:
        url (str): The url to be encoded in the QR code.
        dark_color (str, optional): The color of the dark modules. Defaults to #000000.
        light_color (str, optional): The color of the light modules. Defaults to #FFFFFF.
        size (int, optional): The scale of the QR code (1-60). Defaults to 10.
    """
    url: str
    dark_color: str = '#000000'
    light_color: str = '#FFFFFF'
    size: int = 10

    @validator('dark_color')
    def _validate_dark_color(cls, v):
        return cls._validate_hex_color(cls, v)

    @validator('light_color')
    def _validate_light_color(cls, v):
        return cls._validate_hex_color(cls, v)

    @validator('size')
    def _validate_size(cls, v):
        if v < 6 or v > 40:
            raise ValueError('size must be between 6 and 40')
        return v

    def _validate_hex_color(self, v):
        if v[0] != '#':
            raise ValueError('color must start with #')
        if len(v) != 7:
            raise ValueError('color must be 7 characters long')
        try:
            int(v[1:], 16)
        except ValueError:
            raise ValueError('color must be a valid hex color')

        return v
