import tcpNetwork


class socketHandeler(object):
	""" Class for keeping track of sockets """

	def __init__(self, socketDoMethod, logMethod = tcpNetwork.logMethod):
		self.stopSockets = False
		self.logMethod = logMethod
		self.socketDoMethod = socketDoMethod

	def handleSocket(self, s):

		# set socket options
		s.setblocking(True)
		s.settimeout(60)

		while not self.stopSockets:

			try:
				result = self.socketDoMethod(s)
				if not result:
					break

			except Exception as e:
				self.logMethod("handleSocket exception with value %s" % e.message)
				break
