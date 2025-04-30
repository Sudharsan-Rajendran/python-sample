from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.controllers import student_controller

app = FastAPI()

@app.get("/")
def heratbeat():
    return {"message": "Hello World"}

app.include_router(student_controller.router)