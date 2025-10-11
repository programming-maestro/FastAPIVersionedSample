# Use official Python image
FROM python:3.13-slim

# Install git to clone repository
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set working directory inside container
WORKDIR /app

# Clone the GitHub repository
RUN git clone https://github.com/programming-maestro/FastAPIVersionedSample.git /app

# Install dependencies
# Assuming requirements.txt exists in repo root
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expose port 8000 for FastAPI
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
