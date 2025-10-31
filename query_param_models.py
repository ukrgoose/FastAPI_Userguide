from typing import Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
router = APIRouter()

class ItemFilters(BaseModel):
    q: Optional[str] = None
    size: Optional[int] = None
    in_stock: bool = True

def filters_dep(q: Optional[str] = None, size: Optional[int] = None, in_stock: bool = True) -> ItemFilters:
    return ItemFilters(q=q, size=size, in_stock=in_stock)

@router.get("/items")
def list_items(filters: ItemFilters = Depends(filters_dep)):
    return {"filters": filters}
