from picozero import Pot
from time import sleep

dial = Pot(0) # Forbundet til pin A0 (GPIO26)

while True:
    print(dial.value)
    sleep(0.1)
