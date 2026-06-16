from app.db.supabase import supabase

def get_user_by_email(email: str):
    res = supabase.table("users").select("*").eq("email", email).execute()
    return res.data[0] if res.data else None