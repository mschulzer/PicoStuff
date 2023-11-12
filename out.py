from machine import Pin, PWM

gpiopin = 16
pwm = PWM(Pin(gpiopin))
pwm.freq(1000)


# Brug værdier mellem 10000 (0.5V) --> 60000 (3V)
# Spring på 10000 svarer til ca. 0.5 V

pwm.duty_u16(60000)
