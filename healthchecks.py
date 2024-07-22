# healthchecks.py

from fastapi import APIRouter, FastAPI, HTTPException, Request
import logging
import httpx
import psutil

router = APIRouter()

logger = logging.getLogger(__name__)

# config = {
#     "user": "your_username",
#     "password": "your_password",
#     "host": "your_host",
#     "database": "your_database"
# }

@router.get("/healthcheck", tags=["healthchecks"])
def healthcheck(request: Request):
    logger.info(f"Request received: {request.url.path}")
    return {"status": "healthy", "message": "Application is up and running."}

# @app.get("/healthcheck/db", tags=["healthchecks"])
# def db_healthcheck():
#     try:
#         conn = mysql.connector.connect(**config)
#         return {"status": "connected", "database_name": config["database"]}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

@router.get("/healthcheck/services", tags=["healthchecks"])
async def services_healthcheck():
    services = []
    async with httpx.AsyncClient() as client:
        try:
            api_response = await client.get("https://api.example.com/healthcheck")
            services.append({"name": "API", "status": "available" if api_response.status_code == 200 else "unavailable"})
            
            queue_response = await client.get("https://queue.example.com/healthcheck")
            services.append({"name": "Queue", "status": "available" if queue_response.status_code == 200 else "unavailable"})
        except httpx.HTTPStatusError as e:
            logger.error("Service check failed", exc_info=True)
            raise HTTPException(status_code=500, detail=str(e))
    
    return {"services": services}


@router.get("/healthcheck/metrics", tags=["healthchecks"])
def metrics_healthcheck():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    response_time = 100

    return {"cpu_usage": cpu_usage, "memory_usage": memory_usage, "response_time": response_time}

@router.get("/healthcheck/liveness", tags=["healthchecks"])
def liveness_healthcheck():
    return "I'm alive!"

@router.get("/healthcheck/readiness", tags=["healthchecks"])
def readiness_healthcheck():
    try:
        # Check if the application is ready to accept requests
        if 1:  # Replace with your readiness check logic
            return "I'm ready!"
        else:
            raise HTTPException(status_code=503, detail="Application not ready")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/healthcheck/memory", tags=["healthchecks"])
def memory_healthcheck():
    memory_usage = psutil.virtual_memory().percent
    available_memory = psutil.virtual_memory().available / (1024.0 **3)

    return {"memory_usage": memory_usage, "available_memory": available_memory}
