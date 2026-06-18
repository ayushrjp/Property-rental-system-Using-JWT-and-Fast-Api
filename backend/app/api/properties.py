from fastapi import APIRouter
from app.services.property_service import *

router = APIRouter()

@router.get("/")
def get_all():
    return get_properties()

@router.post("/")
def create(data: dict):
    return create_property(data)

@router.put("/{property_id}")
def update(property_id: str, data: dict):
    return update_property(property_id, data)

@router.delete("/{property_id}")
def delete(property_id: str):
    return delete_property(property_id)