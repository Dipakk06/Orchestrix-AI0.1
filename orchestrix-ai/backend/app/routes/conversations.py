from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.models import Conversation
from app.db.session import get_db

router = APIRouter(prefix="/api", tags=["conversations"])


@router.get("/conversations")
def get_conversations(user_id: str, db: Session = Depends(get_db)):
    rows = db.scalars(select(Conversation).where(Conversation.user_id == user_id)).all()
    return [
        {
            "id": c.id,
            "title": c.title,
            "content": c.content,
            "created_at": c.created_at,
        }
        for c in rows
    ]
