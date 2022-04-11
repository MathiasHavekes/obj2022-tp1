from models.distance import Distance

class DistanceDto:
    def __init__(self, distance: Distance):
        self.__value = str(distance.value)

    @property
    def value(self) -> str:
        return self.__value
