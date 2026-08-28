from datasets import load_dataset

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

import mlflow
import mlflow.sklearn

import joblib
import os


# -----------------------------
# 1. Load dataset
# -----------------------------

dataset = load_dataset("dair-ai/emotion")

train_data = dataset["train"]
test_data = dataset["test"]

X_train = train_data["text"]
y_train = train_data["label"]

X_test = test_data["text"]
y_test = test_data["label"]


# -----------------------------
# 2. TF-IDF
# -----------------------------

vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# -----------------------------
# 3. Train model
# -----------------------------

model = LogisticRegression(
    max_iter=1000
)

model.fit(X_train_tfidf, y_train)


# -----------------------------
# 4. Evaluate
# -----------------------------

predictions = model.predict(X_test_tfidf)

accuracy = accuracy_score(
    y_test,
    predictions
)

matrix = confusion_matrix(
    y_test,
    predictions
)

print("Accuracy:", accuracy)

print("\nConfusion Matrix:")
print(matrix)


# -----------------------------
# 5. Label mapping
# -----------------------------

label_names = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}


# -----------------------------
# 6. Test prediction
# -----------------------------

sample = "I am extremely happy today"

sample_vector = vectorizer.transform(
    [sample]
)

prediction = model.predict(
    sample_vector
)[0]

print("\nSample:", sample)
print("Label ID:", prediction)
print("Emotion:", label_names[prediction])


# -----------------------------
# 7. MLflow
# -----------------------------

mlflow.set_experiment(
    "sakoonify-emotion"
)

with mlflow.start_run():

    mlflow.log_param(
        "model",
        "LogisticRegression"
    )

    mlflow.log_param(
        "vectorizer",
        "TF-IDF"
    )

    mlflow.log_param(
        "max_iter",
        1000
    )

    mlflow.log_metric(
        "accuracy",
        accuracy
    )

    mlflow.sklearn.log_model(
        model,
        "emotion-model"
    )


# -----------------------------
# 8. Save locally
# -----------------------------

os.makedirs("models", exist_ok=True)

joblib.dump(
    model,
    "models/emotion_model.pkl"
)

joblib.dump(
    vectorizer,
    "models/tfidf_vectorizer.pkl"
)

print("\nModel saved successfully.")