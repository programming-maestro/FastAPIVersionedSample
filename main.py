from fastapi import FastAPI
from routes import v1_routers, v2_routers, v3_routers, legacy_routers

app = FastAPI(title="Multi-Version Modular FastAPI")

# Include routers
for router in legacy_routers + v1_routers + v2_routers + v3_routers :
    app.include_router(router)
