from fastapi import APIRouter, HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer
from app.routers.auth import get_current_user

router = APIRouter()


@router.get("/public")
def public_route():
    return {"message": "This is a public endpoint."}


@router.get("/user")
def user_route(user: dict = Depends(get_current_user)):
    return {"message": f"Hello {user['sub']}, you have access!"}

# Admin-only route
@router.get("/admin")
def admin_route(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin access required")
    return {"message": "Welcome Admin!"}


@router.get("/data1")
def data1():
    return {"data": "Sample Data 1"}

@router.get("/data2")
def data2():
    return {"data": "Sample Data 2"}

@router.get("/secret_data")
def secret_data(user: dict = Depends(get_current_user)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403, detail="Admin only data")
    return {"data": "Only admin can access this info"}
