'''
from fastapi import FastAPI
from routes.v1 import temp as temp_v1, upload as upload_v1
from routes.v2 import temp as temp_v2, upload as upload_v2


app = FastAPI(title="Versioned FastAPI Service")

# Include legacy routes (for old clients)
app.include_router(temp_v1.legacy_router)

# Include versioned routes (v1)
app.include_router(temp_v1.v1_router)
app.include_router(upload_v1.router)

# Include versioned routes (v2)
app.include_router(temp_v2.router)
app.include_router(upload_v2.router)

'''



