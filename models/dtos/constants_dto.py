from config import Constants

class ConstantsDto:
    def __init__(self):
        self.__min_temperature = str(Constants.MIN_TEMPERATURE)
        self.__max_temperature = str(Constants.MAX_TEMPERATURE)
        self.__min_distance = str(Constants.MIN_DISTANCE)
        self.__max_distance = str(Constants.MAX_DISTANCE)

    @property
    def min_temperature(self) -> str:
        return self.__min_temperature
    
    @property
    def max_temperature(self) -> str:
        return self.__max_temperature
    
    @property
    def min_distance(self) -> str:
        return self.__min_distance

    @property
    def min_distance(self) -> str:
        return self.__max_distance
