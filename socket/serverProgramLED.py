import RPi.GPIO as GPIO
import socket

# Pin setup
ledPin = 11
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
portNumber = 7777
mysock.bind(("", portNumber))
mysock.listen(5)	#Starts listening for a connect. 5 as number of request allowed to wait for service

print 'Listen connections from port ' + str(portNumber)

try:
	while True:
		conn, addr = mysock.accept()

		data = conn.recv(1000)

		if not data:
			break
		
		if data == b'on':
			GPIO.output(ledPin, True)
			conn.sendall("LED ON!")
		elif data== b'off':
			GPIO.output(ledPin, False)
			conn.sendall("LED OFF!")
		else:
			conn.sendall("Nothing happend")
		
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    GPIO.cleanup() # cleanup all GPIO
    conn.close()
mysock.close()
