from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix


texts = [
    "I am extremely happy today",
    "I feel amazing and joyful",
    "I am so excited",
    "Today is a wonderful day",
    "I feel very sad",
    "I am feeling depressed",
    "I am crying and unhappy",
    "Today has been terrible",
    "I am really angry",
    "This makes me furious",
    "I hate this situation",
    "I am very annoyed",
]

labels = [
    "joy",
    "joy",
    "joy",
    "joy",
    "sadness",
    "sadness",
    "sadness",
    "sadness",
    "anger",
    "anger",
    "anger",
    "anger",
]


# 1. Split the data
X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.25,
    random_state=42,
    stratify=labels
)


# 2. Convert text into numerical features
vectorizer = TfidfVectorizer()

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# 3. Train the classifier
model = LogisticRegression(max_iter=1000)

model.fit(X_train_tfidf, y_train)


# 4. Make predictions
predictions = model.predict(X_test_tfidf)


# 5. Evaluate
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))