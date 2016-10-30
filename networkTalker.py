#!/usr/bin/python

import tcpNetwork
import tcpNetwork.connecting
import tcpNetwork.serving
import tcpNetwork.socketKeeping

import threadHandeling.threadKeeping

import actualProgram.talker


threader = threadHandeling.threadKeeping.threadHandeler()
server = tcpNetwork.serving.networkingServer(threadMethod = threader.startThread)
socketHandle = tcpNetwork.socketKeeping.socketHandeler(actualProgram.talker.socketDoMethod)

COMMANDS = {'q':'quit',
			'c':'connect',
			'h':'help'}

port = 8008


if __name__ == "__main__":

	threader.startThread(server.runServer, args = (port, socketHandle.handleSocket))

	while True:

		try:
			userInput = raw_input("\nq,c,h>")

			if userInput == 'h':
				for command in COMMANDS:
					tcpNetwork.logMethod("\t%s: %s" % (command, COMMANDS[command]))

			if userInput == 'q':
				tcpNetwork.logMethod("Quitting")
				server.stopServer = True
				socketHandle.stopSockets = True
				break

			if userInput == 'c':
				ip = raw_input("Connect to ip: ")
				s = tcpNetwork.connecting.connectTo(ip, port)
				threader.startThread(socketHandle.handleSocket, args = (s,))
		
		except Exception as e:
				tcpNetwork.logMethod("Main loop exception with value %s" % e.message)
				break

	threader.joinThreads()