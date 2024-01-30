import requests as rq
import json
from .client import Client

class users():
	""""""
	class users():
		def __init__(self, user_id, username, level, rank, playedSeconds, lastSeen, guild, guild_id):
			self.user_id = user_id
			self.username = username
			self.level = level
			self.rank = rank
			self.playedSeconds = playedSeconds
			self.lastSeen = lastSeen
			self.guild = guild
			self.guild_id = guild_id

	def __init__(self, client_instance):
		self.sess = client_instance.session
	
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
			if guild is not None:
				guild_id = guild.get('id', None)
			else:
				guild_id = None
			return self.users(user_id, username, level, rank, playedSeconds, lastSeen, guild, guild_id)
		else:
			return self.users('Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found')

	def get_by_id(self, id:int):
		info_by_id = json.loads(self.sess.get(f"https://api.vimeworld.com/user/{id}").content)
		if info_by_id != []:
			user_id = info_by_id[0].get('id', None)
			username = info_by_id[0].get('username', None)
			level = info_by_id[0].get('level', None)
			levelPercentage = info_by_id[0].get('levelPercentage', None)
			rank = info_by_id[0].get('rank', None)
			playedSeconds = info_by_id[0].get('playedSeconds', None)
			lastSeen = info_by_id[0].get('lastSeen', None)
			guild = info_by_id[0].get('guild', None)
			if guild is not None:
				guild_id = guild.get('id', None)
			else:
				guild_id = None
			return self.users(user_id, username, level, rank, playedSeconds, lastSeen, guild, guild_id)
		else:
			return self.users('Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found', 'Not found')

