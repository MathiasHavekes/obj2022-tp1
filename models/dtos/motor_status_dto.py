from models.enums.enum_control_state import ControlState
from models.enums.enum_motor_direction import MotorDirection
from models.motor_status import MotorStatus

class MotorStatusDto:
    def __init__(self, motor_status: MotorStatus):
        self.__state = ControlState(motor_status.state).name.lower()
        self.__target = str(motor_status.target)
        self.__direction = MotorDirection(motor_status.direction).name.lower()
        self.__speed = str(motor_status.speed)

    @property
    def state(self) -> str:
        return self.__state

    @property
    def target(self) -> str:
        return self.__target

    @property
    def direction(self) -> str:
        return self.__direction

    @property
    def speed(self) -> str:
        return self.__speed
