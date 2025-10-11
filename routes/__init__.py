from routes.v1 import temp as temp_v1, upload as upload_v1
from routes.v2 import temp as temp_v2, upload as upload_v2
from routes.v3 import temp as temp_v3, upload as upload_v3

# Import new internal/LAN routers
from routes.internal import internal_routes
from routes.lan import lan_routes
from routes.public import public_routes

legacy_routers = [temp_v1.legacy_router]
v1_routers = [temp_v1.v1_router, upload_v1.router]
v2_routers = [temp_v2.router, upload_v2.router]
v3_routers = [temp_v3.router, upload_v3.router]

internal_routers = [internal_routes.router]  # Internal-only routes
lan_routers = [lan_routes.router]            # LAN-only routes
public_routers = [public_routes.router]      # Public routes
