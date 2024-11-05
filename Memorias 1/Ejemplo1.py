import asyncio

async def blink(led, period_ms):
    while True:
        led.on()
        await asyncio.sleep_ms(2_000)
        led.off()
        await asyncio.sleep_ms(period_ms)

async def main(led2):
    asyncio.create_task(blink(led2, 2_000))
    await asyncio.sleep_ms(16_000)

# Running on a generic board
from machine import Pin
led = Pin(2, Pin.OUT)
asyncio.run(main(led))