"""Test QR code generator."""
from os import listdir
from os.path import exists
from shutil import rmtree

from app.qr_codes.service import generate_qr_code, clear_qr_codes_folder, FOLDER_PATH


class TestQrCodeService:
    """
    Run tests on QR code generator.
    """

    def setup_class(self):
        """
        Setup class.
        """
        clear_qr_codes_folder()

    def test_generate_qr_code(self):
        """
        Test generate QR code.
        """
        file_path = generate_qr_code(
            url="https://www.example.com",
            dark_color="#000000",
            light_color="#FFFFFF",
            scale=10
        )

        assert exists(file_path)

    def test_generate_qr_code_with_default_values(self):
        """
        Test generate QR code with default values.
        """
        file_path = generate_qr_code("https://www.example.com")

        assert exists(file_path)

    def test_clear_qr_codes(self):
        """
        Test clear QR codes.
        """
        clear_qr_codes_folder()

        assert len(listdir(FOLDER_PATH)) == 0

    def teardown_class(self):
        """
        Teardown class.
        """
        rmtree(FOLDER_PATH)
