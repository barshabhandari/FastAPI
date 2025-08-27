from fastapi import APIRouter, Depends, HTTPException, status
from app.routers.auth import create_token, users_db



router = APIRouter()


@router.post("/login")
def login(username: str, password: str):
    user = users_db.get(username)
    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_token(username=user["username"], role=user["role"])
    return {"access_token": token, "token_type": "bearer"}


from fastapi.security import OAuth2PasswordRequestForm

@router.post("/token")
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_db.get(form_data.username)
    if not user or user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token(username=user["username"], role=user["role"])
    return {"access_token": token, "token_type": "bearer"}