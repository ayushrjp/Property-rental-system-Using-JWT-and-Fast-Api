from fastapi import APIRouter
from app.db.supabase import supabase

router = APIRouter()  

@router.get("/")
def get_payments():
    return supabase.table("payments").select("*").execute().data

@router.post("/")
def add_payment(data: dict):
    return supabase.table("payments").insert(data).execute().data