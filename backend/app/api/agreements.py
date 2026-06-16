from fastapi import APIRouter
from app.db.supabase import supabase

router = APIRouter()   

@router.get("/")
def get_agreements():
    return supabase.table("agreements").select("*").execute().data

@router.post("/")
def add_agreement(data: dict):
    return supabase.table("agreements").insert(data).execute().data