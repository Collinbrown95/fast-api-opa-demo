from fastapi import FastAPI
from pydantic import BaseModel

from ml import MLModel


class InputModel(BaseModel):
    text: str


app = FastAPI()


@app.post("/predict")
async def root(input: InputModel):
    ml_model = MLModel()
    return ml_model.predict(input.text)
