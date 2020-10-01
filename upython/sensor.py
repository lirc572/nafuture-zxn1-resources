import machine
import dht
import time

'''
Usage:

from sensor import Sensor
s = Sensor()
s.getTemperature()
s.getHumidity()
'''

class Sensor:
    def __init__(self, pin = 4):
        self.pin = pin
        self.sensor = sensor = dht.DHT11(machine.Pin(4))
        self.tms = 0
    def measure(self):
        self.sensor.measure()
        while not self.sensor.humidity():
            time.sleep_ms(1200)
    def getTemperature(self):
        self.measure()
        return self.sensor.temperature()
    def getHumidity(self):
        self.measure()
        return self.sensor.humidity()
