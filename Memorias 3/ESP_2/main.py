from machine import Pin

# configuracion GPIO
led=Pin(2, Pin.OUT)

# función que imprime información sobre sobre el tópico y el mensaje recibido
def sub_cb(topic, msg):
    print((topic, msg))

    # activa el led
    led.value(int(msg))

# funcion para conexión al broker y subscripción a tópicos
def connect_and_subscribe():
  global client_id, mqtt_server, topic_sub
  client = MQTTClient(client_id, mqtt_server, user=mqtt_user, password=mqtt_pass)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(topic_sub)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, topic_sub))
  return client

# función para reiniciar el ESP32 si falla al conectarse al broker
def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(10)
  machine.reset()

try:
  # intenta conectarse al broker
  client = connect_and_subscribe()
except OSError as e:
  # en caso de que no pueda conectarse, reinicia el ESP32
  restart_and_reconnect()

while True:
  try:
    # chequea si hay mensajes nuevos y los almacena en una variable
    new_message = client.check_msg()
    #if new_message != 'None':
        #client.publish(topic_pub, b'received')
        #print(new_message)
        #for topic,msg in new_message:
        #print(new_message[1])
    #time.sleep(0.1)
  except OSError as e:
    restart_and_reconnect()
