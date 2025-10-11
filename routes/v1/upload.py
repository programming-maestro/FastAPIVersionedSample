# routes/upload.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1", tags=["Upload"])

class UploadData(BaseModel):
    name: str
    value: float

@router.post("/upload")
async def upload_data(data: UploadData):
    return {
        "message": f"Received data for {data.name}",
        "value": data.value,
        "status": "success"
    }
