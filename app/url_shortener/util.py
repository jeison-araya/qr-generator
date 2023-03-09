"""
Utility functions for the url_shortener app.
"""
import string
import secrets


ALPHABET = string.ascii_letters + string.digits


def generate_key(length: int) -> str:
    """
    # Generate key.

    ## Parameters:
        - length: int: Length of the key.

    ## Returns:
        - str: Key.
    """
    if length < 1:
        raise ValueError('Key length must be greater than 0.')

    return ''.join(secrets.choice(ALPHABET) for _ in range(length))
