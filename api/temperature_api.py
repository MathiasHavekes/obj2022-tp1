import json
import uuid
from config import Constants
from models.dtos.temperature_dto import TemperatureDto
from models.temperature import Temperature
from azure.iot.device import Message, IoTHubDeviceClient

class TemperatureApi:
    def __init__(self, temperature: Temperature, device_client = IoTHubDeviceClient):
       self.__temperature_model = temperature
       self.__device_client = device_client

    def post_temperature(self):
        current_temperature = TemperatureDto(self.__temperature_model)

        message = Message(json.dumps(current_temperature.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
