from fastapi import APIRouter

router = APIRouter()

users = {1: {"name": "Alice"}, 2: {"name": "Bob"}}

@router.get("/users", tags=["Public"])
def list_users():
    return users
