import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()	#empty means local machine
mysock.connect((host, 1234))

mysock.sendall("Helloworld from client!")
data = mysock.recv(1000)

print data
mysock.close()
