from fastapi import APIRouter, Request, HTTPException
from utils.access_control import internal_only

router = APIRouter()

users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}
#internal means same machine.

@router.get("/internal/users/{user_id}", tags=["Internal"])
@internal_only
async def get_user_internal(user_id: int, request: Request):
    if user_id in users:
        return users[user_id]
    raise HTTPException(status_code=404, detail="User not found")
