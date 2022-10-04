from discord.ext.commands import Bot
from discord import Intents


# SECTION_TYPE: Intent
intents = Intents.all()


# SECTION_TYPE: Initialize Bot
bot = Bot(command_prefix='$', intents=intents)