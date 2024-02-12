from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB : List[Person] = [
    Person(id=1, name="Tina", age=18),
    Person(id=2, name="Gene", age=15),
    Person(id=3, name="Louise", age=16)
]
@app.get("/api")
def read_root():
    return DB


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}