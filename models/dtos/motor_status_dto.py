from models.enums.enum_control_state import ControlState
from models.enums.enum_motor_direction import MotorDirection
from models.motor_status import MotorStatus

class MotorStatusDto:
    def __init__(self, motor_status: MotorStatus):
        self.__type = 'motor_status'
        self.__state = ControlState(motor_status.state).name.lower()
        self.__target = motor_status.target
        self.__direction = MotorDirection(motor_status.direction).name.lower()
        self.__speed = motor_status.speed

    @property
    def type(self) -> str:
        return self.__type

    @property
    def state(self) -> str:
        return self.__state

    @property
    def target(self) -> int:
        return self.__target

    @property
    def direction(self) -> str:
        return self.__direction

    @property
    def speed(self) -> int:
        return self.__speed
