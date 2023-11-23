from discord import SelectOption
from discord.ui import View, select, Select
from discord.interactions import Interaction
from api.const.item import ALL_CURRENCY_TRADE, ITEMS

class TradeMenu(View):
    @select(options=[SelectOption(label=item) for item in ['1', 'A']])
    async def select_item_name(self, interaction: Interaction, select: Select):
        await interaction.response.send_message(f'You selected { interaction.data["values"][0] }')
    
    @select(options=[SelectOption(label=item) for item in ALL_CURRENCY_TRADE])
    async def select_currency(self, interaction: Interaction, select: Select):
        await interaction.response.send_message(f'You selected { interaction.data["values"][0] }')