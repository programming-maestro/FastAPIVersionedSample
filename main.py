from fastapi import FastAPI
from routes import (
    legacy_routers,
    v1_routers,
    v2_routers,
    v3_routers,
    public_routers,
    internal_routers,
    lan_routers,
)

app = FastAPI(title="Multi-Version Modular FastAPI with Access Control")

for router in (
    legacy_routers
    + v1_routers
    + v2_routers
    + v3_routers
    + public_routers
    + internal_routers
    + lan_routers
):
    app.include_router(router)
