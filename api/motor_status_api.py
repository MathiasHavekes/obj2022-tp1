import json
import uuid
from config import Constants
from models.dtos.motor_status_dto import MotorStatusDto
from models.motor_status import MotorStatus
from azure.iot.device import Message, IoTHubDeviceClient

class MotorStatusApi:
    def __init__(self, motor_status: MotorStatus, device_client: IoTHubDeviceClient):
       self.__motor_status_model = motor_status
       self.__device_client = device_client

    def post_motor_status(self):
        current_motor_status = MotorStatusDto(self.__motor_status_model)

        message = Message(json.dumps(current_motor_status.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
