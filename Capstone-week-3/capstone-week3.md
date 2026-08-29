#  Week3 Sakoonify v0.3 Review

## Architecture

Client
→ FastAPI
→ Authentication
→ Emotion Model
→ SQLite
→ JSON Response

## Request Flow

1. The user sends a request from the mobile app or browser.
2. FastAPI receives and validates the request using Pydantic.
3. The user authenticates using a JWT token.
4. The message is passed to the emotion classifier.
5. TF-IDF converts the text into numerical features.
6. Logistic Regression predicts the emotion.
7. The message and emotion are saved in SQLite.
8. FastAPI returns the result as JSON.

## Authentication Flow

Register:
password → bcrypt hash → SQLite

Login:
password → verify hash → JWT

Protected request:
JWT → verify token → allow access

## ML Flow

Text
→ TF-IDF
→ Logistic Regression
→ Label ID
→ Emotion Name

## Main Components

### main.py
Contains FastAPI routes and connects the application components.

### auth.py
Handles password hashing, password verification, JWT creation and JWT verification.

### database.py
Handles SQLite database operations.

### emotion.py
Loads the trained ML model and performs emotion prediction.

### schemas.py
Defines Pydantic request models.

## What I Built

Sakoonify v0.3 now has:

- SQLite persistence
- User registration
- Password hashing
- Login
- JWT authentication
- Protected `/chat` endpoint
- Own ML emotion classifier
- TF-IDF text processing
- Logistic Regression
- Emotion persistence
- JSON API responses