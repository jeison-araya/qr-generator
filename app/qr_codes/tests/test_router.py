"""Testing the qr codes router."""
import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database.connection import get_db
from app.database.tests.test_connection import override_get_db
from . import mocks


class TestQRCodesRouter():
    """Testing the QR codes router."""

    def test_generate_qr_code(self, client: TestClient):
        """Testing generate qr code."""
        json = mocks.qr_code_mock()

        response = client.post("/qr_codes/", json=json)

        assert response.status_code == 201

    def test_generate_qr_code_with_invalid_dark_color(self, client: TestClient):
        """Testing generate qr code with invalid dark color."""
        json = mocks.qr_code_mock()
        json['dark_color'] = "000000"

        response = client.post("/qr_codes/", json=json)

        assert response.status_code == 422
        assert response.json() == {
            'detail': [
                {
                    'loc': ['body', 'dark_color'],
                    'msg': 'color must start with #',
                    'type': 'value_error'
                }
            ]
        }

    def test_generate_qr_code_with_invalid_light_color(self, client: TestClient):
        """Testing generate qr code with invalid light color."""
        json = mocks.qr_code_mock()
        json['light_color'] = "FFFFFF"

        response = client.post("/qr_codes/", json=json)

        assert response.status_code == 422
        assert response.json() == {
            'detail': [
                {
                    'loc': ['body', 'light_color'],
                    'msg': 'color must start with #',
                    'type': 'value_error'
                }
            ]
        }

    def test_generate_qr_code_with_invalid_scale(self, client: TestClient):
        """Testing generate qr code with invalid scale."""
        json = mocks.qr_code_mock()
        json['scale'] = 5

        response = client.post("/qr_codes/", json=json)

        assert response.status_code == 422
        assert response.json() == {
            'detail': [
                {
                    'loc': ['body', 'scale'],
                    'msg': 'scale must be between 6 and 40',
                    'type': 'value_error'
                }
            ]
        }


@pytest.fixture(name="client", scope="session", autouse=True)
def _client():
    """Client."""
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client
