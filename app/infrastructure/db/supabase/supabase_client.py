from supabase import Client, create_client

from .supabase_settings import SupabaseSettings


def get_supabase_client() -> Client:
    supabase_settings = SupabaseSettings()
    return create_client(supabase_settings.url, supabase_settings.key)
