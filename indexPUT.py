from fastapi import FastAPI
from pydantic import BaseModel

class Input(BaseModel):
    age : int
    gender : str

app = FastAPI()
@app.put("/predict")
def predict_model(d:Input):
    if d.age<20 or d.gender == 'F':
        return {'survived':1}
    else:
        return {'survived':0}
