#!/usr/bin/python
import RPi.GPIO as GPIO
import time

print 'Hello World!'

# Pin definitions
sensorPin = 11

# Pin setup
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme

# Main program loop
print("Here we go! Press CTRL+C to exit")
try:
	while True:
		# Discharge capacitor
		GPIO.setup(sensorPin, GPIO.OUT)
		GPIO.output(sensorPin, GPIO.HIGH)
		time.sleep(0.1)

		GPIO.setup(sensorPin, GPIO.IN)

		if GPIO.input(sensorPin) == GPIO.LOW:
			print 'Detected!'
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
	GPIO.cleanup() # cleanup all GPIO
