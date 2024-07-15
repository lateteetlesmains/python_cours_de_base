import neopixel
import machine
from machine import Pin

PIN = 5

np = neopixel.NeoPixel(machine.Pin(5), 7)

while True:
    for i in range(7):
        np[i] = (128, 120, 0) 
        np.write()
         