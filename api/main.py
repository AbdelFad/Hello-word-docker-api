from typing import Optional

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{name}")
def read_item(name: str, q: Optional[str] = None):
    return {"text": f"Hello {name} nice to meet you"}