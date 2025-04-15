from typing import Union

from fastapi import FastAPI
from dbconnection import DbConnection

app = FastAPI()
db = DbConnection()

@app.get("/")
def read_root():
    return {"Count": db.increase_counter()}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}