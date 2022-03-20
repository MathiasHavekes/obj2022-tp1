from models.enum_distance_unit import DistanceUnit

class Distance:
    def __init__(self, value: int, unit: DistanceUnit):
        self._value = value
        self._unit = unit

    @property
    def value(self) -> int:
        return self._value

    @property
    def unit(self) -> DistanceUnit:
        return self._unit

    @value.setter
    def value(self, new_value: int):
        self._value = new_value

    @unit.setter
    def unit(self, new_unit: DistanceUnit):
        self._unit = new_unit
