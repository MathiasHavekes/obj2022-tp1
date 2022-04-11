import json
import uuid
from config import Constants
from models.distance import Distance
from azure.iot.device import Message, IoTHubDeviceClient

from models.dtos.distance_dto import DistanceDto

class DistanceApi:
    def __init__(self, distance: Distance, device_client = IoTHubDeviceClient):
       self.__distance_model = distance
       self.__device_client = device_client

    def post_distance(self):
        current_distance = DistanceDto(self.__distance_model)

        message = Message(json.dumps(current_distance.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
