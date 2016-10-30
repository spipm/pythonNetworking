import socket
import threading
import tcpNetwork
from time import sleep


class networkingServer(object):
	""" Class for running a non-blocking TCP server, creating blocking sockets """

	def __init__(self, logMethod = tcpNetwork.logMethod, threadMethod = threading.Thread):
		self.stopServer = False
		self.logMethod = logMethod
		self.threadMethod = threadMethod
		
	def runServer(self, port, socketHandeler):

		self.logMethod("Starting server")

		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			s.bind(('', port))
			s.listen(1)
			s.setblocking(False)

		except Exception as e:
			self.logMethod("runServer socket creation exception with value %s" % e.message)
			return

		while True:

			if self.stopServer:
				s.close()
				break

			try:
				conn, addr = s.accept()
				self.logMethod("Accepted connection from %s" % str(addr[0]))
				self.threadMethod(socketHandeler, args=(conn,))

			except Exception as e:

				# We expect exceptions here because of non-blocking sockets
				if e.message != "":
					self.logMethod("runServer socket creation exception with value %s" % e.message)
				
				sleep(1)
