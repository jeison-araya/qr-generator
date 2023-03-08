"""Testing create qr schema."""
import pytest

from app.schemas.create_qr import CreateQR
from app.tests.test_schemas import fake_create_qr


class TestCreateQr():
    """Testing create qr schema."""

    def test_create_qr(self, create_qr_json):
        """Testing create qr schema."""
        create_qr = CreateQR(**create_qr_json)

        assert create_qr.url == create_qr_json['url']
        assert create_qr.dark_color == create_qr_json['dark_color']
        assert create_qr.light_color == create_qr_json['light_color']
        assert create_qr.scale == create_qr_json['scale']

    @pytest.mark.parametrize("dark_color", [
        '000000', '#0000000', '#GGGGGG', '#000'
    ])
    def test_create_qr_with_invalid_dark_color(self, create_qr_json, dark_color):
        """Testing create qr schema with invalid dark color."""
        json = create_qr_json
        json['dark_color'] = dark_color

        with pytest.raises(ValueError):
            CreateQR(**json)

    @pytest.mark.parametrize("light_color", [
        'FFFFFF', '#FFFFFFF', '#GGGGGG', '#FFF'
    ])
    def test_create_qr_with_invalid_light_color(self, create_qr_json, light_color):
        """Testing create qr schema with invalid light color."""
        json = create_qr_json
        json['light_color'] = light_color

        with pytest.raises(ValueError):
            CreateQR(**json)

    @pytest.mark.parametrize("scale", [5, 41])
    def test_create_qr_with_invalid_scale(self, create_qr_json, scale):
        """Testing create qr schema with invalid scale."""
        json = create_qr_json
        json['scale'] = scale

        with pytest.raises(ValueError):
            CreateQR(**json)


@pytest.fixture(name='create_qr_json')
def _create_qr_json():
    """Create fake create qr schema."""
    return fake_create_qr.build_json()
