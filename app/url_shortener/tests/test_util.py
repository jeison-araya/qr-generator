"""
Test the utility functions.
"""
import pytest

from app.url_shortener.util import generate_key


def test_generate_key():
    """
    Test generate key.
    """
    key = generate_key(length=8)
    assert len(key) == 8
    assert key.isalnum()


def test_generate_key_with_length_0():
    """
    Test generate key with length 0.
    """
    with pytest.raises(ValueError):
        generate_key(length=0)
