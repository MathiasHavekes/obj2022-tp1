from datetime import datetime
import sqlite3
from threading import Lock

from config import Constants


class InternalDatabase:
  def __init__(self):
    self.__internal_database = sqlite3.connect(Constants.SQLITE_DATABASE_FILE, check_same_thread=False)
    self.__lock = Lock()
  
  def insert_into_distance_temperature(self, device_id: str, temperature: int, distance: int, utc_now: datetime):
    query = "INSERT INTO distance_temperature (ConnectionDeviceId, temperature, distance, EventProcessedUtcTime) VALUES(?, ?, ?, ?)"
    data_tuple = (device_id, temperature, distance, utc_now)
    self.__insert(query, data_tuple)

  def insert_into_motor(self, device_id: str, state: str, target: int, direction: str, speed: int, utc_now: datetime):
    query = "INSERT INTO motor (ConnectionDeviceId, motor_state, motor_target, direction, speed, EventProcessedUtcTime) VALUES(?, ?, ?, ?, ?, ?)"
    data_tuple = (device_id, state, target, direction, speed, utc_now)
    self.__insert(query, data_tuple)

  def insert_into_constants(self, device_id: str, min_temperature: int, max_temperature: int, min_distance: int, max_distance: int, utc_now: datetime):
    query = "INSERT INTO constants (ConnectionDeviceId, min_temperature, max_temperature, min_distance, max_distance, EventProcessedUtcTime) VALUES(?, ?, ?, ?, ?, ?)"
    data_tuple = (device_id, min_temperature, max_temperature, min_distance, max_distance, utc_now)
    self.__insert(query, data_tuple)

  def insert_into_control(self, device_id: str, state: str, target: int, utc_now: datetime):
    query = "INSERT INTO control (ConnectionDeviceId, mode, distance, EventProcessedUtcTime) VALUES(?, ?, ?, ?)"
    data_tuple = (device_id, state, target, utc_now)
    self.__insert(query, data_tuple)

  def __insert(self, query: str, data_tuple: tuple):
    self.__lock.acquire()
    cursor = self.__internal_database.cursor()
    cursor.execute(query, data_tuple)
    self.__internal_database.commit()
    self.__lock.release()

  def close(self):
    self.__internal_database.close()