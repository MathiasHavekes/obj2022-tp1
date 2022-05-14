from datetime import datetime
import json
import uuid
from config import Constants
from controllers.internal_database import InternalDatabase
from models.dtos.constants_dto import ConstantsDto
from azure.iot.device import Message, IoTHubDeviceClient

class ConstantsApi:
    def __init__(self, device_client: IoTHubDeviceClient, internal_database: InternalDatabase):
       self.__device_client = device_client
       self.__internal_database = internal_database

    def post_constants_setup(self):
        constants_setup = ConstantsDto()

        self.__internal_database.insert_into_constants(Constants.DEVICE_ID, Constants.MIN_TEMPERATURE, Constants.MAX_TEMPERATURE, Constants.MIN_DISTANCE, Constants.MAX_DISTANCE, datetime.utcnow())

        message = Message(json.dumps(constants_setup.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
