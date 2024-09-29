from fastapi import FastAPI

app = FastAPI()

# HW2 - test1
@app.get("/")
async def root():
    return {
            "message": "Hello World"
            }


# HW2 - test2
@app.get("/items/{item_id}")
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