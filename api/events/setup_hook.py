from api.bot import bot
from api.ui import load_ui

@bot.event
async def setup_hook():
    load_ui()