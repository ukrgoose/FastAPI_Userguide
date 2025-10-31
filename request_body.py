from fastapi import APIRouter
from pydantic import BaseModel, Field
router = APIRouter()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = Field(default=False)

@router.post("/items")
def create_item(item: Item):
    return {"created": item}
