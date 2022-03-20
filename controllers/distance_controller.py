from models.distance import Distance
from views.main_window import View
from config import Constants
from utils import Utils
import RPi.GPIO as GPIO
import time

class DistanceController():
    def __init__(self, distance: Distance, view: View):
        self.__distance_model = distance
        self.__view = view
        self.__old_distance = 0
        self.__time_out = Constants.MAX_DISTANCE_MEASURING * 60
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD) # Use PHYSICAL GPIO Numbering
        GPIO.setup(Constants.TRIG_PIN, GPIO.OUT) # Set trigPin to OUTPUT mode
        GPIO.setup(Constants.ECHO_PIN, GPIO.IN) 

    def pulse_in(self, pin, level): # Obtain pulse time of a pin under timeOut
        t0 = time.time()

        while(GPIO.input(pin) != level):
            if((time.time() - t0) > self.__time_out * 0.000001):
                return 0
        t0 = time.time()

        while(GPIO.input(pin) == level):
            if((time.time() - t0) > self.__time_out * 0.000001):
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

            if distance < Constants.MIN_DISTANCE or distance > Constants.MAX_DISTANCE: continue

            if self.__old_distance != distance: 
                self.__old_distance = distance
            else: continue
            
            self.__distance_model.value = distance
            self.__view.update_distance(self.__distance_model)

            distance_percentage = Utils.castValue(distance, 0, 100, 
                Constants.MIN_DISTANCE, Constants.MAX_DISTANCE)
            self.__view.update_open_percentage(distance_percentage)

            time.sleep(Constants.TIME_BETWEEN_DISTANCE_UPDATE)
        GPIO.cleanup
