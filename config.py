from models.enums.enum_control_state import ControlState
from models.enums.enum_temperature_unit import TemperatureUnit
from models.enums.enum_distance_unit import DistanceUnit

class Constants:
    MIN_TEMPERATURE = 20        # En celsius
    MAX_TEMPERATURE = 35        # En celsius
    MIN_DISTANCE = 0            # En centimetre
    MAX_DISTANCE = 14           # En centimetre
    MAX_DISTANCE_MEASURING = 50 # En centimetre

    DEFAULT_TEMPERATURE_UNIT = TemperatureUnit.CELSIUS
    DEFAULT_DISTANCE_UNIT = DistanceUnit.CENTIMETRE
    DEFAULT_MOTOR_STATE = ControlState.AUTOMATIQUE
    DEFAULT_DOOR_OPEN_PERCENTAGE = 50

    TIME_BETWEEN_TEMPERATURE_UPDATE = 1        # En seconde
    TIME_BETWEEN_DISTANCE_UPDATE = 1           # En seconde
    TIME_BETWEEN_PERCENTAGE_BAR_UPDATE = 0.001 # En seconde
    TIME_BETWEEN_API_POST = 60                 # En seconde
    TIME_BETWEEN_CONTROL_CHECK = 1             # En seconde

    SOUND_SPEED = 340 # En m/s

    # GPIO utilises
    TRIG_PIN = 16
    ECHO_PIN = 18

    MOTOR_PINS = (31, 33, 35, 37)   # Define pins connected to four phase ABCD of stepper motor
    
    CCW_STEP = (0x01,0x02,0x04,0x08) # Define power supply order for rotating anticlockwise 
    CW_STEP = (0x08,0x04,0x02,0x01)  # Define power supply order for rotating clockwise

    PID_SETUP = (20.0, 0.0, 0.0)

    IOT_HUB_URL = 'HostName=iotObjectHub.azure-devices.net;DeviceId=tempsensor;SharedAccessKey=kudN1EiFDqPDpy98iYN4ZC8mTiLFGCMMcqA840r29r0='
    IOT_HUB_MESSAGE_CONTENT_ENCODING = 'utf-8'
    IOT_HUB_MESSAGE_CONTENT_TYPE = 'application/json'

    SQLITE_DATABASE_FILE = './database/sqlDatabase.db'
    DEVICE_ID = "tempsensor"
