from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()

# HW2 - test1
@app.get("/")
async def root():
    return {
            "message": "Hello World"
            }


# HW2 - test2
@app.put("/items/{item_id}")
async def read_item(item_id : int, q : str|None = None) :
    results = {
        "item_id": item_id,
        "name": "Test Item",
        "description": "A test description",
        "price": 10.5,
        "tax": 1.5
    }
    if q:
        results.update({"q":q})
    return results


# HW3 - test1
@app.get("/items/{item_id}")
async def read_item(item_id: Annotated[int, Path(ge=1, le=1000)], q: Annotated[str | None, Query(max_length=50, min_length=3)] = None, sort_order: str | None = "asc"):
    if q:
        description = f"This is a sample item that matches the query {q}."
    else:
        description = "This is a sample item."
    
    results = { 
        "item_id": item_id,
        "description": description,
        "sort_order": sort_order
    }
    return results

# HW3 - test12
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float

@app.put("/items/{item_id}")
async def update_item(item_id: Annotated[int, Path(ge=1, le=1000)],item: Item, q: Annotated[str | None, Query(max_length=50, min_length=3)] = None):
    results = {
        "item_id": item_id,
        **item.dict()
    }
    if q:
        results.update({"q": q})

    return results

