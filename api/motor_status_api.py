from datetime import datetime
import json
import uuid
from config import Constants
from controllers.internal_database import InternalDatabase
from models.dtos.motor_status_dto import MotorStatusDto
from models.motor_status import MotorStatus
from azure.iot.device import Message, IoTHubDeviceClient

class MotorStatusApi:
    def __init__(self, motor_status: MotorStatus, device_client: IoTHubDeviceClient, internal_database: InternalDatabase):
       self.__motor_status_model = motor_status
       self.__device_client = device_client
       self.__internal_database = internal_database

    def post_motor_status(self):
        current_motor_status = MotorStatusDto(self.__motor_status_model)

        self.__internal_database.insert_into_motor(Constants.DEVICE_ID, self.__motor_status_model.state.name, self.__motor_status_model.target, self.__motor_status_model.direction.name, self.__motor_status_model.speed, datetime.utcnow())

        message = Message(json.dumps(current_motor_status.__dict__))
        message.message_id = uuid.uuid4()
        message.content_encoding = Constants.IOT_HUB_MESSAGE_CONTENT_ENCODING
        message.content_type = Constants.IOT_HUB_MESSAGE_CONTENT_TYPE
        message.custom_properties["tornado-warning"] = "yes"

        self.__device_client.send_message(message)
