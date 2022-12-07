# Bibliotecas para API
import json
from requests import get
from pprint import pprint
##

# Biblioteacas para Camera
from time import sleep
#from picamera import PiCamera
##

# API
endereco = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'
id_baseMeteorologica = 966583;
endereco += str(id_baseMeteorologica)

meuClima = get(endereco).json()['items']

pprint(meuClima)

temperatura = meuClima[0]['ambient_temp']
print(f'Temperatura: {temperatura}°C')
##

# Camera
with PiCamera as camera:
  camera.annotate_text = 'Hadler - 11801095\nLucas - 11845726'
  
  # Foto
  camera.resolution = (1024, 768)
  camera.start_preview()
  sleep(2)
  camera.capture('foto.jpg')
  camera.stop_preview()
  ##

  # Video
  camera.resolution = (640, 480)
  camera.start_recording('video.h264')
  camera.wait_recording(5)
  camera.stop_recording()
  ##
##