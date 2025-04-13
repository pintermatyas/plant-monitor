import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import random
from time import sleep
from prometheus_client import start_http_server, Gauge
import logging

percentage_gauge = Gauge('soil_humidity_percentage', 'Simulated soil humidity percentage')
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D5) # GPIO8 pin
mcp = MCP.MCP3008(spi, cs)
chan = AnalogIn(mcp, MCP.P0) # CH0 pin of ADC

max_saturation_voltage = 1.4 # Sensor submerged in water
min_saturation_voltage = 3.05 # Sensor completely dry

def read_percentage():
    voltage = chan.voltage
    saturation_percentage = (voltage - max_saturation_voltage) * 100 / (min_saturation_voltage/max_saturation_voltage)
    percentage = 100 - saturation_percentage
    print(percentage)
    percentage_gauge.set(percentage)

if __name__ == "__main__":
    start_http_server(8000)
    while True:
        read_percentage()
        sleep(1)
