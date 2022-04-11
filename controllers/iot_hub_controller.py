import time
from api.constants_api import ConstantsApi
from api.distance_api import DistanceApi
from api.motor_status_api import MotorStatusApi
from config import Constants
from models.motor_status import MotorStatus
from models.temperature import Temperature
from models.distance import Distance
from api.temperature_api import TemperatureApi
from azure.iot.device import IoTHubDeviceClient

class IotHubController:
    def __init__(self, temperature: Temperature, distance: Distance, motor_status: MotorStatus):
        self.__device_client = IoTHubDeviceClient.create_from_connection_string(Constants.IOT_HUB_URL)
        self.__device_client.connect()
        self.__temperature_api = TemperatureApi(temperature, self.__device_client)
        self.__distance_api = DistanceApi(distance, self.__device_client)
        self.__motor_status_api = MotorStatusApi(motor_status, self.__device_client)
        self.__constants_api = ConstantsApi(self.__device_client)

    def iot_hub_update_thread(self, stop):
        self.__constants_api.post_constants_setup()

        while True:
            if stop(): break
            
            self.__temperature_api.post_temperature()
            self.__distance_api.post_distance()
            self.__motor_status_api.post_motor_status()

            time.sleep(Constants.TIME_BETWEEN_API_POST)
