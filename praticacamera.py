'''
from time import sleep
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()
camera.annotate_text = 'Hadler - 11801095\nLucas - 11845726'
# Camera warm-up time

sleep(2)
camera.capture('foo4.jpg')
'''
#'''
import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.start_recording('my_video.h264')
camera.annotate_text = 'Hadler - 11801095\nLucas - 11845726'
camera.wait_recording(5)
camera.stop_recording()
#'''
