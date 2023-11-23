from api import bot
from dotenv import dotenv_values

env = dotenv_values('.env')
bot.run(env.get('token'))