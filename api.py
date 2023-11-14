import network
import urequests
from machine import Pin, PWM
from time import sleep

# Initier WiFi
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = '...'
password = '...'

wlan.connect(ssid, password)


# Initier PIN og PWM
pwm = PWM(Pin(16))
pwm.freq(1000)


# Hent data fra API (EnergiNet)
url = 'https://api.energidataservice.dk/dataset/ElectricityProdex5MinRealtime?limit=5'
response = urequests.get(url)
result = response.json()


while True:
    records = result.get('records', [])
    val = [record['SolarPower'] for record in records]
    pwm.duty_u16(val+10000)
    
    sleep(10) # gentag hvert 10. sekund
