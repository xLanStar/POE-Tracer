from api.bot import bot
from discord import Interaction
from typing import Optional

VIEW_TRADE_MENU = None

@bot.tree.command(name='trade')
async def test(ineraction: Interaction):
	await ineraction.response.send_message(view=VIEW_TRADE_MENU)