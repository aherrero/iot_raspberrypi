import time
import picamera

# Explicitly open a new file called my_image.jpg
my_file = open('my_image.jpg', 'wb')
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture(my_file)
# Note that at this point the data is in the file cache, but may
# not actually have been written to disk yet
my_file.close()
# Now the file has been closed, other processes should be able to
# read the image successfully
