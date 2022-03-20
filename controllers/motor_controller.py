from models.enum_control_state import ControlState
from models.motor_status import MotorStatus
from models.temperature import Temperature
from models.distance import Distance
from views.main_window import View
from config import Constants
import RPi.GPIO as GPIO
import time 

class MotorController():
    def __init__(self, motor_status: MotorStatus, 
    temperature: Temperature, distance: Distance, view: View):
        self.motor_status_model = motor_status
        self.temperature_model = temperature
        self.distance_model = distance
        self.view = view
        self.setup()

    def setup(self):    
        GPIO.setmode(GPIO.BOARD)    
        for pin in Constants.MOTOR_PINS:
            GPIO.setup(pin,GPIO.OUT)

    # As for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
    def moveOnePeriod(self, direction, ms):    
        for j in range(0,4,1):      # Cycle for power supply order
            for i in range(0,4,1):  # Assign to each pin
                if (direction == 1):# Power supply order clockwise
                    GPIO.output(Constants.MOTOR_PINS[i],((Constants.CCW_STEP[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
                else :              # Power supply order anticlockwise
                    GPIO.output(Constants.MOTOR_PINS[i],((Constants.CW_STEP[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            if(ms<3): # The delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
                ms = 3
            time.sleep(ms*0.001)    
        
    def moveSteps(self, direction, ms, steps):
        for i in range(steps):
            self.moveOnePeriod(direction, ms)
        
    def motorStop(self):
        for i in range(0,4,1):
            GPIO.output(Constants.MOTOR_PINS[i],GPIO.LOW)
            
    def loop(self):
        self.moveSteps(1,3,1024)  # Rotating 360 deg clockwise, a total of 2048 steps in a circle, 512 cycles
        time.sleep(0.5)
        self.moveSteps(0,3,1024)  # Rotating 360 deg anticlockwise
        time.sleep(0.5)

    def update_motor_state(self, new_motor_state):
        self.motor_status_model.state = new_motor_state
        print(new_motor_state)
        
    def state_machine_thread(self, stop):
        while True:
            if stop(): break
            elif self.motor_status_model.state == ControlState.AUTOMATIC:
                temperature = self.temperature_model.value
                #self.calculateOpenDistanceWithTemp(temperature)
                continue
            elif self.motor_status_model.state == ControlState.MANUAL:
                continue
            elif self.motor_status_model.state == ControlState.OPEN_DOOR:
                continue
            elif self.motor_status_model.state == ControlState.CLOSE_DOOR:
                continue
        GPIO.cleanup