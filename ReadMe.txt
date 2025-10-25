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

    Why -p 8000:8000 is needed
        Docker containers have their own network isolated from your host machine.
        Even if FastAPI is running on port 8000 inside the container, your host cannot see it unless you explicitly map the ports.

    The -p host_port(personal computer in our case):container_port syntax does this mapping:
        container_port = 8000 → where FastAPI is listening inside the container.
        host_port = 8000 → where your computer will forward traffic to the container.

        Your Computer (localhost:8000)
                │
                ▼
        Docker Port Mapping (-p 8000:8000)
                │
                ▼
        Container (0.0.0.0:8000) → FastAPI (Uvicorn)

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
    - Implemeented
    - FYI, Currently we are passing container count at runtime, same can be fixed on the docker-compose.yml file.

    Commands:
        Start:              docker compose up --build -d --scale fastapi-app=3
        Delete Container:   docker-compose down -v
        Delete Image:       docker system prune -af

    URL:        http://localhost:8090/whoami
    Dashboard:  http://localhost:8091/dashboard

------------------------------------------------------------------------------------------------------------------------
Kubernetes
------------------------------------------------------------------------------------------------------------------------
(No need to execute any commands from Dockerization, ensure docker desktop is up and running)
Step 1: Create a kind cluster
    kind create cluster --name fastapi-cluster --config ./k8s/kind-config.yaml

Step 2: Build your Docker image for kind
    docker build -t fastapi-app:latest .
    kind load docker-image fastapi-app:latest --name fastapi-cluster

Step 3: Create Kubernetes Deployment
    Created a file deployment.yaml under k8s folder.

Step 4: Expose Deployment with Service
    Created service.yaml under k8s folder.

Step 5: Apply Deployment and Service
    kubectl apply -f ./k8s/deployment.yaml
    kubectl apply -f ./k8s/service.yaml

    Check pods:
        kubectl get pods
        kubectl get svc

Step 6: Test your app/endpoints
    Test the endpoint: http://localhost:30001/temp

------------------------------------------------------------------------------------------------------------------------
Kubernetes: Enable Metrics Server (Required for Autoscaling) Horizontal Pod Autoscaler (HPA)
------------------------------------------------------------------------------------------------------------------------

Step 7: HPA requires metrics. Install metrics-server in your cluster:
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

Step 8: Verify metrics-server is running
    kubectl get deployment metrics-server -n kube-system
    kubectl get pods -n kube-system

    Test metrics API
        kubectl top nodes
        kubectl top pods

    # Allow insecure TLS (bypass kubelet cert validation)
        kubectl patch deployment metrics-server -n kube-system --type="json" -p="[{'op':'add','path':'/spec/template/spec/containers/0/args/-','value':'--kubelet-insecure-tls'}]"

    # Prefer internal IPs for scraping (helps in containerized environments like Kind)
        kubectl patch deployment metrics-server -n kube-system --type="json" -p="[{'op':'add','path':'/spec/template/spec/containers/0/args/-','value':'--kubelet-preferred-address-types=InternalIP,Hostname,ExternalIP'}]"

    Then restart the deployment:
        kubectl rollout restart deployment metrics-server -n kube-system

    After a few seconds, confirm it’s running:
        kubectl get pods -n kube-system

    kubectl top nodes
    kubectl top pods -A

Step 9: Create Horizontal Pod Autoscaler (HPA)
    Created hpa.yaml under k8s folder.

Step 10: Apply it
    kubectl apply -f ./k8s/hpa.yaml

    Check:
        kubectl get hpa

------------------------------------------------------------------------------------------------------------------------
Test AutoScaling
------------------------------------------------------------------------------------------------------------------------
You can generate load using hey or ab or even Python:

# Install hey if not available
    Download from https://github.com/rakyll/hey
        https://hey-release.s3.us-east-2.amazonaws.com/hey_windows_amd64
        hey_windows_amd64 will be downloaded
        rename with extension, .ext ->  hey_windows_amd64.exe

# Send load
    hey -z 60s -c 20 http://localhost:30001/temp

Check HPA status:
    kubectl get hpa -w      [have this command run in a seperate cmd prompt so that you see live update on pod creation and deletion.]
    kubectl get pods
    kubectl top pod
    kubectl top nodes

For testing auto - scaling, I had the CPU utilization to 2%.
    - Validated the maxpod increase from 1 to 7
    - For scaling down, post stopping the traffic, viz in our case 'hey' command.
        - Each pod will monitor for 5 for CPU utilization, before deleting that pod.
        - Alternately we can
            1. This temporarily sets replicas to 1 [After auto scaling], which will delete all pods
                kubectl scale deployment fastapi-deployment --replicas=1

            2. You can delete and re-apply HPA (less recommended):
                here update CPU utilization from 2 to more like 5% under hpa.yaml, 50% then run the following command.
                    kubectl delete hpa fastapi-hpa
                    kubectl apply -f hpa.yaml
            3. - update CPU utilization from 2 to more like 5% under hpa.yaml
               - kubectl apply -f hpa.yaml
               - Then each pod will take 5min, to ensure minimum pod utilization is below set target, viz 5%. before deleting itself.

Note: 2% cpu or 5% is for testing auto scaling.

I tried "hey -z 10s -c 2000 http://localhost:30001/temp" and things fall apart, nodes got created to max, but later no request will fulfilling, coz
    Why your requests fail
        1. Kind networking on Windows is limited
            NodePort (30001) goes through Docker’s NAT/bridge
            Windows + Docker Desktop has low max TCP connections for containers (usually 1500 rps/tps)
            High concurrency (-c 2000) easily saturates the NodePort → connections fail
        2. FastAPI concurrency inside pod is limited by OS / TCP sockets
            With 1 worker, pod can’t handle thousands of concurrent connections on Windows + Kind
        3. Resource starvation in Kind
            Default Kind cluster on Windows often has 1–2 CPUs
            HPA may scale pods, but host cannot schedule all connections quickly enough

Extra Notes for Windows + Kind:

    Docker Desktop on Windows has network limits. NodePort > 1500-2000 concurrent connections may fail.

    For very high concurrency testing, consider minikube on Linux VM or local microk8s.
------------------------------------------------------------------------------------------------------------------------
Clean Up
------------------------------------------------------------------------------------------------------------------------
kind delete cluster --name fastapi-cluster
docker image rm fastapi-app:latest

------------------------------------------------------------------------------------------------------------------------
Clean Up: All
------------------------------------------------------------------------------------------------------------------------
Delete Kind cluster
    kind delete cluster --name fastapi-cluster

Delete all Kubernetes resources
    # Delete all workloads in all namespaces
    kubectl delete all --all --all-namespaces

    # Delete all configmaps and secrets (optional but thorough)
    kubectl delete configmap --all --all-namespaces
    kubectl delete secret --all --all-namespaces

Delete all Kind clusters
    # List all Kind clusters and delete each one
    kind get clusters | ForEach-Object { kind delete cluster --name $_ }

Clean up Docker containers, images, networks, and volumes
    # Stop all running containers
    docker ps -q | ForEach-Object { docker stop $_ }

    # Remove all containers
    docker ps -aq | ForEach-Object { docker rm $_ }

    # Remove all images
    docker images -q | ForEach-Object { docker rmi $_ -f }

    # Remove all volumes
    docker volume ls -q | ForEach-Object { docker volume rm $_ }

    # Remove all networks not used by default
    docker network ls -q | ForEach-Object { docker network rm $_ }