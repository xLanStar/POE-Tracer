from bot.instance import bot


@bot.event
async def on_ready():
    print('目前登入身份：',bot.user)


@bot.command('%')
async def test(ctx):
    pass