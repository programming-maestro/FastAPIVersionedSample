from fastapi import APIRouter, Request, HTTPException
from utils.access_control import lan_only

router = APIRouter()

devices = {1: {"name": "Printer"}, 2: {"name": "Router"}}

@router.get("/lan/devices/{device_id}", tags=["LAN"])
@lan_only
async def get_device_lan(device_id: int, request: Request):
    if device_id in devices:
        return devices[device_id]
    raise HTTPException(status_code=404, detail="Device not found")
