from dataclasses import dataclass
from datetime import datetime
import json
import time
from api.constants_api import ConstantsApi
from api.control_api import ControlApi
from api.motor_status_api import MotorStatusApi
from api.temperature_distance_api import TemperatureDistanceApi
from config import Constants
from controllers.internal_database import InternalDatabase
from models.control import Control
from models.enums.enum_control_state import ControlState
from models.motor_status import MotorStatus
from models.temperature import Temperature
from models.distance import Distance
from azure.iot.device import IoTHubDeviceClient

class IotHubController:
    def __init__(self, temperature: Temperature, distance: Distance, motor_status: MotorStatus, control: Control):
        self.__device_client = IoTHubDeviceClient.create_from_connection_string(Constants.IOT_HUB_URL)
        self.__device_client.connect()
        self.__internal_database = InternalDatabase()
        self.__device_client.on_message_received = self.message_handler
        self.__motor_status = motor_status
        self.__control = control
        self.__temperature_distance_api = TemperatureDistanceApi(temperature, distance, self.__device_client, self.__internal_database)
        self.__motor_status_api = MotorStatusApi(motor_status, self.__device_client, self.__internal_database)
        self.__constants_api = ConstantsApi(self.__device_client, self.__internal_database)
        self.__control_api = ControlApi(self.__control, self.__device_client, self.__internal_database)

    def iot_hub_update_thread(self, stop):
        self.__constants_api.post_constants_setup()

        while True:
            if stop(): break
            
            self.__temperature_distance_api.post_temperature_distance()
            self.__motor_status_api.post_motor_status()

            time.sleep(Constants.TIME_BETWEEN_API_POST)
    
    def iot_hub_update_control_thread(self, stop):
        while True:
            if stop(): break
            if(self.__control.state_changed):
                self.__control_api.post_control_status()
                self.__control.state_changed = False
            time.sleep(Constants.TIME_BETWEEN_CONTROL_CHECK)
    
    def message_handler(self, message):
        try:
            data = vars(message).get('data')
            data_dict = json.loads(data)
            if "state" and "target" not in data_dict.keys():
                return
            state = data_dict.get("state")
            if state == 'FermerPorte':
                update_state = ControlState["FERMER_PORTE"]
                self.__control.update(update_state, -1)
            elif state == 'OuvrirPorte':
                update_state = ControlState["OUVRIR_PORTE"]
                self.__control.update(update_state, -1)
            elif state == 'Automatique':
                update_state = ControlState["AUTOMATIQUE"]
                self.__control.update(update_state, -1)
            elif state == 'Manuel':
                update_state = ControlState["MANUEL"]
                target = data_dict.get("target")
                if target:
                    self.__control.update(update_state, target)
                
        except Exception as e:
            print("Exception catched in message handler: {0}", str(e))

    def close(self):
        self.__device_client.disconnect()
        self.__internal_database.close()
        
