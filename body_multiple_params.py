from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
router = APIRouter()

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

class Item(BaseModel):
    name: str
    price: float

@router.post("/users/{user_id}/items")
def create_user_item(user_id: int, user: User, item: Item, notify: bool = False):
    return {"user_id": user_id, "user": user, "item": item, "notify": notify}
