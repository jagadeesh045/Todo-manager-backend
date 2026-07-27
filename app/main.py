from fastapi import FastAPI
from app.database import db

app = FastAPI(
    title="Todo Manager API",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to Todo Manager API"
    }

@app.get("/db-test")
def test_database():
    db.list_collection_names()
    return {
        "message": "MongoDB Connected Successfully"
    }