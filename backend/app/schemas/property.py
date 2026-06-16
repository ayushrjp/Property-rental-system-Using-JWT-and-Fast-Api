from pydantic import BaseModel

class PropertyCreate(BaseModel):
    title: str
    location: str
    price: int

class PropertyResponse(BaseModel):
    id: str
    title: str
    location: str
    price: int