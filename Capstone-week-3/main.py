import sqlite3

from fastapi import FastAPI, HTTPException, Depends

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user
)

from database import (
    init_db,
    create_user,
    get_user,
    save_message
)

from emotion import predict_emotion

from schemas import (
    RegisterRequest,
    LoginRequest,
    ChatRequest
)


app = FastAPI(
    title="Sakoonify v0.3"
)


# --------------------------------
# Register
# --------------------------------

@app.post("/register")
def register(request: RegisterRequest):

    password_hash = hash_password(
        request.password
    )

    try:

        create_user(
            request.username,
            password_hash
        )

    except sqlite3.IntegrityError:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return {
        "message": "User registered successfully"
    }


# --------------------------------
# Login
# --------------------------------

@app.post("/login")
def login(request: LoginRequest):

    user = get_user(
        request.username
    )

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    username, password_hash = user

    if not verify_password(
        request.password,
        password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        username
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# --------------------------------
# Protected Chat
# --------------------------------

@app.post("/chat")
def chat(
    request: ChatRequest,
    username: str = Depends(
        get_current_user
    )
):

    emotion_result = predict_emotion(
        request.message
    )

    save_message(
        username,
        request.message,
        emotion_result["emotion"]
    )

    return {
        "username": username,
        "message": request.message,
        "emotion": emotion_result,
        "reply": (
            f"I understand that you "
            f"are feeling "
            f"{emotion_result['emotion']}."
        )
    }


# --------------------------------
# Initialize database
# --------------------------------

init_db()