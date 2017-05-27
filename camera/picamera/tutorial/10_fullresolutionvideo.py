import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (2592, 1944)
    # camera.resolution = camera.MAX_IMAGE_RESOLUTION

    # 1440x1080 para resolucion maxima a 30fps
    
    camera.start_recording('full_res.h264', resize=(1024, 768))
    # esto dara 15fps, reducida la imagen pero con calidad 5MP
    #camera.start_recording('full_res.h264')

    camera.wait_recording(20)
    camera.stop_recording()
