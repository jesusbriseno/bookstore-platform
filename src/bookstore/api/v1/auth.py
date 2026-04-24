from fastapi import APIRouter, HTTPException
from bookstore.schemas.auth import LoginRequest
from bookstore.core.security import create_access_token

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
def login(data: LoginRequest):

    if data.username != "admin" or data.password != "1234":
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": data.username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }