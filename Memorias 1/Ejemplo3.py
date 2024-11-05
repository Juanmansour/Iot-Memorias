'''
Practica 3
A través de esta práctica queremos coordinar dos tareas
utilizando las funciones de eventos:
asyncio.Event()
evento.set()
evento.wait()
'''

# Declaracion de librerias
from machine import Pin
import asyncio

# Funcion para hacer parpadear el led
async def blink(led, period_ms, evento):
    led.on()							# Enciende led
    await asyncio.sleep_ms(period_ms)	# Espera 2 segundos
    led.off()							# Apaga led
    await asyncio.sleep_ms(period_ms)	# Espera 2 segundos
    evento.set()						# Se activa el evento

# Funcion que cuenta los segundos que han pasado
async def temporizador(evento):
    count = 0
    await evento.wait()	# Espera a que el evento se active
    while True:
        print(count)
        await asyncio.sleep_ms(1_000)
        count += 1

# Funcion principal
async def main(led2):
    evento = asyncio.Event()						# Crea un evento
    asyncio.create_task(blink(led2, 2_000, evento))	# Llama a la funcion de parpadeo de led					
    asyncio.create_task(temporizador(evento))		# Llama a la funcion que muestra los segundos en pantalla
    await asyncio.sleep_ms(16_000)					# Espera 16 segundos y termina el programa


led = Pin(2, Pin.OUT)	# Declaramos el pin 2 como led
asyncio.run(main(led))	# Ejecutamos funcion principal
