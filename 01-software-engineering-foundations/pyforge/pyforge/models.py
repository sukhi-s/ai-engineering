from pydantic import BaseModel


class ChatRequest(BaseModel):
    model: str
    prompt: str
    temperature: float = 0.7


class ChatResponse(BaseModel):
    text: str
    model: str