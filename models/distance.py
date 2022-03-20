import logging
from config import Constants
from models.enum_distance_unit import DistanceUnit

class Distance:
    def __init__(self, value: int, unit: DistanceUnit):
        self.__value = value
        self.__unit = unit

    @property
    def value(self) -> int:
        return self.__value

    @property
    def unit(self) -> DistanceUnit:
        return self.__unit

    @value.setter
    def value(self, new_value: int):
        if new_value < Constants.MAX_DISTANCE or new_value > Constants.MIN_DISTANCE: return
        unit = DistanceUnit(self.__unit).name.lower()
        logging.info('Distance d\'ouverture : %s %s', new_value, unit, )
        self.__value = new_value

    @unit.setter
    def unit(self, new_unit: DistanceUnit):
        self.__unit = new_unit
