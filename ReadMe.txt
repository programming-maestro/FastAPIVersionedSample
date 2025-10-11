pip install fastapi uvicorn

uvicorn main:app --reload
uvicorn main:app --host 0.0.0.0 --port 8000


http://127.0.0.1:8000/temp

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

{
  "name": "Chetan",
  "value": 6,
  "unit": "5F 8In"
}