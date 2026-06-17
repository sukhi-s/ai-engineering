from .config import Config
from .models import ChatRequest, ChatResponse


class AIClient:

    def __init__(self):
        self.default_model = Config.DEFAULT_MODEL

    def chat(
        self,
        request: ChatRequest
    ) -> ChatResponse:

        return ChatResponse(
            text=f"Echo: {request.prompt}",
            model=request.model
        )