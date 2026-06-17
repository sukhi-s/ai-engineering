from pydantic import BaseModel


class ChatRequest(BaseModel):
    model: str
    prompt: str


class ChatResponse(BaseModel):
    text: str
    model: str