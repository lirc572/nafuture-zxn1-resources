import machine
LED = machine.Pin(12, machine.Pin.OUT)
LEDP = machine.PWM(LED)
LEDP.freq(500)
LEDP.duty(1023)

import time
from sensor import Sensor
s = Sensor()
t = s.getTemperature()
h = s.getHumidity()
from battery import Battery
b = Battery()
v = b.getVoltage()
reading_str = 't:{0}°C, h:{1}%, v:{2:.1f}V'.format(t, h, v)

import network
sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active(False)
ap_if.active(True)
ap_if.config(essid='ESP: '+reading_str, password='helloworld')
print(reading_str)

LEDP.duty(256)