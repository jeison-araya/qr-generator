from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.qr_codes.qr_generator import QrGenerator


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

qr_generator = QrGenerator("app/static/qrcodes")


@app.post("/qr/", status_code=201)
async def generate_qr_code(
    url: str,
    file_name: str,
    dark_color: str = None,
    light_color: str = None,
    scale: int = None
):
    file_path = qr_generator.generate_qr_code(url, file_name, dark_color, light_color, scale)
    
    return FileResponse(file_path, status_code=201)
