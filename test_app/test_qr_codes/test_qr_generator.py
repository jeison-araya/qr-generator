"""Test QR code generator."""
from os import makedirs
from os.path import exists
from shutil import rmtree

from app.qr_codes.qr_generator import QrGenerator


class TestQrGenerator():
    """
    Run tests on QR code generator.
    """
    def setup_class(self):
        """
        Setup class.
        """
        self.static_path = 'test_app/static'
        self.qr_generator = QrGenerator("test_app/static/qr_codes")

        makedirs("test_app/static/qr_codes", exist_ok=True)

    def test_generate_qr_code(self):
        """
        Test generate QR code.
        """
        file_path = self.qr_generator.generate_qr_code(
            "https://www.google.com", "#000000", "#FFFFFF", 10)

        assert exists(file_path)

    def test_generate_qr_code_with_default_values(self):
        """
        Test generate QR code with default values.
        """
        file_path = self.qr_generator.generate_qr_code(
            "https://www.google.com")

        assert exists(file_path)

    def teardown_class(self):
        """
        Teardown class.
        """
        rmtree('test_app/static')

