"""
CRUD operations for URL shortener
"""
from app.url_shortener.schemas import CreateURL, URL
from app.util import jsonable_encoder


COLLECTION_NAME = 'urls'


async def create_url(database, url: CreateURL):
    """
    # Create url.

    ## Parameters:
        - create_url: CreateURL: Create url schema.

    ## Returns:
        - Url: Url schema.
    """
    url = await database[COLLECTION_NAME].insert_one(jsonable_encoder(url))

    return await database[COLLECTION_NAME].find_one({'_id': url.inserted_id})


async def get_url(database, key: str, is_active: bool) -> URL:
    """
    Get url.

    ## Parameters:
        - url_key: str: Url key.
        - is_active: bool: Url is active.

    ## Returns:
        - Url: Url schema.
    """
    return await database[COLLECTION_NAME].find_one(
        {'key': key, 'is_active': is_active}
    )


async def increment_clicks(database, key: str):
    """
    Increment clicks.

    ## Parameters:
        - url_key: str: Url key.

    ## Returns:
        - None
    """
    await database[COLLECTION_NAME].update_one(
        {'key': key}, {'$inc': {'clicks': 1}})
