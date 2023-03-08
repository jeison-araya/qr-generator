"""
FastAPI app
"""
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks
from fastapi.encoders import jsonable_encoder

from app.database import get_db
from app.qr_codes.qr_generator import QrGenerator
from app.schemas.create_qr import CreateQR

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

qr_generator = QrGenerator("app/static/qrcodes")


@app.post("/qr/", status_code=201)
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
    file_path = qr_generator.generate_qr_code(
        create_qr.url, create_qr.dark_color, create_qr.light_color, create_qr.scale)

    await database['qr_codes'].insert_one(jsonable_encoder(create_qr))

    background_job.add_task(qr_generator.clear_qr_codes)

    return FileResponse(file_path, status_code=201)
