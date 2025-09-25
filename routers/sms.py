from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from utils import sms as sms_utils
from database import get_db
import requests

router = APIRouter(
    prefix="/sms",
    tags=["sms"],
)

@router.post("/send_bulk")
def send_bulk_sms(message: str, db: Session = Depends(get_db)):
    return sms_utils.send_bulk_sms(db, message)

@router.post("/send_individual")
def send_individual_sms(phone_number: str, message: str, db: Session = Depends(get_db)):
    return sms_utils.send_individual_sms(db, phone_number, message)

@router.get("/users-numbers/")
def get_users_numbers(db: Session = Depends(get_db)):
    return sms_utils.get_all_users_number(db)

@router.post("/register")
def register_id( db: Session = Depends(get_db)):

    endPoint = 'https://api.mnotify.com/api/senderid/register'
    apiKey = 'BnznzOKUz4c6krqXEmtU8N7Jt'
    data = {
        'sender_name': 'Betgeniuz',
        'purpose': 'For Sending SMS Newsletters'
    }
    url = endPoint + '?key=' + apiKey
    response = requests.post(url, data)
    data = response.json()

    return data

@router.get("/check")
def check_id( db: Session = Depends(get_db)):

    endPoint = 'https://api.mnotify.com/api/senderid/status'
    apiKey = 'BnznzOKUz4c6krqXEmtU8N7Jt'
    data = {
        'sender_name': 'Betgeniuz',
    }
    url = endPoint + '?key=' + apiKey
    response = requests.post(url, data)
    data = response.json()

    return data

@router.post("/send_specific")
def send_to_specific_numbers(phone_numbers: list, message: str):
    return sms_utils.send_to_specific_numbers(phone_numbers, message)