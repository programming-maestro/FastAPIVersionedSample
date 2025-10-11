Install:
    pip install fastapi uvicorn

Local Development Testing:
    uvicorn main:app --reload

Network Testing:
    uvicorn main:app --host 0.0.0.0 --port 8000

Network Development Testing:
    uvicorn main:app --reload --host 0.0.0.0 --port 8000

URL:
Legacy: http://127.0.0.1:8000/temp
v1: http://127.0.0.1:8000/api/v1/temp
v2: http://127.0.0.1:8000/api/v2/temp
v3: http://127.0.0.1:8000/api/v3/temp

Interactive Docs:(default by FastAPI)
    Swagger: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc


Post Curl Request:
Legacy:
curl -X POST "http://127.0.0.1:8000/upload"  -H "Content-Type: application/json" -d "{\"name\": \"sensor1\", \"value\": 42.8}"

v1:
curl -X POST "http://127.0.0.1:8000/api/v1/upload"  -H "Content-Type: application/json" -d "{\"name\": \"sensor1\", \"value\": 42.8}"

v2:
curl -X POST "http://127.0.0.1:8000/api/v2/upload"  -H "Content-Type: application/json" -d "{\"name\": \"Chetan\", \"value\": 6, \"unit\": \"5F 8in\"}"

v3:
curl -X POST "http://127.0.0.1:8000/api/v3/upload"  -H "Content-Type: application/json" -d "{\"name\": \"Don\", \"value\": 786}"

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
INTERNAL API
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
uvicorn internal_api:app --reload --host 127.0.0.1 --port 8000 [if in the root]
uvicorn routes.internal_api:app --reload --host 127.0.0.1 --port 8000
uvicorn routes.internal_api:app --reload --host 0.0.0.0 --port 8000  [allows access via LAN and deployed system ip: in windows check with ipconfig]


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
LAN ONLY API
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
uvicorn routes.lan_only:app --reload --host 0.0.0.0 --port 8000  [allows access via LAN and deployed system ip: in windows check with ipconfig]
