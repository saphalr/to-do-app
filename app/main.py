from fastapi import FastAPI
from app.core.config import settings

app = FastAPI()

# app.include_router(todo.router, prefix='/api/todo')


@app.get("/")
def read_root():
    return {
        "debug": settings.debug,
        "environment": settings.environment,
        "port": settings.port,
        "host": settings.host,
    }
