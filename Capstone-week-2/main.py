import logging
from pathlib import Path

from fastapi import FastAPI, UploadFile, File, HTTPException

from models import ChatRequest, ChatResponse, HistoryResponse
from sessions import Session
from config import (
    UPLOAD_FOLDER,
    MAX_FILE_SIZE,
    ALLOWED_AUDIO_EXTENSIONS
)


# -------------------------
# Logging
# -------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# -------------------------
# FastAPI application
# -------------------------

app = FastAPI(
    title="Sakoonify API",
    version="0.2.0"
)


# -------------------------
# Session manager
# -------------------------

session = Session()


# -------------------------
# Health endpoint
# -------------------------

@app.get("/health")
def health():
    return {
        "status": "ok"
    }


# -------------------------
# Chat endpoint
# -------------------------

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    try:
        # Save user's message
        session.add_message(
            request.user_id,
            "user",
            request.message
        )

        # Placeholder AI reply
        reply = "I am here to listen and help."

        # Save bot's reply
        session.add_message(
            request.user_id,
            "bot",
            reply
        )

        logging.info(
            f"Chat processed for user {request.user_id}"
        )

        return {
            "user_id": request.user_id,
            "message": request.message,
            "reply": reply
        }

    except Exception as e:
        logging.error(f"Chat error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Failed to process chat."
        )


# -------------------------
# Session history endpoint
# -------------------------

@app.get(
    "/history/{user_id}",
    response_model=HistoryResponse
)
def get_history(user_id: str):

    try:
        history = session.get_history(user_id)

        return {
            "user_id": user_id,
            "history": history
        }

    except Exception as e:
        logging.error(f"History error: {e}")

        raise HTTPException(
            status_code=500,
            detail="Failed to retrieve history."
        )


# -------------------------
# Audio upload endpoint
# -------------------------

@app.post("/upload-audio")
async def upload_audio(
    file: UploadFile = File(...)
):

    # -------------------------
    # Check filename
    # -------------------------

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="Filename is missing."
        )


    # -------------------------
    # Check extension
    # -------------------------

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_AUDIO_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only .mp3 and .wav files are allowed."
        )


    # -------------------------
    # Read file
    # -------------------------

    try:
        content = await file.read()

    except Exception as e:
        logging.error(f"Failed to read uploaded file: {e}")

        raise HTTPException(
            status_code=500,
            detail="Failed to read uploaded file."
        )


    # -------------------------
    # Check file size
    # -------------------------

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=413,
            detail="File is larger than 10 MB."
        )


    # -------------------------
    # Create uploads folder
    # -------------------------

    UPLOAD_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )


    # -------------------------
    # Create safe filename
    # -------------------------

    filename = Path(file.filename).name

    file_path = UPLOAD_FOLDER / filename


    # -------------------------
    # Save file
    # -------------------------

    try:
        with open(file_path, "wb") as output_file:
            output_file.write(content)

        logging.info(
            f"Audio uploaded successfully: {filename}"
        )

    except Exception as e:
        logging.error(f"Failed to save audio: {e}")

        raise HTTPException(
            status_code=500,
            detail="Failed to save audio file."
        )


    return {
        "message": "Audio uploaded successfully.",
        "filename": filename,
        "size_bytes": len(content)
    }