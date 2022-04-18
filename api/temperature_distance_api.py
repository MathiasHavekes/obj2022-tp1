import json
import uuid
from config import Constants
from models.distance import Distance
from models.dtos.temperature_distance_dto import TemperatureDistanceDto
from models.temperature import Temperature
from azure.iot.device import Message, IoTHubDeviceClient

class TemperatureDistanceApi:
    def __init__(self, temperature: Temperature, distance: Distance, device_client = IoTHubDeviceClient):
       self.__temperature_model = temperature
       self.__distance_model = distance
       self.__device_client = device_client

    def post_temperature_distance(self):
        current_temperature = TemperatureDistanceDto(self.__temperature_model, self.__distance_model)

        message = Message(json.dumps(current_temperature.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
