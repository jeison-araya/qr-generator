"""
FastAPI app
"""
from fastapi import FastAPI
from app.url_shortener.router import router as urls_router
from app.qr_codes.router import router as qr_codes_router

app = FastAPI()

# Routers
app.include_router(urls_router)
app.include_router(qr_codes_router)
