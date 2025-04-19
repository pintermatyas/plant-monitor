import random
from time import sleep
from prometheus_client import start_http_server, Gauge
import logging
import adafruit_dht
import board

air_humidity = Gauge('air_humidity_percentage', 'Air Humidity Percentage (Inside)')
air_temperature = Gauge('air_temperature', 'Air Tempearature (Inside)')

device = adafruit_dht.DHT22(board.D4)

def read_values():
    while True:
        try:
            humidity, temperature = device.humidity, device.temperature
            print("Temp:{:.1f} C    Humidity: {}%".format(temperature, humidity))
            air_humidity.set(humidity)
            air_temperature.set(temperature)
        except:
            print("Something went wrong")
        sleep(5)

if __name__ == "__main__":
    start_http_server(8001)
    read_values()
