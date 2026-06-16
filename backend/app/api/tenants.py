from fastapi import APIRouter
from app.db.supabase import supabase

router = APIRouter()  

@router.get("/")
def get_tenants():
    return supabase.table("tenants").select("*").execute().data

@router.post("/")
def add_tenant(data: dict):
    return supabase.table("tenants").insert(data).execute().data