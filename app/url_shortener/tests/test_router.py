"""
Test the router
"""
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database.connection import get_db
from app.database.tests.test_connection import override_get_db
from . import mocks


@pytest.fixture(name="client", scope="function")
def _client():
    """Client."""
    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as client:
        yield client


def test_create_url(client: TestClient):
    """Testing generate qr code."""
    json = mocks.url_mock()

    response = client.post("/urls/", json=json)

    assert response.status_code == 201



@pytest.mark.asyncio
async def test_forward_to_target_url(client: TestClient):
    """Testing generate qr code."""

    json = mocks.url_mock()

    response = client.post("/urls/", json=json)

    assert response.status_code == 201

    response = client.get(f"/urls/{response.json()['key']}", follow_redirects=False)

    assert response.status_code == 307



def test_forward_to_target_url_not_found(client: TestClient):
    """Testing generate qr code."""
    response = client.get("/urls/123")

    assert response.status_code == 404

    json = response.json()

    assert json['detail'] == "URL 'http://testserver/urls/123' doesn't exist"
