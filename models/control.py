import logging
from models.enums.enum_control_state import ControlState
from config import Constants

class Control:
  def __init__(self, state = Constants.DEFAULT_MOTOR_STATE, target = Constants.DEFAULT_DOOR_OPEN_PERCENTAGE):
    self.__state = state
    self.__target = target
    self.state_changed = False

  @property
  def state(self) -> ControlState:
    return self.__state

  @property
  def target(self) -> int:
    return self.__target

  @state.setter
  def state(self, new_state: ControlState):
    self.state_changed = True
    state = ControlState(new_state).name.lower()
    self.__state = new_state

  @target.setter
  def target(self, new_target: int):
    self.state_changed = True
    self.__target = new_target
  
  def update(self, state: ControlState, target: int):
    self.state_changed = True
    if target > 0:
      self.target = target
    self.state = state
        