from pydantic import BaseModel

class PaymentCreate(BaseModel):
    tenant_id: str
    property_id: str
    amount: int
    status: str

class PaymentResponse(BaseModel):
    id: str
    tenant_id: str
    property_id: str
    amount: int
    status: str