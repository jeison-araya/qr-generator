"""
CRUD operations for QR Codes
"""
from app.qr_codes.schemas import CreateQR
from app.util import jsonable_encoder

COLLECTION_NAME = 'qr_codes'


async def create_qr_code(database, qr_code: CreateQR) -> None:
    """
    # Create QR code.

    ## Parameters:
        - database: Database: Database
        - qr: CreateQR: Create QR code schema.

    ## Returns:
        - CreateQR: Create QR code schema.

    """
    await database[COLLECTION_NAME].insert_one(jsonable_encoder(qr_code))
