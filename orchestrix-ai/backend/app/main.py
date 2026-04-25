from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.core.logging import configure_logging
from app.db.base import Base
from app.db.session import engine
from app.routes.agent import router as agent_router
from app.routes.chat import router as chat_router
from app.routes.conversations import router as conversations_router
from app.routes.memory import router as memory_router
from app.routes.tools import router as tools_router
from app.routes.voice import router as voice_router

configure_logging()
settings = get_settings()

app = FastAPI(title="Orchestrix AI API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin.strip() for origin in settings.cors_origins.split(",")],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(chat_router)
app.include_router(agent_router)
app.include_router(conversations_router)
app.include_router(memory_router)
app.include_router(voice_router)
app.include_router(tools_router)


@app.get("/")
def root():
    return {"name": settings.app_name, "status": "running"}
