from fastapi import FastAPI
from app.models.PredictData import PredictData

app = FastAPI()


@app.post("/predict/")
async def predict(input_data: PredictData):
    return {"Predict Data": input_data.dict()}
