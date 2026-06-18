import time


def stream_tokens(text: str):

    words = text.split()

    for word in words:

        yield word + " "

        time.sleep(0.2)