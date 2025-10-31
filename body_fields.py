from fastapi import APIRouter
from pydantic import BaseModel, Field
router = APIRouter()

class Product(BaseModel):
    name: str = Field(..., title="Product Name", min_length=2, max_length=100)
    price: float = Field(..., gt=0, description="Must be > 0")
    tags: list[str] = Field(default_factory=list, description="Optional tags")

@router.post("/products")
def create_product(p: Product):
    return {"product": p}
