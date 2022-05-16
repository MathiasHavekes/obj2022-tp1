import logging
from models.enums.enum_control_state import ControlState
from models.enums.enum_motor_direction import MotorDirection
from config import Constants

class MotorStatus:
    def __init__(self, 
    state = Constants.DEFAULT_MOTOR_STATE, 
    target = Constants.DEFAULT_DOOR_OPEN_PERCENTAGE,
    direction = 0, speed = 0):
        self.__state = state
        self.__target = target
        self.__direction = direction
        self.__speed = speed

    @property
    def state(self) -> ControlState:
        return self.__state

    @property
    def target(self) -> int:
        return self.__target

    @property
    def direction(self) -> MotorDirection:
        return self.__direction

    @property
    def speed(self) -> int:
        return self.__speed

    @state.setter
    def state(self, new_state: ControlState):
        state = ControlState(new_state).name.lower()
        logging.info('Selection du mode : %s', state)
        self.__state = new_state

    @target.setter
    def target(self, new_target: int):
        logging.info('Valeur d\'ouverture de porte entree : %s', new_target)
        self.__target = new_target

    @direction.setter
    def direction(self, new_direction: MotorDirection):
        direction = MotorDirection(new_direction).name.lower()
        logging.info('Direction du moteur : %s', direction)
        self.__direction = new_direction

    @speed.setter
    def speed(self, new_speed: int):
        logging.info('Vitesse du moteur : %s tour/min', new_speed)
        self.__speed = new_speed
        