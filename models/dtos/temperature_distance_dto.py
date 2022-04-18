from models.distance import Distance
from models.temperature import Temperature

class TemperatureDistanceDto:
    def __init__(self, temperature: Temperature, distance: Distance):
        self.__type = 'distance_temperature'
        self.__temperature = temperature.value
        self.__distance = distance.value

    @property
    def type(self) -> str:
        return self.__type

    @property
    def temperature(self) -> int:
        return self.__temperature
    
    @property
    def distance(self) -> int:
        return self.__distance
