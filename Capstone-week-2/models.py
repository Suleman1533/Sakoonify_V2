from pydantic import BaseModel


class ChatRequest(BaseModel):
    user_id: str
    message: str


class ChatResponse(BaseModel):
    user_id: str
    message: str
    reply: str


class HistoryResponse(BaseModel):
    user_id: str
    history: list