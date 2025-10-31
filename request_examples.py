from pydantic import BaseModel, Field
from fastapi import APIRouter
router = APIRouter()

class BlogPost(BaseModel):
    title: str = Field(..., description="Post title")
    content: str = Field(..., description="Markdown content")
    published: bool = False
    model_config = {
        "json_schema_extra": {
            "examples": [
                {"title": "My First Post", "content": "Hello **FastAPI**!", "published": True}
            ]
        }
    }

@router.post("/posts")
def create_post(p: BlogPost):
    return {"post": p}
