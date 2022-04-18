import json
import uuid
from config import Constants
from models.dtos.constants_dto import ConstantsDto
from azure.iot.device import Message, IoTHubDeviceClient

class ConstantsApi:
    def __init__(self, device_client: IoTHubDeviceClient):
       self.__device_client = device_client

    def post_constants_setup(self):
        constants_setup = ConstantsDto()

        message = Message(json.dumps(constants_setup.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
