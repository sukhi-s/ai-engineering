from fastapi import APIRouter

from .models import PromptCreate
from .service import create_prompt
from .service import list_prompts

router = APIRouter()


@router.get("/")
def root():

    return {
        "message": "Welcome to FastServe"
    }


@router.post("/prompts")
def create(prompt: PromptCreate):

    return create_prompt(
        title=prompt.title,
        content=prompt.content
    )


@router.get("/prompts")
def get_all():

    return list_prompts()