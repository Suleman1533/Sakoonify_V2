import sqlite3

import joblib

from fastapi import FastAPI
from pydantic import BaseModel


# --------------------------------
# 1. Load model and vectorizer
# --------------------------------

model = joblib.load("models/emotion_model.pkl")
vectorizer = joblib.load("models/tfidf_vectorizer.pkl")


# --------------------------------
# 2. Emotion labels
# --------------------------------

LABEL_NAMES = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise",
}


# --------------------------------
# 3. Create FastAPI app
# --------------------------------

app = FastAPI()


# --------------------------------
# 4. Request schema
# --------------------------------

class ChatRequest(BaseModel):
    message: str


# --------------------------------
# 5. Initialize database
# --------------------------------

def init_db():

    conn = sqlite3.connect("sakoonify.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            message TEXT NOT NULL,
            emotion TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# --------------------------------
# 6. Predict emotion
# --------------------------------

def predict_emotion(text):

    text_vector = vectorizer.transform([text])

    label_id = model.predict(text_vector)[0]

    return {
        "label_id": int(label_id),
        "emotion": LABEL_NAMES[int(label_id)]
    }


# --------------------------------
# 7. Save message
# --------------------------------

def save_message(message, emotion):

    conn = sqlite3.connect("sakoonify.db")
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages (message, emotion)
        VALUES (?, ?)
        """,
        (message, emotion)
    )

    conn.commit()
    conn.close()


# --------------------------------
# 8. Chat endpoint
# --------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    emotion_result = predict_emotion(request.message)

    save_message(
        request.message,
        emotion_result["emotion"]
    )

    return {
        "message": request.message,
        "emotion": emotion_result,
        "reply": f"I understand that you are feeling {emotion_result['emotion']}."
    }


# --------------------------------
# 9. Start database
# --------------------------------

init_db()