"""Testing the main module."""
from fastapi.testclient import TestClient

from app.main import app
from app.tests.test_schemas import fake_create_qr

client = TestClient(app)


class TestMain():
    """Testing the main module."""

    def test_generate_qr_code(self):
        """Testing generate qr code."""
        json = fake_create_qr.build_json()

        response = client.post("/qr/", json=json)

        assert response.status_code == 201

    def test_generate_qr_code_with_invalid_dark_color(self):
        """Testing generate qr code with invalid dark color."""
        json = fake_create_qr.build_json()
        json['dark_color'] = "000000"

        response = client.post("/qr/", json=json)

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

    def test_generate_qr_code_with_invalid_light_color(self):
        """Testing generate qr code with invalid light color."""
        json = fake_create_qr.build_json()
        json['light_color'] = "FFFFFF"

        response = client.post("/qr/", json=json)

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

    def test_generate_qr_code_with_invalid_scale(self):
        """Testing generate qr code with invalid scale."""
        json = fake_create_qr.build_json()
        json['scale'] = 5

        response = client.post("/qr/", json=json)

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
