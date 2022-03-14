class Temperature:
    def __init__(self, value, unit):
        self._value = value
        self._unit = unit

    @property
    def unit(self):
        return self._unit

    @property
    def value(self):
        return self._value

    @unit.setter
    def unit(self, new_unit):
        self._unit = new_unit

    @value.setter
    def value(self, new_value):
        self._value = new_value
        