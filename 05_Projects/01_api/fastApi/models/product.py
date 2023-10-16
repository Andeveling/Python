from typing import Optional
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float

    class Config:
        orm_mode = True
