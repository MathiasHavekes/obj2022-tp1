from config import Constants

class ConstantsDto:
    def __init__(self):
        self.__type = 'constant' 
        self.__min_temperature = int(Constants.MIN_TEMPERATURE)
        self.__max_temperature = int(Constants.MAX_TEMPERATURE)
        self.__min_distance = int(Constants.MIN_DISTANCE)
        self.__max_distance = int(Constants.MAX_DISTANCE)

    @property
    def type(self) -> str:
        return self.__type

    @property
    def min_temperature(self) -> int:
        return self.__min_temperature
    
    @property
    def max_temperature(self) -> int:
        return self.__max_temperature
    
    @property
    def min_distance(self) -> int:
        return self.__min_distance

    @property
    def min_distance(self) -> int:
        return self.__max_distance
