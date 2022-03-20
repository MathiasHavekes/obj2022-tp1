from math import dist
from turtle import distance, update
from models.enum_control_state import ControlState
from models.enum_motor_direction import MotorDirection
from models.motor_status import MotorStatus
from models.temperature import Temperature
from models.distance import Distance
from utils import Utils
from views.main_window import View
from config import Constants
from .PID import PID
import RPi.GPIO as GPIO
import logging
import time 

class MotorController():
    def __init__(self, motor_status: MotorStatus, 
    temperature: Temperature, distance: Distance, view: View):
        self.__motor_status_model = motor_status
        self.__temperature_model = temperature
        self.__distance_model = distance
        self.__open_percentage = Constants.DEFAULT_DOOR_OPEN_PERCENTAGE
        self.__view = view
        self.__target = 0.0
        self.setup()

    def setup(self): 
        GPIO.setmode(GPIO.BOARD)    
        for pin in Constants.MOTOR_PINS:
            GPIO.setup(pin,GPIO.OUT)

        self.pid = PID(
            Constants.PID_SETUP[0], 
            Constants.PID_SETUP[1], 
            Constants.PID_SETUP[2])

    # As for four phase stepping motor, four steps is a cycle. the function is used to drive the stepping motor clockwise or anticlockwise to take four steps    
    def move_one_period(self, direction, ms):    
        for j in range(0,4,1):      # Cycle for power supply order
            for i in range(0,4,1):  # Assign to each pin
                if (direction == 1):# Power supply order clockwise
                    GPIO.output(Constants.MOTOR_PINS[i],((Constants.CCW_STEP[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
                else :              # Power supply order anticlockwise
                    GPIO.output(Constants.MOTOR_PINS[i],((Constants.CW_STEP[j] == 1<<i) and GPIO.HIGH or GPIO.LOW))
            if(ms<3): # The delay can not be less than 3ms, otherwise it will exceed speed limit of the motor
                ms = 3
            time.sleep(ms*0.001)    
        
    def move_steps(self, direction, ms, steps):
        for i in range(steps):
            self.move_one_period(direction, ms)
        
    def motor_stop(self):
        for i in range(0,4,1):
            GPIO.output(Constants.MOTOR_PINS[i], GPIO.LOW)
            
    def update_motor_state(self, new_motor_state: MotorStatus):
        self.__motor_status_model.state = new_motor_state

    def update_open_percentage(self, new_open_percentage: int):
        logging.info('Valeur d\'ouverture de porte entree : %s', new_open_percentage)
        self.__open_percentage = new_open_percentage
        
    def state_machine_thread(self, stop):
        while True:
            destination = 0.0

            if stop(): break
            elif self.__motor_status_model.state == ControlState.AUTOMATIQUE:
                temperature = self.__temperature_model.value
                destination = round(Utils.castValue(
                    temperature,
                    Constants.MIN_DISTANCE,
                    Constants.MAX_DISTANCE,
                    Constants.MIN_TEMPERATURE,
                    Constants.MAX_TEMPERATURE))
            elif self.__motor_status_model.state == ControlState.MANUEL:
                destination = round(Utils.castValue(
                    self.__open_percentage, 
                    Constants.MIN_DISTANCE, 
                    Constants.MAX_DISTANCE, 
                    0, 100))
            elif self.__motor_status_model.state == ControlState.OUVRIR_PORTE:
                destination = Constants.MAX_DISTANCE
            elif self.__motor_status_model.state == ControlState.FERMER_PORTE:
                destination = Constants.MIN_DISTANCE
            self.pid.SetPoint = destination
            distance = self.__distance_model.value
            self.pid.update(distance)
            speed = int(self.pid.output)
            direction = MotorDirection.ARRET.value

            if speed < 0:
                self.__motor_status_model.direction = MotorDirection.BAS
                direction = self.__motor_status_model.direction.value
            elif speed > 0:
                self.__motor_status_model.direction = MotorDirection.HAUT
                direction = self.__motor_status_model.direction.value
            else:
                self.__motor_status_model.direction = MotorDirection.ARRET

            speed = abs(speed)

            self.__view.update_rotation_speed(speed)
            self.__view.update_rotation_direction(direction)

            if direction != MotorDirection.ARRET.value: self.move_steps(direction, 3, speed)

            time.sleep(0.5)
        GPIO.cleanup

    def config(self):
        global pid_target
        self.pid.SetPoint = self.__target
        pid_target = self.pid.SetPoint
        self.pid.setKp(Constants.PID_SETUP[0])
        self.pid.setKi(Constants.PID_SETUP[1])
        self.pid.setKd(Constants.PID_SETUP[2])
