import streamlit as st
import requests

st.title("🐶 Dog Breed Classifier")

file = st.file_uploader("Upload an image", type=["jpg", "png"])

if file:
    st.image(file, caption="Uploaded Image")

    if st.button("Predict"):
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            files={"file": file.getvalue()}
        )

        prediction = response.json()["prediction"]
        st.success(f"Prediction: {prediction}")