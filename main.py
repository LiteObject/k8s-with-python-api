import json
import logging
from fastapi import Depends, FastAPI, Request
import os
import time
import gc
import logging_setup as ls;

app = FastAPI(
    openapi=True,
    docs_url="/apidocs",
    openapi_title="My Awesome Fast API",
    openapi_description="This is a description of my awesome Fast API.",
    openapi_version="0.0.1",
    openapi_tags=[
        {"name": "tests", "description": "Test-related endpoints"},
        {"name": "products", "description": "Product-related endpoints"},
    ],
)

logger = ls.logger

@app.get("/")
def read_root(request: Request, logger: logging.Logger = Depends(lambda: logger)):
    logger.info(f"Request received: {request.url.path}")
    return {"Message": "Hello World!"}

@app.get("/items/{item_id}", tags=["products"])
def read_item(item_id: int, request: Request, logger: logging.Logger = Depends(lambda: logger)):
    logger.info(f"Received request for item_id: {item_id}, path: {request.url.path}")    
    return {"item_id": item_id}

@app.get("/crash", tags=["tests"])
def crash_loop():
    while True:
        try:
            # Simulate a crash
            os._exit(1)
        except Exception as e:
            print(f"Crashing: {e}")

@app.get("/memory-leak/", tags=["tests"])
def create_memory_leak():
    # Create a large dictionary to occupy memory
    big_dict = {"x": [i for i in range(100000)]}

    # Don't release the reference!
    gc.collect()  # This won't help, actually makes it worse

    return {"message": "Memory leak created!"}
