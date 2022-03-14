import RPi.GPIO as GPIO
import time
from threading import Thread

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          # Define the maximum measuring distance, unit: cm
timeOut = MAX_DISTANCE*60   # Calculate timeout according to the maximum measuring distance

class DistanceController(Thread):
    def __init__(self, distance, view):
        super().__init__()
        self.distance_model = distance
        self.view = view
        self.setup()

    def __enter__(self):
        return self

    def __exit__(self):
        GPIO.cleanup()   

    def setup(self):
        GPIO.setmode(GPIO.BOARD) # Use PHYSICAL GPIO Numbering
        GPIO.setup(trigPin, GPIO.OUT) # Set trigPin to OUTPUT mode
        GPIO.setup(echoPin, GPIO.IN) 

    def pulse_in(self, pin,level,timeOut): # Obtain pulse time of a pin under timeOut
        t0 = time.time()

        while(GPIO.input(pin) != level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0
        t0 = time.time()

        while(GPIO.input(pin) == level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0
        pulseTime = (time.time() - t0)*1000000
        
        return pulseTime
    
    def get_distance(self): 
        GPIO.output(trigPin,GPIO.HIGH) # Make trigPin output 10us HIGH level 
        time.sleep(0.00001) # 10us
        GPIO.output(trigPin,GPIO.LOW) # Make trigPin output LOW level 
        pingTime = self.pulse_in(echoPin,GPIO.HIGH,timeOut) # Read plus time of echoPin
        distance = pingTime * 340.0 / 2.0 / 10000.0 # Calculate distance with sound speed 340m/s 
        
        return round(distance)
    
    def run(self):
        while(True):
            distance = self.get_distance() 

            self.distance_model.value = distance
            self.view.update_distance(distance)

            time.sleep(1)
    