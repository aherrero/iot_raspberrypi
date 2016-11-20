import RPi.GPIO as GPIO
import time
import picamera

print 'hello'

camera = picamera.PiCamera()

camera.capture('image.jpg')

camera.start_preview()

time.sleep(10)

camera.stop_preview()
