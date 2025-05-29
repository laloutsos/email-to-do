from fastapi import FastAPI
from app.router import router

app = FastAPI(title="Email Reader API")

app.include_router(router)
