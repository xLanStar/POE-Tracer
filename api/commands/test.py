from api.bot import bot
from api.trace.trade import trade
from discord.app_commands import choices, Choice, command, describe
from discord import Interaction, Object, app_commands
from typing import Optional

@bot.tree.command(name='test')
@app_commands.describe(name='your name')
async def test(ineraction: Interaction, name:Optional[str]):
    if name == '1':
        

# tree.add_command(test)