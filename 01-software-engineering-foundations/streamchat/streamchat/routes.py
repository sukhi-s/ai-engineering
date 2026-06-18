from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from models import ChatRequest
from service import generate_response
from stream import stream_tokens

router = APIRouter()


@router.get("/")
def root():

    return {
        "message": "Welcome to StreamChat"
    }


@router.post("/chat")
def chat(request: ChatRequest):

    response_text = generate_response(
        request.prompt
    )

    return StreamingResponse(
        stream_tokens(response_text),
        media_type="text/plain"
    )