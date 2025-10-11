Install:
    pip install fastapi uvicorn

Local Development Testing:
    uvicorn main:app --reload

Network Testing:
    uvicorn main:app --host 0.0.0.0 --port 8000

Network Development Testing:
    uvicorn main:app --reload --host 0.0.0.0 --port 8000

------------------------------------------------------------------------------------------------------------------------
URL
------------------------------------------------------------------------------------------------------------------------
Legacy: http://127.0.0.1:8000/temp
v1: http://127.0.0.1:8000/api/v1/temp
v2: http://127.0.0.1:8000/api/v2/temp
v3: http://127.0.0.1:8000/api/v3/temp

public:     http://127.0.0.1:8000/users
lan:        http://127.0.0.1:8000/lan/devices/1
internal:   http://127.0.0.1:8000/internal/users/1

------------------------------------------------------------------------------------------------------------------------
Interactive Docs:(default by FastAPI)
------------------------------------------------------------------------------------------------------------------------
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

------------------------------------------------------------------------------------------------------------------------
INTERNAL API
------------------------------------------------------------------------------------------------------------------------
uvicorn internal_api:app --reload --host 127.0.0.1 --port 8000 [if in the root]
uvicorn routes.internal_api:app --reload --host 127.0.0.1 --port 8000
uvicorn routes.internal_api:app --reload --host 0.0.0.0 --port 8000  [allows access via LAN and deployed system ip: in windows check with ipconfig]


------------------------------------------------------------------------------------------------------------------------
LAN ONLY API
------------------------------------------------------------------------------------------------------------------------
uvicorn routes.lan_only:app --reload --host 0.0.0.0 --port 8000  [allows access via LAN and deployed system ip: in windows check with ipconfig]


------------------------------------------------------------------------------------------------------------------------
Dockerfile: How it works
------------------------------------------------------------------------------------------------------------------------
    Base image: Python 3.13 slim for small size.
    Installs git so the container can clone your repo.
    Sets working directory /app.
    Clones your GitHub repo directly into /app.
    Installs Python dependencies from requirements.txt.
    Exposes port 8000 for LAN/public access.
    Runs FastAPI using uvicorn.

------------------------------------------------------------------------------------------------------------------------
Docker Steps:
------------------------------------------------------------------------------------------------------------------------
1️⃣ Make sure your project is ready

    You have a requirements.txt file. ✅
    Your main.py is at the project root. ✅
    Your Dockerfile is in the project root (same folder as main.py). ✅

2️⃣ Build the Docker image

    Open a terminal in your project root (where the Dockerfile is) and run:

    docker build -t fastapi-sample .

        -t fastapi-sample → gives your image a name.
        The . at the end means “build from this directory”.
        You should see Docker steps run: base image, install dependencies, copy files, etc.

3️⃣ Run the Docker container

    Once the build finishes, run:

        docker run -p 8000:8000 fastapi-sample

            -p 8000:8000 maps container port 8000 → host machine port 8000.
            Your FastAPI app will now be accessible: http://localhost:8000
            Or from LAN (other devices on the network): http://<your_machine_ip>:8000

4️⃣ Test your APIs

    Check public routes, internal routes, and LAN-only routes.
    Localhost routes should work as expected (127.0.0.1).
    LAN-only routes should be accessible from devices in the same network.
    Internal-only routes should fail from LAN devices.

5️⃣ Optional: Run container in background

    docker run -d -p 8000:8000 fastapi-sample

        -d → detached mode (runs in background).
        Use docker ps to see running containers.
        Use docker logs <container_id> to check logs.

6️⃣ Update container when code changes

    Since your Dockerfile pulls code from GitHub at build time:
        1. Update your code in GitHub.
        2. Rebuild the image:

            docker build -t fastapi-sample .

        3. Stop the old container and run the new one.

Summary
    docker build -t fastapi-sample .
    docker run -d -p 8000:8000 --name my-fastapi-container fastapi-sample
    # it gives container name, viz 'my-fastapi-container'

------------------------------------------------------------------------------------------------------------------------
Docker Compose: dynamic, auto ports
------------------------------------------------------------------------------------------------------------------------
How it works

    The service is defined once.
    You can scale it at runtime, with the following command from the cmd line

        docker-compose up --build --scale fastapi-app=5
            This creates 5 containers:
                fastapi_app_1
                fastapi_app_2
                …
                fastapi_app_5
                Note: fastapi_app is the name given under docker-compose.yml --> service name, under services

            Each container exposes port 8000 internally, but Docker automatically assigns a random free host port for each container.
    Check host ports with: docker ps
Note:
    use docker-compose simple 1.yml
------------------------------------------------------------------------------------------------------------------------
Load Balancing: NGINX (Dev only)
------------------------------------------------------------------------------------------------------------------------
NGINX automatically load balances requests to all FastAPI containers.
    1. Updated the docker-compose.yml
    2. docker-compose up --build --scale fastapi-app-service=5
        This will start 5 FastAPI containers plus 1 NGINX container.
        If you change the number of FastAPI containers, that at runtime in above command, you need to update NGINX upstream list in the docker-compose.yml

    3. Testing
        hit this to get container id in response: http://localhost:8000/whoami

    Note: Stop and remove everything from previous runs to ensure no cached images are used.
        docker-compose down -v
        docker system prune -af
            This removes all stopped containers, unused images, and old volumes.
            use following: docker-compose with nginx.yml
------------------------------------------------------------------------------------------------------------------------
Load Balancing: Traefik (Prod ready)
------------------------------------------------------------------------------------------------------------------------
    Currently we are passing container count at runtime, same can be fixed on the docker-compose.yml file.
    Commands:
        Start:              docker compose up --build -d --scale fastapi-app=3
        Delete Container:   docker-compose down -v
        Delete Image:       docker system prune -af

    URL:        http://localhost:8090/whoami
    Dashboard:  http://localhost:8091/dashboard