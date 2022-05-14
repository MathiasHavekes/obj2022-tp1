from datetime import datetime
import json
import uuid
from config import Constants
from controllers.internal_database import InternalDatabase
from models.control import Control
from azure.iot.device import Message, IoTHubDeviceClient

from models.dtos.control_dto import ControlDto

class ControlApi:
    def __init__(self, control: Control, device_client: IoTHubDeviceClient, internal_database: InternalDatabase):
       self.__control_model = control
       self.__device_client = device_client
       self.__internal_database = internal_database

    def post_control_status(self):
        control_status = ControlDto(self.__control_model)

        self.__internal_database.insert_into_control(Constants.DEVICE_ID, control_status.state, control_status.target, datetime.utcnow())

        message = Message(json.dumps(control_status.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
