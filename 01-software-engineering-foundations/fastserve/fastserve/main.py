from fastapi import FastAPI

from fastserve.routes import hello

app = FastAPI()


@app.get("/")
def root():
    return hello()