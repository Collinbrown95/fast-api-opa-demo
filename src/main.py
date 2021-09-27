from fastapi import FastAPI
from pydantic import BaseModel

from ml import MLModel
from db import DB


class InputModel(BaseModel):
    text: str


app = FastAPI()


@app.post("/predict")
async def predict(input: InputModel):
    ml_model = MLModel()
    return ml_model.predict(input.text)


@app.get("/proprietary")
async def get_proprietary(id: int):
    return DB.get_input(id, kind="proprietary")


@app.get("/beta_release")
async def get_beta_release(id: int):
    return DB.get_input(id, kind="beta_release")
