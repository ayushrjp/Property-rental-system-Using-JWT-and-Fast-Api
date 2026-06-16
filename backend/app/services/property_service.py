from app.database import supabase

def get_all_properties():
    return supabase.table("properties").select("*").execute().data

def create_property(data):
    return supabase.table("properties").insert(data).execute().data

def delete_property(property_id: str):
    return supabase.table("properties").delete().eq("id", property_id).execute()