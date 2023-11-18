import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
SUPABSE_URL = os.getenv("SUPABASE_URL")
SUPABSE_KEY = os.getenv("SUPABASE_KEY")


class SupabaseSettings(BaseModel):
    url: str = SUPABSE_URL
    key: str = SUPABSE_KEY
