from fastapi import APIRouter
from app.services.dependency_service import DependencyService

router = APIRouter(prefix="/dependencies", tags=["dependencies"])

@router.get("")
def graph():
    return DependencyService.build_graph()