"""
Helper class to convert ObjectId to string and vice versa
"""
from bson import ObjectId


class PyObjectId(ObjectId):
    """Helper class to convert ObjectId to string and vice versa"""
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        """Validate the objectid"""
        if not ObjectId.is_valid(value):
            raise ValueError("Invalid objectid")
        return ObjectId(value)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")
