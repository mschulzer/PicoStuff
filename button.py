from machine import Pin
import time

#led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value():
	    #led.toggle()
	    print('button clicked')
	    time.sleep(0.5)
