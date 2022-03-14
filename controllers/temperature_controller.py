import RPi.GPIO as GPIO
import time
import math
from threading import Thread
from .ADCDevice import *

class TemperatureController(Thread):
    def __init__(self, temperature, view):
        super().__init__()
        self.temperature_model = temperature
        self.view = view
        self.adc = ADCDevice()
        self.setup()

    def __enter__(self):
        return self

    def __exit__(self):
        self.adc.close()
        GPIO.cleanup()

    def setup(self):
        if(self.adc.detectI2C(0x48)): # Detect the pcf8591.
            self.adc = PCF8591()
        elif(self.adc.detectI2C(0x4b)): # Detect the ads7830
            self.adc = ADS7830()
        else:
            print("No correct I2C address found, \n"
            "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
            "Program Exit. \n")
            exit(-1)

    def get_temperature(self):
        value = self.adc.analogRead(0) # Read ADC value A0 pin
        voltage = value / 255.0 * 3.3 # Calculate voltage
        Rt = 10 * voltage / (3.3 - voltage) # Calculate resistance value of thermistor
        tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0) # Calculate temperature (Kelvin)
        tempC = tempK -273.15 # Calculate temperature (Celsius)
        
        return round(tempC)
            
    def run(self):
        while(True):
            temperature = self.get_temperature() 

            self.temperature_model.value = temperature
            self.view.update_temperature(temperature)

            time.sleep(1)
