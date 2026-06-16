from app.database import supabase

def get_all_agreements():
    return supabase.table("agreements").select("*").execute().data

def create_agreement(data):
    return supabase.table("agreements").insert(data).execute().data