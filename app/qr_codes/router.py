"""Router for the qr codes app."""
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks


from app.database.connection import get_db
from app.qr_codes.schemas import CreateQR
from app.qr_codes import service, crud

router = APIRouter(prefix='/qr_codes', tags=['QR Codes'])


@router.post("/", status_code=201)
async def generate_qr_code(
    create_qr: CreateQR,
    background_job: BackgroundTasks,
    database=Depends(get_db)
):
    """
    # Generate QR code.

    ## Parameters:
        - create_qr: CreateQR: Create QR code schema.

    ## Returns:
        - FileResponse: QR code image.
    """
    file_path = service.generate_qr_code(
        url=create_qr.url,
        dark_color=create_qr.dark_color,
        light_color=create_qr.light_color,
        scale=create_qr.scale
    )

    await crud.create_qr_code(database, create_qr)

    background_job.add_task(service.clear_qr_codes_folder)

    return FileResponse(file_path, status_code=201)
