from fastapi import FastAPI
import os
import time
import gc

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


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", tags=["products"])
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}


@app.get("/crash", tags=["tests"])
def crash_loop():
    while True:
        # This will cause the process to exit
        raise Exception("Crashing intentionally")


@app.get("/memory-leak/", tags=["tests"])
def create_memory_leak():
    # Create a large dictionary to occupy memory
    big_dict = {"x": [i for i in range(100000)]}

    # Don't release the reference!
    gc.collect()  # This won't help, actually makes it worse

    return {"message": "Memory leak created!"}
