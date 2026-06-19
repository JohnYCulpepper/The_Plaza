from fastapi import FastAPI

from backend.routes.auth import router

from backend.database import engine, Base

from backend.models.user import User


app = FastAPI()

app.include_router(router)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "The Plaza API"
    }
