from models.enum_distance_unit import DistanceUnit
from models.distance import Distance
from views.main_window import View
from config import Constants
from utils import Utils
import RPi.GPIO as GPIO
import time
import logging

class DistanceController():
    def __init__(self, distance: Distance, view: View):
        self.distance_model = distance
        self.view = view
        self.old_distance = 0
        self.time_out = Constants.MAX_DISTANCE_MEASURING * 60
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD) # Use PHYSICAL GPIO Numbering
        GPIO.setup(Constants.TRIG_PIN, GPIO.OUT) # Set trigPin to OUTPUT mode
        GPIO.setup(Constants.ECHO_PIN, GPIO.IN) 

    def pulse_in(self, pin, level): # Obtain pulse time of a pin under timeOut
        t0 = time.time()

        while(GPIO.input(pin) != level):
            if((time.time() - t0) > self.time_out * 0.000001):
                return 0
        t0 = time.time()

        while(GPIO.input(pin) == level):
            if((time.time() - t0) > self.time_out * 0.000001):
                return 0
        pulse_time = (time.time() - t0) * 1000000
        
        return pulse_time
    
    def get_distance(self): 
        GPIO.output(Constants.TRIG_PIN, GPIO.HIGH) # Make trigPin output 10us HIGH level 
        time.sleep(0.00001) # 10us
        GPIO.output(Constants.TRIG_PIN, GPIO.LOW) # Make trigPin output LOW level 
        ping_time = self.pulse_in(Constants.ECHO_PIN, GPIO.HIGH) # Read plus time of echoPin
        distance = ping_time * Constants.SOUND_SPEED / 2.0 / 10000.0 # Calculate distance with sound speed 340m/s 
        
        return round(distance, 1)
    
    def update_distance_thread(self, stop):
        while True:
            if stop(): break

            distance = self.get_distance() 
            max_distance = Constants.MAX_DISTANCE
            min_distance = Constants.MIN_DISTANCE

            if distance > max_distance or distance < min_distance: continue

            distance_percentage = Utils.castToPercentage(distance, max_distance, min_distance)

            if self.old_distance != distance:
                unitValue = self.distance_model.unit
                unit = DistanceUnit(unitValue).name.lower()
                logging.info('Nouvelle distance d\'ouverture : %s %s ~ %s%%', 
                distance, unit, distance_percentage)
                self.old_distance = distance
            
            self.distance_model.value = distance
            self.view.update_distance(distance)
            self.view.update_open_percentage(distance_percentage)

            time.sleep(Constants.TIME_BETWEEN_DISTANCE_UPDATE)
        GPIO.cleanup
