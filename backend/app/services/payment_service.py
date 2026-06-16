from app.database import supabase

def get_all_payments():
    return supabase.table("payments").select("*").execute().data

def create_payment(data):
    return supabase.table("payments").insert(data).execute().data