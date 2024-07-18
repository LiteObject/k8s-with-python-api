# Start with a base image containing Python runtime
FROM python:3.8

# Add Maintainer Info
LABEL maintainer="lite.object@gmail.com"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies and copy source code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Run main.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
