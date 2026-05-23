from fastapi import APIRouter
from sqlalchemy import text
from app.db.database import engine

router = APIRouter(prefix="/health", tags=["health"])

@router.get("")
def health():

    status = {
        "application": "UP",
        "database": "UNKNOWN"
    }

    try:
        with engine.begin() as conn:
            conn.execute(text("SELECT 1"))
        status["database"] = "UP"
    except Exception:
        status["database"] = "DOWN"

    return status