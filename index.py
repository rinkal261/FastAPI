from fastapi import FastAPI

app = FastAPI()

@app.get("/predict")
def predict_model(age:int , gender:str):

    if age<20 or gender == 'F':
        return {'survived' : 1}
    else:
        return{'survived' : 0}