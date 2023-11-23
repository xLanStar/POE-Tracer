from api.bot import bot
from discord import Interaction

VIEW_NINJA = None

@bot.tree.command(name='ninja')
async def ninja(ineraction: Interaction, url: str):
	await ineraction.response.send_message(view=VIEW_TRADE_MENU)