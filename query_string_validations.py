from typing import Optional
from fastapi import APIRouter, Query
router = APIRouter()

@router.get("/validate")
def validate_q(
    q: Optional[str] = Query(
        default=None, min_length=3, max_length=50, pattern="^[a-zA-Z0-9_ ]+$",
        description="Alphanumeric, 3~50 chars"
    )
):
    return {"q": q}
