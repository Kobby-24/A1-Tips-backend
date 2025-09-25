from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    phone_number = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Integer, default=1)
    is_superuser = Column(Integer, default=0)
    is_staff = Column(Integer, default=0)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    share_code = Column(String, unique=True, index=True)
    share_url = Column(String, unique=False, index=True)
    deadline = Column(DateTime, index=True)
    category = Column(String, index=True)
    sold_out = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)
    games = relationship("Game", back_populates="booking")
    price = Column(String)
    updated = Column(Boolean, default=False)


class Game(Base):
    __tablename__ = "games"

    id = Column(Integer, primary_key=True, index=True)
    home_team = Column(String, index=True)
    away_team = Column(String, index=True)
    tournament = Column(String, index=True)
    sport = Column(String, index=True)
    odds = Column(Float, index=True)
    prediction = Column(String, index=True)
    match_status = Column(String, index=True, default="scheduled")
    match_day = Column(DateTime, index=True, default=datetime.now)
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    booking = relationship("Booking", back_populates="games")

class Purchase(Base):
    __tablename__ = "purchases"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    booking_id = Column(Integer, ForeignKey("bookings.id"))
    purchase_date = Column(DateTime, default=datetime.now)
    reference = Column(String, unique=True, index=True)
    status = Column(String, index=True, default="pending")

    user = relationship("User")
    booking = relationship("Booking")

class AdminNotification(Base):
    __tablename__ = "admin_notifications"

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.now)
    is_read = Column(Boolean, default=False)
    type = Column(String, index=True, default="info")


class AdminSendSMS(Base):
    __tablename__ = "admin_send_sms"

    id = Column(Integer, primary_key=True, index=True)
    number_of_recipients = Column(Integer, index=True)
    message = Column(String, index=True)
    sent_at = Column(DateTime, default=datetime.now)
    status = Column(String, index=True)