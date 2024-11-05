'''
Practica 2
Este codigo consiste en hacer un programa de ejecucion asíncrona,
por un lado enciende un led y por otro lado muestra en pantalla
un contador de cuantos segundos han pasado, ambas al mismo tiempo.
'''

# Declaracion de librerias
from machine import Pin
import asyncio

# Funcion para hacer parpadear el led
async def blink(led, period_ms):
    while True:
        led.on()							# Enciende led
        await asyncio.sleep_ms(period_ms)	# Espera 2 segundos
        led.off()							# Apaga led
        await asyncio.sleep_ms(period_ms)	# Espera 2 segundos

# Funcion que cuenta los segundos que han pasado
async def temporizador():
    count = 0
    while True:
        print(count)
        await asyncio.sleep_ms(1_000)
        count += 1

# Funcion principal
async def main(led2):
    asyncio.create_task(blink(led2, 2_000))	# Llama a la funcion de parpadeo de led
    asyncio.create_task(temporizador())		# Llama a la funcion que muestra los segundos en pantalla
    await asyncio.sleep_ms(16_000)			# Espera 16 segundos y termina el programa


led = Pin(2, Pin.OUT)	# Declaramos el pin 2 como led
asyncio.run(main(led))	# Ejecutamos funcion principal

