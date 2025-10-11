from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v2", tags=["Upload v2"])

class UploadDataV2(BaseModel):
    name: str
    value: float
    unit: str

@router.post("/upload")
async def upload_v2(data: UploadDataV2):
    return {
        "message": f"Received data for {data.name} ({data.unit})",
        "value": data.value,
        "status": "success"
    }
