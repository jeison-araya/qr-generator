"""
Test CRUD operations for the URL Shortener app.
"""
import pytest

from app.url_shortener import crud, schemas
from app.database.tests.test_connection import override_get_db
from . import mocks


@pytest.fixture(name="database", scope="function")
def _override_get_db():
    """Get database."""
    return override_get_db()


@pytest.mark.asyncio
async def test_create_url(database):
    """Testing generate qr code."""
    url = schemas.CreateURL(**mocks.url_mock())

    db_url = await crud.create_url(database, url=url)

    assert db_url is not None


@pytest.mark.asyncio
async def test_get_url(database):
    """Testing generate qr code."""
    url = schemas.CreateURL(**mocks.url_mock())

    db_url = await crud.create_url(database, url=url)

    assert db_url is not None

    db_url = await crud.get_url(database, key=db_url['key'], is_active=True)

    assert db_url is not None


@pytest.mark.asyncio
async def test_increment_clicks(database):
    """Testing generate qr code."""
    url = schemas.CreateURL(**mocks.url_mock())

    db_url = await crud.create_url(database, url=url)

    assert db_url is not None

    await crud.increment_clicks(database, key=db_url['key'])

    db_url = await crud.get_url(database, key=db_url['key'], is_active=True)

    assert db_url['clicks'] == 1
