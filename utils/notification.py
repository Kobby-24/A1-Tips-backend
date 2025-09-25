from models import AdminNotification
from sqlalchemy.orm import Session

def create_admin_notification(db: Session, message: str):
    notification = AdminNotification(message=message)
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return notification

def get_notifications(db: Session):
    notifications = db.query(AdminNotification).all()
    return [
        {
            "id": n.id,
            "message": n.message,
            "type": getattr(n, "type", "info"),
            "read": n.is_read,
            "timestamp": n.created_at.strftime('%Y-%m-%d %I:%M %p') if n.created_at else None
        }
        for n in notifications
    ]

def mark_notification_as_read(db: Session, notification_id: int):
    notification = db.query(AdminNotification).filter(AdminNotification.id == notification_id).first()
    if notification:
        notification.is_read = True
        db.commit()
        db.refresh(notification)
    return notification

def number_of_unread_notifications(db: Session):
    return db.query(AdminNotification).filter(~AdminNotification.is_read).count()