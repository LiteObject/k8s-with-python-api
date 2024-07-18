"""
This is a simple FastAPI application example.
"""
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.
    
    This endpoint will return a JSON response with the key "Hello" and the value "World".
    It does not accept any query parameters.
    """
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    """
    Item details endpoint.
    
    This endpoint will return a JSON response with the key "item_id" and its value.
    It also includes an optional query parameter "q".
    """
    return {"item_id": item_id, "q": q}
