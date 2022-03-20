import logging
from models.enum_control_state import ControlState
from models.enum_motor_direction import MotorDirection

class MotorStatus:
    def __init__(self, state: ControlState, 
    direction: MotorDirection, speed: int):
        self.__state = state
        self.__direction = direction
        self.__speed = speed

    @property
    def state(self) -> ControlState:
        return self.__state

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

    @direction.setter
    def direction(self, new_direction: MotorDirection):
        direction = MotorDirection(new_direction).name.lower()
        logging.info('Direction du moteur : %s', direction)
        self.__direction = new_direction

    @speed.setter
    def speed(self, new_speed: int):
        logging.info('Vitesse du moteur : %s', new_speed)
        self.__speed = new_speed
        