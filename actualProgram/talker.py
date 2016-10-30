from time import sleep
import actualProgram

def socketDoMethod(s, logMethod = actualProgram.logMethod):
	''' Does actual things with the socket '''

	try:
		remoteIP = s.getpeername()[0]
		s.sendall("Sup %s!" % remoteIP)

		data = s.recv(2048)

		if not data:
			logMethod("No data, closed connection")
			return False

		logMethod("Recieved: %s" % data)

		if "Sup" in data:
			localIP, localPort = s.getsockname()
			s.sendall("Hey man, my local ip is %s and my local port is %s." % (localIP, str(localPort)))
			s.sendall("Please tell me about your file descriptor.")
		
		if "Please tell me about your file descriptor" in data:
			s.sendall("I thought you'd neve ask. My file descriptor is %s." % str(s.fileno()))

		sleep(1)

		return True

	except Exception as e:
		logMethod("socketDoMethod exception with value %s" % e.message)
		return False
		
