import time
from umqttsimple import MQTTClient
import ubinascii
from machine import Pin, unique_id
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

# configuración
ssid = 'IOTNET_2.4'
password = '10T@ATC_'
mqtt_server = '192.168.2.28'
mqtt_user = ""
mqtt_pass = ""

# suscripción a tópicos 
client_id = ubinascii.hexlify(unique_id())
topic_sub = b'notification'
topic_pub = b'hello'

# variables para manejar el tiempo
last_message = 0
message_interval = 5
counter = 0

# conexión a la red
station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
