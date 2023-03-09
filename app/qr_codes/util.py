"""
Utility functions for QR codes.
"""
import uuid
from os import makedirs
from shutil import rmtree


def generate_file_path(folder_path: str) -> str:
    """
    Generate a file path for a QR code.
    """
    file_name = uuid.uuid4().hex

    return f'{folder_path}/{file_name}.png'


def clear_folder(folder_path: str):
    """
    Clear a folder.
    """
    rmtree(folder_path, ignore_errors=True)
    makedirs(folder_path, exist_ok=True)
