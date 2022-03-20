from models.enum_temperature_unit import TemperatureUnit

class Temperature:
    def __init__(self, value: int, unit: TemperatureUnit):
        self._value = value
        self._unit = unit

    @property
    def value(self) -> int:
        return self._value

    @property
    def unit(self) -> TemperatureUnit:
        return self._unit

    @value.setter
    def value(self, new_value: int):
        self._value = new_value

    @unit.setter
    def unit(self, new_unit: TemperatureUnit):
        self._unit = new_unit
        