"""Module to generate QR codes."""
import os
import uuid
import segno
from PIL import Image


class QrGenerator:
    def __init__(self, folder_path: str,
                 default_dark_color: str = None,
                 default_light_color: str = None,
                 default_scale: int = 10) -> None:
        self._folder_path = self._mkdir_if_no_exists(folder_path)
        self._default_dark_color = default_dark_color or "black"
        self._default_light_color = default_light_color or "white"
        self._default_scale = default_scale

    def generate_qr_code(self, url: str,
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
            str: The path to the generated QR code.
        """
        if dark_color is None:
            dark_color = self._default_dark_color

        if light_color is None:
            light_color = self._default_light_color

        if scale is None:
            scale = self._default_scale

        file_path = self._generate_file_path()

        qr = segno.make_qr(url, error='H')
        qr.save(file_path, dark=dark_color, light=light_color, scale=scale)
        self._add_logo(file_path, 'app\static\images\logo.png')
        return file_path

    def _add_logo(self, file_path: str, logo_path: str):
        qr_img = Image.open(file_path).convert("RGBA")
        logo_img = Image.open(logo_path)

        box = self.__get_logo_box(qr_img.size, logo_img.size)
        qr_img.crop(box)

        region = logo_img.resize((box[2] - box[0], box[3] - box[1]))

        # set background color to logo
        background = Image.new('RGB', region.size, (255, 255, 255))
        background.paste(region, region)

        qr_img.paste(background, box)
        qr_img.save(file_path)

    def __get_logo_box(self, qr_size: dict, logo_size):
        qr_w, qr_h = qr_size
        logo_w, logo_h = logo_size

        A = int(qr_w / 2 - logo_w / 2)
        B = int(qr_h / 2 - logo_h / 2)
        C = int(qr_w / 2 + logo_w / 2)
        D = int(qr_h / 2 + logo_h / 2)

        return (A, B, C, D)

    def _generate_file_path(self) -> str:
        file_name = uuid.uuid4().hex

        return f'{self._folder_path}/{file_name}.png'

    def _mkdir_if_no_exists(self, path: str) -> str:
        try:
            os.mkdir(path)
        except FileExistsError:
            print(f'Folder {path} already exists.')
        finally:
            return path
