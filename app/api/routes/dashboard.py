from fastapi import APIRouter

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/summary")
def summary():
    return {
        "active_incidents": 3,
        "healthy_services": 12,
        "critical_services": 1,
        "cluster_health": "WARNING"
    }

@router.get("/incidents")
def incidents():
    return [
        {
            "id": "INC-1001",
            "service": "payment-service",
            "severity": "P1",
            "status": "OPEN"
        }
    ]