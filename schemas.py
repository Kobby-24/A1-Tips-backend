from datetime import datetime
from pydantic import BaseModel



## Schemas for the blog application

    


class User(BaseModel):
    username: str
    email:str
    password:str
    phone_number: str
    is_superuser: bool = False
    is_staff: bool = False

class AdminUser(BaseModel):
    username: str
    email:str
    password:str
    phone_number: str
    is_superuser: bool = True
    is_staff: bool = True

class GetUser(BaseModel):
    id:int
    username: str
    email:str
    phone_number: str
    is_active: int
    is_superuser: int
    is_staff: int
    class Config:
        orm_mode = True
        

class Login(BaseModel):
    email_or_username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: str | None = None

class Game(BaseModel):
    id: int
    home_team: str
    away_team: str
    tournament: str
    sport: str
    odds: float
    match_status: str
    prediction: str
    match_day: str

    class Config:
        orm_mode = True
class Booking(BaseModel):
    id: int
    share_code: str
    share_url: str
    deadline: str
    sold_out: bool
    created_at: str
    category: str
    price: str  # <-- Add this line
    games: list[Game] = []

    class Config:
        orm_mode = True

class GameResponse(BaseModel):
    home: str
    away: str
    prediction: str | None = None
    odd: float | None = None
    sport: str
    tournament: str
    match_status: str 

class BookingResponse(BaseModel):
    deadline: str
    shareCode: str
    shareURL: str
    category: str
    price: str  # <-- Add this line
    games: list[GameResponse] = []


class PurchaseResponse(BaseModel):
    id: int
    reference: str
    amount: float
    email: str
    purchase_date: str
    user_id: int
    booking_id: int

    class Config:
        orm_mode = True

class AdminNotificationResponse(BaseModel):
    id: int
    message: str
    created_at: datetime

    class Config:
        orm_mode = True

class SMSRequest(BaseModel):
    phone_number: list[str]
    message: str