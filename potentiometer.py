from picozero import Pot
from time import sleep

dial = Pot(0) # Connected to pin A0 (GP_26)

while True:
    print(dial.value)
    sleep(0.1)
