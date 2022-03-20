from models.enum_temperature_unit import TemperatureUnit
from models.temperature import Temperature
from views.main_window import View
from config import Constants
import RPi.GPIO as GPIO
import time
import math
import logging
from .ADCDevice import *

class TemperatureController():
    def __init__(self, temperature: Temperature, view: View):
        self.temperature_model = temperature
        self.old_temperature = 0
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
        
        return round(tempC, 1)
            
    def update_temperature_thread(self, stop):
        while True:
            if stop(): break

            temperature = self.get_temperature()

            if self.old_temperature != temperature:
                unitValue = self.temperature_model.unit
                unit = TemperatureUnit(unitValue).name.lower()
                logging.info('Nouvelle temperature : %s %s', temperature, unit)
                self.old_temperature = temperature
            
            self.temperature_model.value = temperature
            self.view.update_temperature(temperature)

            time.sleep(Constants.TIME_BETWEEN_TEMPERATURE_UPDATE)
        self.adc.close()
        GPIO.cleanup
