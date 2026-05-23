from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes.analysis import router as analysis_router
from app.api.routes.dashboard import router as dashboard_router
from app.api.routes.health import router as health_router
from app.api.routes.dependencies import router as dependency_router
from app.db.database import initialize_database

app = FastAPI(
    title="ObservaAI Enterprise",
    version="4.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    initialize_database()

app.include_router(health_router)
app.include_router(analysis_router)
app.include_router(dashboard_router)
app.include_router(dependency_router)