"""Router for the urls app."""
from fastapi import APIRouter, Depends, Request, HTTPException
from fastapi.responses import RedirectResponse

from app.database.connection import get_db
from app.url_shortener.schemas import CreateURL, URL
from app.url_shortener import crud

router = APIRouter(prefix='/urls', tags=['URL'])


@router.post("/", response_model=URL, status_code=201)
async def create_url(
    url: CreateURL,
    database=Depends(get_db)
):
    """
    # Create url.

    ## Parameters:
        - url: CreateURL: Create url schema.

    ## Returns:
        - Url: Url schema.
    """
    return await crud.create_url(database, url)


@router.get("/{key}")
async def forward_to_target_url(
    key: str,
    request: Request,
    database=Depends(get_db)
):
    """
    # Forward to target url.

    ## Parameters:
        - key: str: Url key.

    ## Returns:
        - RedirectResponse: Redirect to target url.

    ## Raises:
        - HTTPException: Url doesn't exist.
    """
    db_url = await crud.get_url(database, key=key, is_active=True)

    if db_url is None:
        _raise_not_found(request)

    await crud.increment_clicks(database, key=db_url['key'])
    return RedirectResponse(db_url['target_url'])


def _raise_not_found(request):
    message = f"URL '{request.url}' doesn't exist"
    raise HTTPException(status_code=404, detail=message)
