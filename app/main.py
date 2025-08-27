from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.login import router as login_router
from app.routers.auth import router as auth_router
from app.routers.post import router as post_router

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router)
app.include_router(auth_router)
app.include_router(post_router)