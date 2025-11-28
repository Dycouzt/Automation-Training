# FAST API Practice Script in Python.
# To run this server, use the command: uvicorn SysOps.fast_api:app --reload
# If running from the directory containing fast_api.py: uvicorn fast_api:app --reload

from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of the FastAPI class
app = FastAPI()

# --- 1. Basic GET Endpoint ---
# This decorator tells FastAPI that the function below corresponds to the
# path "/" with an operation "get".
@app.get("/")
def read_root():
    """
    Root endpoint that returns a simple JSON response.
    """
    return {"Hello": "World"}

# --- 2. Path Parameters ---
# You can declare path parameters with the same syntax used by Python format strings.
# In this example, 'item_id' is passed as an argument to the function.
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """
    Endpoint demonstrating path parameters.
    - item_id: captured from the URL path.
    - q: an optional query parameter (explained below).
    """
    return {"item_id": item_id, "q": q}

# --- 3. Query Parameters ---
# When you declare other function parameters that are not part of the path parameters,
# they are automatically interpreted as "query" parameters.
# Example URL: /users/?skip=0&limit=10
@app.get("/users/")
def read_users(skip: int = 0, limit: int = 10):
    """
    Endpoint demonstrating query parameters with default values.
    - skip: defaults to 0
    - limit: defaults to 10
    """
    fake_users_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
    return fake_users_db[skip : skip + limit]

# --- 4. Request Body with Pydantic ---
# To declare a request body, you use Pydantic models with all their power and benefits.
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post("/items/")
def create_item(item: Item):
    """
    Endpoint demonstrating how to receive a request body.
    FastAPI will:
    - Read the body as JSON.
    - Convert the corresponding types (if needed).
    - Validate the data.
    - Give you the data in the parameter `item`.
    """
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
