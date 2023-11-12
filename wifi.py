import network

ssid = '...'
password = '...'


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

if wlan.isconnected():
    print(wlan.ifconfig())
