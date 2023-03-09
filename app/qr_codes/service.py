"""Module to generate QR codes."""
import segno

from app.qr_codes.util import generate_file_path, clear_folder

FOLDER_PATH = 'app/static/qr_codes'
DEFAULT_DARK_COLOR = '#000000'
DEFAULT_LIGHT_COLOR = '#FFFFFF'
DEFAULT_SCALE = 10


def clear_qr_codes_folder():
    """
    Clear the QR codes folder.
    """
    clear_folder(folder_path=FOLDER_PATH)


def generate_qr_code(url: str,
                     dark_color: str = None,
                     light_color: str = None,
                     scale: int = None) -> str:
    """
    Generate a QR code and save it with the file_name specified.

    Args:
        url (str): The url to be encoded in the QR code.
        dark_color (str, optional): The color of the dark modules. Defaults to None.
        light_color (str, optional): The color of the light modules. Defaults to None.
        scale (int, optional): The scale of the QR code. Defaults to None.

    Returns:
        str: The file path of the QR code.
    """
    if dark_color is None:
        dark_color = DEFAULT_DARK_COLOR

    if light_color is None:
        light_color = DEFAULT_LIGHT_COLOR

    if scale is None:
        scale = DEFAULT_SCALE

    file_path = generate_file_path(folder_path=FOLDER_PATH)

    qr_code = segno.make_qr(url, error='H')
    qr_code.save(file_path, dark=dark_color,
                 light=light_color, scale=scale)

    return file_path


clear_qr_codes_folder()
