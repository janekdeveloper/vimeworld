import vimeworld as pyvime
from vimeworld import Client, users
bot = Client()
bot.start()

us = users(bot)


user_id  = us.get_by_nick('janek').user_id
username = us.get_by_nick('janek').username
level = us.get_by_nick('janek').level
guild = us.get_by_nick('janek').guild
print(f'{user_id}\n{username}\n{level}\n{guild}')