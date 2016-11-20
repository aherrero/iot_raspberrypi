#

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname("www.google.com")

print host

mysock.connect((host, 80))

message = "GET / HTTP/1.1\r\n\r\n"

mysock.sendall(message)

data = mysock.recv(1000)	#Wait until response (1000 bytes expected to receive)
print data
mysock.close()
