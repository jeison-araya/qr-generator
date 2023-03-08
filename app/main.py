from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.qr_codes.qr_generator import QrGenerator
from app.schemas.create_qr import CreateQR

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

qr_generator = QrGenerator("app/static/qrcodes")


@app.post("/qr/", status_code=201)
async def generate_qr_code(
    create_qr: CreateQR
):
    file_path = qr_generator.generate_qr_code(
        create_qr.url, create_qr.dark_color, create_qr.light_color, create_qr.size)

    return FileResponse(file_path, status_code=201)
