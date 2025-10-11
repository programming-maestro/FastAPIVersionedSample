from fastapi import FastAPI, Request, HTTPException
import ipaddress

app = FastAPI()

# Mock internal data
users = {
    1: {"name": "Alice", "role": "admin"},
    2: {"name": "Bob", "role": "user"},
}


# Internal-only route
@app.get("/users/{user_id}", tags=["Public"])
def get_user_internal(user_id: int, request: Request):
    if user_id in users:
        return users[user_id]
    raise HTTPException(status_code=404, detail="User not found")


# Public route
@app.get("/internal/users", tags=["Internal"])
def list_users(request: Request):
    # Restrict to localhost
    if request.client.host != "127.0.0.1":
        raise HTTPException(status_code=403, detail="Forbidden: internal API only")
    return users
