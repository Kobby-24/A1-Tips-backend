from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from typing import Annotated
from schemas import Login, TokenData
from utils import auth as auth_utils

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/login")
def login(request: Login, db: Session = Depends(get_db)):
    return auth_utils.login(db, request)
 
@router.post("/forgot-password")
def forgot_password(request: TokenData, db: Session = Depends(get_db)):
    return auth_utils.forgot_password(db, request)

@router.post("/reset-password")
def reset_password(email: str, new_password: str, db: Session = Depends(get_db)):
    return auth_utils.reset_password(db, email, new_password)