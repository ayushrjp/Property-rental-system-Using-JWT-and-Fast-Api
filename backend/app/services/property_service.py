from app.db.supabase import supabase

def get_properties():
    return supabase.table("properties").select("*").execute().data

def create_property(data):
    return supabase.table("properties").insert(data).execute().data

def update_property(property_id, data):
    return supabase.table("properties").update(data).eq("id", property_id).execute().data

def delete_property(property_id):
    return supabase.table("properties").delete().eq("id", property_id).execute().data