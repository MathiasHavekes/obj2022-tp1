from models.enum_control_state import ControlState
from models.enum_motor_direction import MotorDirection

class MotorStatus:
    def __init__(self, state: ControlState, 
    direction: MotorDirection, speed: int):
        self._state = state
        self._direction = direction
        self._speed = speed

    @property
    def state(self) -> ControlState:
        return self._state

    @property
    def direction(self) -> MotorDirection:
        return self._direction

    @property
    def speed(self) -> int:
        return self._speed

    @state.setter
    def state(self, new_state: ControlState):
        self._state = new_state

    @direction.setter
    def direction(self, new_direction: MotorDirection):
        self._direction = new_direction

    @speed.setter
    def speed(self, new_speed: int):
        self._speed = new_speed
        