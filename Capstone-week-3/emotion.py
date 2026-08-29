import joblib
MODEL_PATH = "models/emotion_model.pkl"
VECTORIZER_PATH = "models/tfidf_vectorizer.pkl"

model = joblib.load(MODEL_PATH)

vectorizer = joblib.load(VECTORIZER_PATH)

LABEL_NAMES = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise",
}

def predict_emotion(text):
    text_vector = vectorizer.transform([text])
    
    label_id = model.predict(text_vector)[0]
    
    return {
        "label_id": int(label_id),
        "emotions": LABEL_NAMES[int(label_id)]
    }

