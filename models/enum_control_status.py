from enum import Enum, auto

class ControlStatus(Enum):
    AUTOMATIC = auto()
    MANUAL = auto()
    OPEN_DOOR = auto()
    CLOSE_DOOR = auto()