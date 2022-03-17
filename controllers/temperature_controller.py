import RPi.GPIO as GPIO
import time
import math
from .ADCDevice import *

TIME_BETWEEN_UPDATE = 1

class TemperatureController():
    def __init__(self, temperature, view):
        self.temperature_model = temperature
        self.view = view
        self.adc = ADCDevice()
        self.setup()

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
        tempK = 1 / (1 / (273.15 + 25) + math.log(Rt / 10) / 3950.0) # Calculate temperature (Kelvin)
        tempC = tempK -273.15 # Calculate temperature (Celsius)
        
        return round(tempC)
            
    def update_temperature_thread(self, stop):
        while True:
            if stop(): break

            temperature = self.get_temperature() 

            self.temperature_model.value = temperature
            self.view.update_temperature(temperature)

            time.sleep(TIME_BETWEEN_UPDATE)
        self.adc.close()
        GPIO.cleanup
