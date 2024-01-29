import vimeworld as pyvime
from vimeworld import Client, users
bot = Client()
bot.start()

us = users(bot)


user_id  = us.get_by_nick('xtrafrancyz').user_id
username = us.get_by_nick('xtrafrancyz').username
level = us.get_by_nick('xtrafrancyz').level
guild = us.get_by_nick('xtrafrancyz').guild_id
print(f'{user_id}\n{username}\n{level}\n{guild}')