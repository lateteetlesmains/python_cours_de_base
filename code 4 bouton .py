import neopixel
import machine
from machine import TouchPad, Pin
from time import sleep
from neopixel import NeoPixel

PIN = 5

touch1 = TouchPad(Pin(13))
touch2= TouchPad(Pin(15))
touch3 = TouchPad(Pin(2))
touch4 = TouchPad(Pin(0))

pixels = neopixel.NeoPixel(machine.Pin(5), 28)   

for i in range(28):
        pixels[i] = (0, 0, 255)
        pixels.write()
sleep(0.5)
for i in range(28):
        pixels[i] = (255, 255, 255)
        pixels.write()
sleep(0.5)
for i in range(28): 
        pixels[i] = (255, 0, 0)
        pixels.write()
sleep(0.5)            
for i in range(28):  # set all 7 pixels to red
        pixels[i] = (0, 0, 0)
        pixels.write()
sleep(0.5)

while True:
    
    #sleep(0.5)
    if touch1.read() < 100:
        print(touch1.read())
        for i in range(28):  
            pixels[i] = (255, 0, 0)
            pixels.write()
        sleep(0.5)
    if touch2.read() < 100:
        print(touch2.read())
        for i in range(28):  
            pixels[i] = (0, 255, 0)
            pixels.write()
        sleep(0.5)
    if touch3.read() < 100:
        print(touch3.read())
        for i in range(28):  
            pixels[i] = (0, 0, 255)
            pixels.write()
        sleep(0.5)
    if touch4.read() < 100:
        print(touch4.read())
        for i in range(28):  
            pixels[i] = (255, 255, 255)
            pixels.write()
        sleep(0.5)