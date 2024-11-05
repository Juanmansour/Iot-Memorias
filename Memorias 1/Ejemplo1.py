'''
Practica 1
Este codigo es el primer contacto con la libreria asyncio,
este programa consiste simplemente en encender y apagar un led
utilizando la libreria.
'''

# Declaracion de librerias
from machine import Pin
import asyncio

# Funcion para hacer parpadear el led
async def blink(led, period_ms):
    while True:
        led.on()							# Enciende led
        await asyncio.sleep_ms(2_000)		# Espera 2 segundos
        led.off()							# Apaga led
        await asyncio.sleep_ms(period_ms)	# Espera 2 segundos
        
# Funcion principal
async def main(led2):
    asyncio.create_task(blink(led2, 2_000))	# Llama a funcion de parpadeo de led
    await asyncio.sleep_ms(16_000)			# Espera 16 segundos y termina el programa


led = Pin(2, Pin.OUT)	# Declaramos el pin 2 como led
asyncio.run(main(led))	# Ejecutamos funcion principal