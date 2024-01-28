import requests as rq
import json
from .client import Client

class users():
	"""docstring for user"""
	class users():
		def __init__(self, user_id, username):
			self.user_id = user_id
			self.username = username
	
	def __init__(self, client_instance):
		self.sess = client_instance.session

	def get_by_nick(self, nick):
		info_by_nick = json.loads(self.sess.get(f"https://api.vimeworld.com/user/name/{nick}").content)[0]
		user_id = info_by_nick.get('id', None)
		username = info_by_nick.get('name', None)
		return self.users(user_id, username)