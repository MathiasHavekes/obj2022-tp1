from datetime import datetime
import time
from api.constants_api import ConstantsApi
from api.motor_status_api import MotorStatusApi
from api.temperature_distance_api import TemperatureDistanceApi
from config import Constants
from controllers.internal_database import InternalDatabase
from models.enums.enum_control_state import ControlState
from models.motor_status import MotorStatus
from models.temperature import Temperature
from models.distance import Distance
from azure.iot.device import IoTHubDeviceClient

class IotHubController:
    def __init__(self, temperature: Temperature, distance: Distance, motor_status: MotorStatus):
        self.__device_client = IoTHubDeviceClient.create_from_connection_string(Constants.IOT_HUB_URL)
        self.__device_client.connect()
        self.__internal_database = InternalDatabase()
        self.__device_client.on_message_received = self.message_handler
        self.__motor_status = motor_status
        self.__temperature_distance_api = TemperatureDistanceApi(temperature, distance, self.__device_client, self.__internal_database)
        self.__motor_status_api = MotorStatusApi(motor_status, self.__device_client, self.__internal_database)
        self.__constants_api = ConstantsApi(self.__device_client, self.__internal_database)

    def iot_hub_update_thread(self, stop):
        self.__constants_api.post_constants_setup()

        while True:
            if stop(): break
            
            self.__temperature_distance_api.post_temperature_distance()
            self.__motor_status_api.post_motor_status()

            time.sleep(Constants.TIME_BETWEEN_API_POST)
    
    def message_handler(self, message):
        try:
            messages = vars(message)
            if "state" and "target" not in messages.keys():
                print("Message doesn't contain opening information")
                return
            state = messages.get("state")
            self.__motor_status.state = ControlState[state]
            target = messages.get("target")
            self.__motor_status.target = target
            self.__internal_database.insert_into_control(Constants.DEVICE_ID, state, target, datetime.utcnow())
        except Exception as e:
            print("Exception catched in message handler: {0}", str(e))

    def close(self):
        self.__device_client.disconnect()
        self.__internal_database.close()
        
