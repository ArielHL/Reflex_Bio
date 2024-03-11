import reflex as rx
from own.modules.database import dataItem
import own.constants as const   
from .twitch_api import TwitchAPI
from .api_supabase import SupabaseAPI

TWITCH_API = TwitchAPI()
SUPABASE_API = SupabaseAPI()

async def repo() -> str:
    return const.REPO_URL

async def live(user:str) -> bool:
    return TWITCH_API.live(user)

async def get_data() -> list[dataItem]:
    return SUPABASE_API.get_table()
