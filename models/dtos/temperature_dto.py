from models.temperature import Temperature

class TemperatureDto:
    def __init__(self, temperature: Temperature):
        self.__value = str(temperature.value)

    @property
    def value(self) -> str:
        return self.__value
