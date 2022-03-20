import logging
from models.enum_temperature_unit import TemperatureUnit

class Temperature:
    def __init__(self, value: int, unit: TemperatureUnit):
        self.__value = value
        self.__unit = unit

    @property
    def value(self) -> int:
        return self.__value

    @property
    def unit(self) -> TemperatureUnit:
        return self.__unit

    @value.setter
    def value(self, new_value: int):
        unit = TemperatureUnit(self.__unit).name.lower()
        logging.info('Temperature : %s %s', new_value, unit)
        self.__value = new_value

    @unit.setter
    def unit(self, new_unit: TemperatureUnit):
        self.__unit = new_unit
        