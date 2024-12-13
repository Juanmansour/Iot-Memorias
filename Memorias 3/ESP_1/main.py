# configuracion GPIO
button = Pin(4, Pin.IN, Pin.PULL_DOWN)

# funcion callback
def sub_cb(topic, msg):
  print((topic, msg))
  if topic == b'notification' and msg == b'received':
    print('ESP received hello message')

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

# recepcion y puclicado de mensajes
while True:
  try:
    client.check_msg()
    if (time.time() - last_message) > message_interval:
      # verifica el estado del pulsador
      if button.value() == 1:
        print("Botón precionado")
        msg = "1"  
      else:
        msg = "0"
      # envia un mensaje con el estado del pulsador
      client.publish(topic_pub, msg)
      last_message = time.time()
      counter += 1
      
  # en caso de que ocurra algo inesperado, reinicia el ESP32
  except OSError as e:
    restart_and_reconnect()
