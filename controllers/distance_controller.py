from models.enum_distance_units import DistanceUnits
import RPi.GPIO as GPIO
import time
import logging

TRIG_PIN = 16
ECHO_PIN = 18
SOUND_SPEED = 340 # En m/s
MAX_DISTANCE = 50 # Define the maximum measuring distance, unit: cm
TIME_BETWEEN_UPDATE = 1 # En secondes

class DistanceController():
    def __init__(self, distance, view):
        self.distance_model = distance
        self.view = view
        self.old_distance = 0
        self.time_out = MAX_DISTANCE * 60
        self.setup()

    def setup(self):
        GPIO.setmode(GPIO.BOARD) # Use PHYSICAL GPIO Numbering
        GPIO.setup(TRIG_PIN, GPIO.OUT) # Set trigPin to OUTPUT mode
        GPIO.setup(ECHO_PIN, GPIO.IN) 

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
        GPIO.output(TRIG_PIN, GPIO.HIGH) # Make trigPin output 10us HIGH level 
        time.sleep(0.00001) # 10us
        GPIO.output(TRIG_PIN, GPIO.LOW) # Make trigPin output LOW level 
        ping_time = self.pulse_in(ECHO_PIN, GPIO.HIGH) # Read plus time of echoPin
        distance = ping_time * SOUND_SPEED / 2.0 / 10000.0 # Calculate distance with sound speed 340m/s 
        
        return round(distance, 1)
    
    def update_distance_thread(self, stop):
        while True:
            if stop(): break

            distance = self.get_distance() 
            max_distance = self.distance_model.max_value
            min_distance = self.distance_model.min_value

            if distance > max_distance or distance < min_distance: continue

            distance_percentage = self.calculateOpenPercentage(distance, max_distance, min_distance)

            if self.old_distance != distance:
                unitValue = self.distance_model.unit
                unit = DistanceUnits(unitValue).name.lower()
                logging.info('Nouvelle distance d\'ouverture : %s %s ~ %s%%', 
                distance, unit, distance_percentage)
                self.old_distance = distance
            
            self.distance_model.value = distance
            self.view.update_distance(distance)
            self.view.update_open_percentage(distance_percentage)

            time.sleep(TIME_BETWEEN_UPDATE)
        GPIO.cleanup

    """
    Fonction qui calcul la distance d'ouverture de la porte en pourcentage 
    avec une fonction de type : y = ax + b
    On trouve a avec les points extremes :
    a = (y_b - y_a) / (x_b - x_a)
    b = -(ax - y)
    """
    def calculateOpenPercentage(self, distance, max_distance, min_distance) -> int:
        gradient = 100 / (max_distance - min_distance)

        intercept = - (gradient * max_distance - 100)

        return round(gradient * distance + intercept)
