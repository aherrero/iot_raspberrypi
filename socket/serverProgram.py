import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.bind(("", 1234))

mysock.listen(5)	#Starts listening for a connect. 5 as number of request allowed to wait for service

while True:
	conn, addr = mysock.accept()

	data = conn.recv(1000)

	if not data:
		break

	print data

	conn.sendall("helloworld from server!")

conn.close()

mysock.close()
