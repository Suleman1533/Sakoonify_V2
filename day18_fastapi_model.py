import joblib

from fastapi import FastAPI
from pydantic import BaseModel


# -----------------------------
# 1. Load the trained model
# -----------------------------

model = joblib.load("models/emotion_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


# -----------------------------
# 2. Emotion label mapping
# -----------------------------

LABEL_NAMES = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise",
}


# -----------------------------
# 3. Create FastAPI app
# -----------------------------

app = FastAPI()


# -----------------------------
# 4. Define request structure
# -----------------------------

class EmotionRequest(BaseModel):
    text: str


# -----------------------------
# 5. Prediction function
# -----------------------------

def predict_emotion(text: str):

    text_vector = vectorizer.transform([text])

    label_id = model.predict(text_vector)[0]

    emotion = LABEL_NAMES[int(label_id)]

    return {
        "label_id": int(label_id),
        "emotion": emotion,
    }


# -----------------------------
# 6. Prediction endpoint
# -----------------------------

@app.post("/predict-emotion")
def predict(request: EmotionRequest):

    result = predict_emotion(request.text)

    return result


# -----------------------------
# 7. Health check
# -----------------------------

@app.get("/")
def home():

    return {
        "message": "Sakoonify emotion API is running"
    }