class Distance:
    def __init__(self, value, unit, min_value, max_value):
        self._value = value
        self._unit = unit
        self._min_value = min_value
        self._max_value = max_value

    @property
    def value(self):
        return self._value

    @property
    def unit(self):
        return self._unit

    @property
    def min_value(self):
        return self._min_value

    @property
    def max_value(self):
        return self._max_value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @unit.setter
    def unit(self, new_unit):
        self._unit = new_unit

    @min_value.setter
    def min_value(self, new_min_value):
        self._min_value = new_min_value

    @max_value.setter
    def max_value(self, new_max_value):
        self._max_value = new_max_value
