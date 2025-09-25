from fastapi import APIRouter, Request, Depends
from sqlalchemy.orm import Session
from utils import payment
from database import get_db

router = APIRouter(
    prefix="/payment",
    tags=["payment"],
)


@router.post("/verify", status_code=200)
async def verify_payment_endpoint(request: Request, db: Session = Depends(get_db)):
    data = await request.json()
    reference = data.get("reference")
    if not reference:
        return {"status": "error", "message": "Reference is required"}

    result = await payment.verify_payment(reference, db)
    import json

    result_data = json.loads(result.body.decode())
    if result_data["status"] == "success":
        return await payment.record_payment_event(
            data.get("email"), db, data.get("booking_id"), reference
        )
    else:
        return {
            "status": "error",
            "message": result_data.get("message", "Verification failed"),
        }


@router.get("/test", status_code=200)
async def test_endpoint(db: Session = Depends(get_db)):
    return payment.get_booking(db)

@router.get("/number-of-purchases", status_code=200)
def number_of_purchases(db: Session = Depends(get_db)):
    return payment.number_of_purchases(db)