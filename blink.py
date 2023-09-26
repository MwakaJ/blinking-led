from machine import pin
from time import sleep

led =pin(5, pin.out)

while True:
    led.value(1)
    sleep(.5)
    led.value(0)
    sleep(.5)