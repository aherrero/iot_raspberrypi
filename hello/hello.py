#!/usr/bin/python
import RPi.GPIO as GPIO
import time

print 'Hello World!'

# Pin definitions
ledPin = 11
butPin = 12
pwmPin = 13
dc = 95 # duty cycle (0-100) for PWM pin

# Pin setup
GPIO.setmode(GPIO.BOARD) # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output
GPIO.setup(pwmPin, GPIO.OUT) # PWM pin set as output

pwm = GPIO.PWM(pwmPin, 50)  # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

# Initial state for LEDs:
GPIO.output(ledPin, GPIO.LOW)
pwm.start(dc)

print("Here we go! Press CTRL+C to exit")
try:
    while 1:
        if GPIO.input(butPin): # button is released
            pwm.ChangeDutyCycle(0)
            GPIO.output(ledPin, GPIO.LOW)
	    dc = 0
        else: # button is pressed:
	    dc = dc + 10
	    if dc > 100:
		dc = 100
		pwm.ChangeDutyCycle(dc)
            GPIO.output(ledPin, GPIO.HIGH)
            time.sleep(0.075)
            GPIO.output(ledPin, GPIO.LOW)
            time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO
