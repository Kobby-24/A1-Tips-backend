from fastapi import APIRouter, status, Depends
from schemas import AdminNotificationResponse
from sqlalchemy.orm import Session
from utils import notification as notification_utils
from database import get_db

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"],
)





@router.post("/create", response_model=AdminNotificationResponse)
def create_notification(message: str, db: Session = Depends(get_db)):
    return notification_utils.create_admin_notification(db, message)


@router.post("/{notification_id}/read", response_model=AdminNotificationResponse)
def mark_notification_as_read(notification_id: int, db: Session = Depends(get_db)):
    notification = notification_utils.mark_notification_as_read(db, notification_id)
    if not notification:
        return {"error": "Notification not found"}
    return notification

@router.get("/unread/count", response_model=int)
def number_of_unread_notifications(db: Session = Depends(get_db)):
    return notification_utils.number_of_unread_notifications(db)

@router.get("/all")
def get_notifications(db: Session = Depends(get_db)):
    return notification_utils.get_notifications(db)