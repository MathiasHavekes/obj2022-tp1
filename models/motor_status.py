class MotorStatus:
    def __init__(self, state, direction, speed):
        self._state = state 
        self._direction = direction
        self._speed = speed

    @property
    def state(self):
        return self._state

    @property
    def direction(self):
        return self._direction

    @property
    def speed(self):
        return self._speed

    @state.setter
    def state(self, new_state):
        self._state = new_state

    @direction.setter
    def temperature(self, new_direction):
        self._direction = new_direction

    @speed.setter
    def temperature(self, new_speed):
        self._speed = new_speed
        