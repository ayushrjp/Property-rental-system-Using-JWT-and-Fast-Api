from pydantic import BaseModel, EmailStr

class TenantCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str

class TenantResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    phone: str