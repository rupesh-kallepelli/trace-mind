from fastapi import APIRouter
from app.agents.production_agent import ProductionSupportAgent

router = APIRouter()

@router.post("/analyze")
def analyze(payload: dict):

    result = ProductionSupportAgent.analyze(
        payload["issue"]
    )

    return result