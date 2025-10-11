from fastapi import APIRouter
import socket

router = APIRouter()

users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}

@router.get("/users", tags=["Public"])
def list_users():
    return users

@router.get("/whoami", tags=["Public"])
def whoami():
    """
    Returns container hostname to identify which instance handled the request.
    """
    hostname = socket.gethostname()
    return {"container_id": hostname}
