import socket
import tcpNetwork


def connectTo(ip, port, logMethod = tcpNetwork.logMethod):
	''' Connect to node and return socket '''

	logMethod("Connecting to %s" % str(ip))

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		return s

	except Exception as e:
		logMethod("connectTo exception with value %s" % e.message)
