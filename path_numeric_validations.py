from fastapi import APIRouter, Path
router = APIRouter()

@router.get("/orders/{order_id}")
def read_order(order_id: int = Path(ge=1, le=999999, description="1~999999")):
    return {"order_id": order_id}
