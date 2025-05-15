from fastapi import FastAPI
from app.routes import router
from app.database import engine, Base

app = FastAPI()


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(engine)


app.include_router(router)
