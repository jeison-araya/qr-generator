"""Test py object id."""
from bson import ObjectId

import pytest

from app.schemas.py_object_id import PyObjectId


def test_py_object_id():
    """Test py object id."""
    object_id = PyObjectId(ObjectId())
    assert str(object_id) == str(object_id)

def test_py_object_id_is_valid():
    """Test py object id is valid."""
    object_id = PyObjectId(ObjectId())
    assert PyObjectId.validate(object_id) == object_id

def test_py_object_id_is_not_valid():
    """Test py object id is not valid."""
    with pytest.raises(ValueError):
        PyObjectId.validate('invalid')

def test_py_object_id_modify_schema():
    """Test py object id modify schema."""
    field_schema = {}
    PyObjectId.__modify_schema__(field_schema)
    assert field_schema == {'type': 'string'}
