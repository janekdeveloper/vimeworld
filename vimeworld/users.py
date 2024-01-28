import requests as rq
import json
from .client import Client

class users():
	"""docstring for user"""
	class users():
		def __init__(self, user_id, username, level, rank, playedSeconds, lastSeen, guild):
			self.user_id = user_id
			self.username = username
			self.level = level
			self.rank = rank
			self.playedSeconds = playedSeconds
			self.lastSeen = lastSeen
			self.guild = guild
	
	def __init__(self, client_instance):
		self.sess = client_instance.session
	# "username":"xtrafrancyz","level":43,"levelPercentage":0.61355,"rank":"ADMIN","playedSeconds":10948983,"lastSeen":1706281819,"guild":{"id":401,"name":"\u041a\u0435\u043a \u0434\u0435\u043b\u0430 - \u0445\u043e\u0440\u043e\u0448\u043e","tag":null,"color":"&f","level":1,"levelPercentage":0.41668,"avatar_url":"https://mc.vimeworld.com/launcher/guilds/401.png?t=1598021991"}}]
	def get_by_nick(self, nick):
		info_by_nick = json.loads(self.sess.get(f"https://api.vimeworld.com/user/name/{nick}").content)
		if info_by_nick != []:
			user_id = info_by_nick[0].get('id', None)
			username = info_by_nick[0].get('username', None)
			level = info_by_nick[0].get('level', None)
			levelPercentage = info_by_nick[0].get('levelPercentage', None)
			rank = info_by_nick[0].get('rank', None)
			playedSeconds = info_by_nick[0].get('playedSeconds', None)
			lastSeen = info_by_nick[0].get('lastSeen', None)
			guild = info_by_nick[0].get('guild', None)
			return self.users(user_id, username, level, rank, playedSeconds, lastSeen, guild)
		else:
			return self.users('Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found')