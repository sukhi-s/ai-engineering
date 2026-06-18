from .storage import PROMPTS


CURRENT_ID = 1


def create_prompt(title: str, content: str):

    global CURRENT_ID

    prompt = {
        "id": CURRENT_ID,
        "title": title,
        "content": content
    }

    PROMPTS[CURRENT_ID] = prompt

    CURRENT_ID += 1

    return prompt


def list_prompts():

    return list(PROMPTS.values())