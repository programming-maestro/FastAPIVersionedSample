from fastapi import FastAPI, Request, HTTPException
import ipaddress

app = FastAPI()

# Example data
devices = {
    1: {"name": "Printer", "status": "online"},
    2: {"name": "Router", "status": "offline"},
}

def is_private_ip(ip: str) -> bool:
    """Check if the IP is in a private LAN range."""
    try:
        ip_obj = ipaddress.ip_address(ip)
        return ip_obj.is_private
    except ValueError:
        return False

# LAN-only route
@app.get("/lan/devices/{device_id}", tags=["LAN"])
def get_device_lan(device_id: int, request: Request):
    if not is_private_ip(request.client.host):
        raise HTTPException(status_code=403, detail="Forbidden: LAN-only access")

    if device_id in devices:
        return devices[device_id]
    raise HTTPException(status_code=404, detail="Device not found")


# Public route
@app.get("/devices", tags=["public"])
def list_devices():
    return devices
