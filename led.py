import machine
from time import sleep

led = machine.Pin("LED", machine.Pin.OUT)
led.off()

while True:
  led.on()
  sleep(1)
  led.off()
  sleep(1)
