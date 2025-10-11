import datetime
from fastapi import APIRouter

router = APIRouter(prefix="/api/v2", tags=["Temperature v2"])

@router.get("/temp2")
async def temp2_v2():
    current_datetime = datetime.datetime.now()
    return {
        "datetime": current_datetime.isoformat(),
        "message": "This is /api/v2/temp2 endpoint with improved format"
    }

@router.get("/temp")
async def temp2_v2():
    current_datetime = datetime.datetime.now()
    return {
        "datetime": current_datetime.isoformat(),
        "message": "This is /api/v2/temp endpoint with improved format"
    }
