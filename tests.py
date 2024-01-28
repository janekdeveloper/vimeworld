import vimeworld as pyvime
from vimeworld import Client, users

bot = Client()
bot.start()
us = users(bot)

print(us.get_by_nick('Janek').user_id)