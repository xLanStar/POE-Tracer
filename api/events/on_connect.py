from api.bot import bot

@bot.event
async def on_connect():
    print("on_connect:", bot.user)