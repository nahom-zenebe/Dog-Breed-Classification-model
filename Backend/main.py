from fastapi import FastAPI, File, UploadFile
from PIL import Image
import io
from utils import predict

app = FastAPI(title="Dog Classifier API", description="API for classifying dog breeds", version="1.0")

@app.get("/")
def root():
    return {"message": "Dog Classifier API"}

@app.post("/predict")
async def predict_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    result = predict(image)

    return {"prediction": result}