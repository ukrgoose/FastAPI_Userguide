from datetime import datetime
from uuid import UUID
from pydantic import BaseModel, EmailStr, HttpUrl
from fastapi import APIRouter
router = APIRouter()

class Meta(BaseModel):
    created_at: datetime
    author_email: EmailStr
    source_url: HttpUrl
    uid: UUID

@router.post("/meta")
def create_meta(m: Meta):
    return {"meta": m}
