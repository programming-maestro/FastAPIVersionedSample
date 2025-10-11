from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/v3", tags=["Upload v3"])

class UploadData(BaseModel):
    name: str
    value: float

@router.post("/upload")
async def upload_v3(data: UploadData):
    return {
        "message": f"Received data for {data.name}",
        "value": data.value,
        "status": "success"
    }
