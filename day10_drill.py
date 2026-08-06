from fastapi import FastAPI
from pydantic import BaseModel

from daySessionPydantic import Session

app = FastAPI()

session = Session()


@app.get("/health")
def health():

    return {
        "status": "ok"
    }


class ChatRequest(BaseModel):

    user_id: str
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    session.add_message(
        request.user_id,
        request.message
    )

    return {

        "user_id": request.user_id,
        "message": request.message,
        "reply": "I'm here to help!"
    }


@app.get("/history")
def history():

    return session.get_history()