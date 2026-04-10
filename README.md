# 🐶 Dog Breed Classifier (CNN + FastAPI + Streamlit)

A full-stack Machine Learning project that classifies dog breeds using a Convolutional Neural Network (CNN) built with PyTorch, served via FastAPI, and accessed through a Streamlit web interface.

---

## 🚀 Features

* 🧠 Deep Learning model (CNN) for image classification
* ⚡ FastAPI backend for inference
* 🎨 Streamlit frontend for user interaction
* 📷 Upload image and get prediction instantly
* 📊 (Optional) Confidence score for predictions

---

## 🏗️ Project Structure

```
dog-classifier/
│
├── backend/
│   ├── main.py          # FastAPI app
│   ├── utils.py         # Model loading & prediction
│      
│
├── frontend/
│   ├── main.py           # Streamlit UI
│--model/  
│   |-main.ipynb           #notebook
├── requirements.txt
└── README.md
```

---

## 🧠 Model Details

* Framework: PyTorch
* Architecture: Convolutional Neural Network (CNN)
* Input size: 224x224 images
* Classes: Multiple dog breeds (e.g., Husky, Labrador, Poodle, Bulldog)

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/dog-classifier.git
cd dog-classifier
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚡ Run Backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

API will run at:

```
http://127.0.0.1:8000
```

Swagger Docs:

```
http://127.0.0.1:8000/docs
```

---

## 🎨 Run Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

App will open at:

```
http://localhost:8501
```

---

## 📡 API Endpoint

### POST `/predict`

Upload an image and get prediction.

#### Request:

* Form-data: `file` (image)

#### Response:

```json
{
  "prediction": "labrador"
}
```

---

## 🧪 Example Workflow

1. Open Streamlit app
2. Upload dog image
3. Click **Predict**
4. View predicted breed

---

## 🔥 Future Improvements

* ✅ Use pretrained models (ResNet, EfficientNet)
* ✅ Add top-3 predictions
* ✅ Deploy (Render + Streamlit Cloud)
* ✅ Add Grad-CAM visualization
* ✅ Store predictions in database

---

## 🌍 Deployment

* Backend: Render / Railway
* Frontend: Streamlit Cloud

---

## 👨‍💻 Tech Stack

* Python
* PyTorch
* FastAPI
* Streamlit
* Pillow

---


⭐ If you like this project, consider giving it a star!
