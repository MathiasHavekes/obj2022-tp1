class MotorStatus:
    def __init__(self, status, direction, speed):
        self._status = status 
        self._direction = direction
        self._speed = speed

    @property
    def status(self):
        return self._status

    @property
    def direction(self):
        return self._direction

    @property
    def speed(self):
        return self._speed

    @status.setter
    def status(self, new_status):
        self._status = new_status

    @direction.setter
    def temperature(self, new_direction):
        self._direction = new_direction

    @speed.setter
    def temperature(self, new_speed):
        self._speed = new_speed
        