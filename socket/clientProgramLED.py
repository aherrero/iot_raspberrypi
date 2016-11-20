import socket
import sys

textToSend = "default"
if len(sys.argv) > 1:
	textToSend = sys.argv[1]

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = socket.gethostname()	#empty means local machine
host = "192.168.1.15"
mysock.connect((host, 7777))

print textToSend
mysock.sendall(textToSend)
data = mysock.recv(1000)

print data
mysock.close()
