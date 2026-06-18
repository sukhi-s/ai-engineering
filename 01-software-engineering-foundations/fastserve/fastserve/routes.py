from .models import MessageResponse


def hello() -> MessageResponse:

    return MessageResponse(
        message="Hello from FastServe"
    )