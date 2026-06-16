from pydantic import BaseModel

class AgreementCreate(BaseModel):
    tenant_id: str
    property_id: str
    start_date: str
    end_date: str

class AgreementResponse(BaseModel):
    id: str
    tenant_id: str
    property_id: str
    start_date: str
    end_date: str