from api.bot import bot
from api.ui import load_ui

@bot.event
async def on_ready():
    # load_ui()
    await bot.tree.sync()
    print("Bot is Synced")
    # await bot.change_presence(Status.online, Game('努力學習py中'))
    # text_channel_list = []
    # for server in Client.servers:
    #     for channel in server.channels:
    #         if channel.type == 'Text':
    #             text_channel_list.append(channel)
    #             channel.send("Hello")