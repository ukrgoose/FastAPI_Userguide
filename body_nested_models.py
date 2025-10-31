from pydantic import BaseModel, Field
from fastapi import APIRouter
router = APIRouter()

class Address(BaseModel):
    city: str
    street: str
    zip_code: str = Field(min_length=4, max_length=10)

class Customer(BaseModel):
    name: str
    address: Address

@router.post("/customers")
def create_customer(c: Customer):
    return {"customer": c}
