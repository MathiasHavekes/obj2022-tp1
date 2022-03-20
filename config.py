from models.enum_control_state import ControlState
from models.enum_temperature_unit import TemperatureUnit
from models.enum_distance_unit import DistanceUnit

class Constants:
    MIN_TEMPERATURE = 20        # En celsus
    MAX_TEMPERATURE = 35        # En celsus
    MIN_DISTANCE = 0            # En centimetre
    MAX_DISTANCE = 15           # En centimetre
    MAX_DISTANCE_MEASURING = 50 # En centimetre

    DEFAULT_TEMPERATURE_UNIT = TemperatureUnit.CELSIUS
    DEFAULT_DISTANCE_UNIT = DistanceUnit.CENTIMETRE
    DEFAULT_MOTOR_STATE = ControlState.AUTOMATIQUE
    DEFAULT_DOOR_OPEN_PERCENTAGE = 50

    TIME_BETWEEN_TEMPERATURE_UPDATE = 1        # En seconde
    TIME_BETWEEN_DISTANCE_UPDATE = 1           # En seconde
    TIME_BETWEEN_PERCENTAGE_BAR_UPDATE = 0.001 # En seconde

    SOUND_SPEED = 340 # En m/s

    # GPIO utilises
    TRIG_PIN = 16
    ECHO_PIN = 18

    MOTOR_PINS = (22, 32, 36, 38)    # Define pins connected to four phase ABCD of stepper motor
    
    CCW_STEP = (0x01,0x02,0x04,0x08) # Define power supply order for rotating anticlockwise 
    CW_STEP = (0x08,0x04,0x02,0x01)  # Define power supply order for rotating clockwise

    PID_SETUP = (100.0, 0.0, 0.0)
