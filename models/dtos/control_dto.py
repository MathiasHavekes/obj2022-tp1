from models.enums.enum_control_state import ControlState
from models.control import Control

class ControlDto:
  def __init__(self, control: Control):
    self.__type = 'control'
    self.__state = ControlState(control.state).name.lower()
    self.__target = control.target

  @property
  def type(self) -> str:
    return self.__type

  @property
  def state(self) -> str:
    return self.__state

  @property
  def target(self) -> int:
    return self.__target
