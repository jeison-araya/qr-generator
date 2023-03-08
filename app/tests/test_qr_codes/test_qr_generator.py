"""Test QR code generator."""
from os import listdir
from os.path import exists
from shutil import rmtree

import pytest

from app.qr_codes.qr_generator import QrGenerator

FOLDER_PATH = "test_app/static/qr_codes"


class TestQrGenerator:
    """
    Run tests on QR code generator.
    """

    def test_generate_qr_code(self, qr_generator: QrGenerator):
        """
        Test generate QR code.
        """
        file_path = qr_generator.generate_qr_code(
            "https://www.google.com", "#000000", "#FFFFFF", 10)

        assert exists(file_path)

    def test_generate_qr_code_with_default_values(self, qr_generator: QrGenerator):
        """
        Test generate QR code with default values.
        """
        file_path = qr_generator.generate_qr_code("https://www.google.com")

        assert exists(file_path)

    def test_clear_qr_codes(self, qr_generator: QrGenerator):
        """
        Test clear QR codes.
        """
        qr_generator.clear_qr_codes()

        assert len(listdir(FOLDER_PATH)) == 0

    def teardown_class(self):
        """
        Teardown class.
        """
        rmtree(FOLDER_PATH)


@pytest.fixture(name='qr_generator')
def _qr_generator() -> QrGenerator:
    return QrGenerator(FOLDER_PATH)
