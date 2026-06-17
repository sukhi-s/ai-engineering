from .models import ChatRequest, ChatResponse


class AIClient:

    def chat(self, request: ChatRequest) -> ChatResponse:

        return ChatResponse(
            text=f"Echo: {request.prompt}",
            model=request.model
        )