import datetime
from fastapi import APIRouter

# Router for versioned endpoints
v1_router = APIRouter(prefix="/api/v1", tags=["Date Time v1"])

# Router for legacy endpoints (old clients)
legacy_router = APIRouter(tags=["Time Legacy"])

# Legacy endpoint (no prefix)
@legacy_router.get("/temp")
async def temp_legacy():
    current_time = datetime.datetime.now().time()
    return {"time": current_time.isoformat()}




# Versioned endpoint
@v1_router.get("/temp")
async def temp_v1():
    current_time = datetime.datetime.now().time()
    return {"time": current_time.isoformat()}

@v1_router.get("/temp2")
async def temp2_v1():
    current_datetime = datetime.datetime.now()
    return {
        "date": current_datetime.date().isoformat(),
        "time": current_datetime.time().isoformat(),
        "message": "This is /api/v1/temp2 endpoint"
    }
