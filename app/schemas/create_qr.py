"""Create QR Schema"""
from pydantic import BaseModel, validator


class CreateQR(BaseModel):
    """
    # Create QR Schema
    
    ## Args:
    
        * url (str): The url to be encoded in the QR code.
        * dark_color (str, optional): The color of the dark modules. Defaults to #000000.
        * light_color (str, optional): The color of the light modules. Defaults to #FFFFFF.
        * scale (int, optional): The scale of the QR code (1-60). Defaults to 10.
    """
    url: str
    dark_color: str = '#000000'
    light_color: str = '#FFFFFF'
    scale: int = 10

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
