from mqtt_as import MQTTClient, config
from machine import Pin
import uasyncio as asyncio

# Variables
pir = Pin(22, Pin.IN, Pin.PULL_DOWN)

async def messages(client):
    async for topic, msg, retained in client.queue:
        print(f'[CAPA APLICACIÓN] Topic: "{topic.decode()}" Message: "{msg.decode()}" Retained: {retained}')


async def down(client):
    while True:
        await client.down.wait()  
        client.down.clear()
        print('[CAPA COMUNICACIÓN] Conexion MQTT cerrada')

async def up(client):
    while True:
        await client.up.wait()
        client.up.clear()
        print('[CAPA COMUNICACIÓN] Conexion MQTT establecida')
        
        # (re) suscripciones (tras evento de conexión o reconexión)
        for s in SUBS: 
            await client.subscribe(s, 1)

async def sensor(client):
    print('[CAPA PERCEPCIÓN] Sensor iniciado ...')
    while True:
        await asyncio.sleep(0.3)
        print(f'[CAPA PERCEPCION] Pir={pir.value()}')
        await client.publish('led', f"{pir.value()}", qos = 1)


async def main(client):
    try:
        print('[CAPA COMUNICACIÓN] Iniciando conexion...')
        await client.connect()
        print('[CAPA COMUNICACIÓN] Conexión establecida')
    except OSError:
        print('[CAPA COMUNICACIÓN] Conexión fallida')
        return
    for task in (up, down, messages):
        asyncio.create_task(task(client))
        
    # crear aquí las tareas que sean necesarias
    await sensor(client) 
    
if __name__ == '__main__':
    
    # configuración
    config['server'] = '192.168.2.5'
    config['ssid'] = 'IOTNET_2.4'
    config['wifi_pw'] = '10T@ATC_'
    config["user"]= ""
    config["password"]= ""
    config['keepalive'] = 120
    config["queue_len"]= 5
    config['will'] = ('topic_final', 'Mensaje de finalizacion', False, 0)

    # suscripciones
    SUBS = ('led')

    # configuración y creación de la clase cliente
    MQTTClient.DEBUG = True
    client = MQTTClient(config)

    # ejecución de la rutina main
    try:
        asyncio.run(main(client))
    finally:
        client.close()
        asyncio.new_event_loop()
