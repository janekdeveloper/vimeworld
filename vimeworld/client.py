import requests as rq

class Client():
	"""docstring for """
	def __init__(self, token=None):
		self.token = token
		self.session = None
		#self.headers = {'Access-Token': self.token}

	def start(self):
		if self.session is None:
			self.session = rq.session()
			#self.session.headers.update(self.headers)

	def stop(self):
		if self.session is not None:
			self.session.close()
			self.session = None