from typing import Optional
from fastapi import APIRouter
router = APIRouter()

@router.get("/search")
def search(q: Optional[str] = None, skip: int = 0, limit: int = 10):
    return {"q": q, "skip": skip, "limit": limit}
