from fastapi import FastAPI
from .database import engine, Base

app = FastAPI(title="Verdana Backend")


Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Backend working fine!"}
