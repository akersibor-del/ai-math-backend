from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Math Reasoning Assistant")

app.include_router(router)
