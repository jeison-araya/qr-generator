"""
FastAPI app
"""
from os import remove

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.background import BackgroundTasks

from app.qr_codes.qr_generator import QrGenerator
from app.schemas.create_qr import CreateQR

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

qr_generator = QrGenerator("app/static/qrcodes")


@app.post("/qr/", status_code=201)
async def generate_qr_code(
    create_qr: CreateQR,
    background_job: BackgroundTasks
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

    background_job.add_task(remove, file_path)

    return FileResponse(file_path, status_code=201)
