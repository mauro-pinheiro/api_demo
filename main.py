from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Aluno(BaseModel):
    media: float
    perc_faltas: float
    perc_disc_conc: float

class Classficador(BaseModel):
    class1: float
    class2: float

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/demo/")
async def demoGet(media: float, perc_faltas: float, perc_disc_conc: float):
    return [
        {"evasor": 0.01},
        {"nao-evasor": 0.99},
    ]


@app.post("/demo/")
async def demoPost(aluno: Aluno):
    return Classficador(0.01, 0.99)

@app.post("/items/")
async def create_item(item: Item):
    return item