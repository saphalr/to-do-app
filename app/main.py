from fastapi import FastAPI
from app.routes import router
from app.database import engine, Base

app = FastAPI()

# app.include_router(todo.router, prefix='/api/todo')


@app.on_event("startup")
def on_satrtup():
    Base.metadata.create_all(engine)


app.include_router(router)
