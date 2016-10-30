import threading
import threadHandeling


class threadHandeler(object):
	""" Class for handeling threads """

	def __init__(self, logMethod = threadHandeling.logMethod):
		self.threads = []
		self.logMethod = logMethod

	def startThread(self, method, args = False):
		''' Start new thread '''

		self.logMethod("Creating new thread")

		try:
			if args:
				newThread = threading.Thread(target = method, args = args)
			else:
				newThread = threading.Thread(target = method)
				
			newThread.start()
			self.threads.append(newThread)

		except Exception as e:
			self.logMethod("startThread creation exception with value %s" % e.message)
			

	def joinThreads(self, timeout=10.0):
		''' Wait for threads to end (with timeout) '''

		self.logMethod("Waiting for threads to close with %s second timeout" % str(timeout))

		try:
			for thread in self.threads:
				thread.join(timeout)

		except Exception as e:
			self.logMethod("stopAllThreads creation exception with value %s" % e.message)