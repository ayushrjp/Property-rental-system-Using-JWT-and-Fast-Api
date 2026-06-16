from fastapi import APIRouter
from app.db.supabase import supabase

router = APIRouter()   

@router.get("/")
def get_properties():
    return supabase.table("properties").select("*").execute().data

@router.post("/")
def add_property(data: dict):
    return supabase.table("properties").insert(data).execute().data

@router.delete("/{property_id}")
def delete_property(property_id: str):
    supabase.table("properties").delete().eq("id", property_id).execute()
    return {"message": "Property deleted"}