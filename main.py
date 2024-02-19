from fastapi import FastAPI, HTTPException,Request, Form
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import joblib
import uvicorn
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

df = pd.read_csv("training_csv")

scaler = MinMaxScaler()
df.drop('Target',axis=1,inplace=True)
df = scaler.fit_transform(df)

# Load the pre-trained Random Forest model
model = joblib.load("covid-19 model.pkl")



class PatientData(BaseModel):
    USMER: int
    MEDICAL_UNIT: int
    SEX: int
    PATIENT_TYPE: int
    INTUBED: int
    AGE: int
    PREGNANT: int
    CLASIFFICATION_FINAL: int
    ICU: int


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/predict")
def predict(patient_data: PatientData):
    features = [patient_data.USMER, patient_data.MEDICAL_UNIT, patient_data.SEX,
                patient_data.PATIENT_TYPE, patient_data.INTUBED, patient_data.AGE,
                patient_data.PREGNANT, patient_data.CLASIFFICATION_FINAL, patient_data.ICU]

    in_array = np.array([features])
    scaled_features = scaler.transform(in_array)

    # Make predictions using your Random Forest model
    prediction = model.predict(scaled_features)[0]

    return {"prediction": "Patient In Risk" if int(prediction) == 1 else "Patient Not In Risk"}


if __name__ == "__main__":
     uvicorn.run(app, host='localhost', port=8000)
