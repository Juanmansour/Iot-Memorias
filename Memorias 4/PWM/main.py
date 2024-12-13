from machine import Pin, PWM, ADC
from time import sleep

# Frecuencia para el PWM
frequency = 5000

# Configura el pin 4 como salida PWM
led = PWM(Pin(4), frequency)

# Configura el pin 15 como entrada analógica
pot = ADC(Pin(15))
pot.atten(ADC.ATTN_11DB)

while True:
    # Lee y escala el valor del potenciómetro
    pot_value = pot.read() / 4095 * 1023 

    # Ajusta el ciclo de trabajo del PWM
    led.duty(int(pot_value))

    # Pausa de 5 ms
    sleep(0.005)