from app.database import supabase

def get_all_tenants():
    return supabase.table("tenants").select("*").execute().data

def create_tenant(data):
    return supabase.table("tenants").insert(data).execute().data