import time
from api.constants_api import ConstantsApi
from api.motor_status_api import MotorStatusApi
from api.temperature_distance_api import TemperatureDistanceApi
from config import Constants
from models.motor_status import MotorStatus
from models.temperature import Temperature
from models.distance import Distance
from azure.iot.device import IoTHubDeviceClient

class IotHubController:
    def __init__(self, temperature: Temperature, distance: Distance, motor_status: MotorStatus):
        self.__device_client = IoTHubDeviceClient.create_from_connection_string(Constants.IOT_HUB_URL)
        self.__device_client.connect()
        self.__temperature_distance_api = TemperatureDistanceApi(temperature, distance, self.__device_client)
        self.__motor_status_api = MotorStatusApi(motor_status, self.__device_client)
        self.__constants_api = ConstantsApi(self.__device_client)

    def iot_hub_update_thread(self, stop):
        self.__constants_api.post_constants_setup()

        while True:
            if stop(): break
            
            self.__temperature_distance_api.post_temperature_distance()
            self.__motor_status_api.post_motor_status()

            time.sleep(Constants.TIME_BETWEEN_API_POST)
