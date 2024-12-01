from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2, max_length=50)
    description: Optional[str] = Field(None, max_length=200)
    price: float = Field(..., gt=0)
    
    class Config:
        schema_extra = {
            "example": {
                "name": "Laptop",
                "description": "High-performance developer laptop",
                "price": 1299.99
            }
        }
