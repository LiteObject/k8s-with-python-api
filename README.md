# FastAPI Simple Application Setup Guide

This guide will help you set up and run the FastAPI simple application.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup Steps

1. Clone the repository:

2. Create a virtual environment (optional but recommended):
   ```
   virtualenv .venv --python=python3.11 
   ```
3. Activate the virtual environment:
- On Windows:
  ```
  .venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source .venv/bin/activate
  ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```     

5. Create a file named `main.py` and copy the provided code into it.

6. Run the application:
   ```
   uvicorn main:app --reload
   ```

7. The application should now be running. You can access it at `http://127.0.0.1:8000`.

## API Endpoints

1. Root Endpoint:
- URL: `http://127.0.0.1:8000/`
- Method: GET
- Response: `{"Hello": "World"}`

2. Item Details Endpoint:
- URL: `http://127.0.0.1:8000/items/{item_id}`
- Method: GET
- Path Parameter: `item_id` (integer)
- Query Parameter: `q` (optional, string)
- Response: `{"item_id": item_id, "q": q}`

## Testing the API

You can test the API using a web browser or a tool like curl:

1. For the root endpoint:

2. For the item details endpoint:

## Development

To make changes to the application, edit the `main.py` file. The server will automatically reload when changes are detected if you used the `--reload` flag with uvicorn.

## Stopping the Application

To stop the application, press `CTRL+C` in the terminal where it's running.

