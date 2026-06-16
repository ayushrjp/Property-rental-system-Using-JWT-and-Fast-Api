from fastapi import APIRouter, HTTPException
from app.schemas.user import LoginRequest
from app.services.auth_service import get_user_by_email
from app.core.security import create_access_token

router = APIRouter()  

@router.post("/login")
def login(data: LoginRequest):
    user = get_user_by_email(data.email)

    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": user["email"]})

    return {
        "access_token": token,
        "user": user
    }