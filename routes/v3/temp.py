import datetime
from fastapi import APIRouter

router = APIRouter(prefix="/api/v3", tags=["Temperature v3"])

@router.get("/temp2")
async def temp2_v3():
    current_datetime = datetime.datetime.now()
    return {
        "datetime": current_datetime.isoformat(),
        "message": "This is /api/v3/temp2 endpoint with additional metadata",
        "metadata": {
            "source": "v3 service",
            "timestamp": current_datetime.timestamp()
        }
    }
