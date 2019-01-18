from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.rotation = 180

camera.start_preview(fullscreen =False,window = (100,150,1024,768))

for i in range(5):
    sleep(2)
    camera.capture('/home/pi/test/picture%s.jpg'%i)

camera.stop_preview()