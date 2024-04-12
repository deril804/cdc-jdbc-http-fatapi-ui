from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    id: int
    name: str
    description: str
    price: float

@app.get("/parse_resume")
def read_root():
    return {"Hello": "World"}

@app.post("/items")
async def create_item(item: Item):
    return {"id": item.id, "name": item.name, "description": item.description, "price": item.price}