from threading import Thread
import tkinter as tk
import logging
from models.control import Control

# Import models
from models.temperature import Temperature
from models.distance import Distance
from models.motor_status import MotorStatus

# Import views
from views.main_window import View

# Import controllers
from controllers.temperature_controller import TemperatureController
from controllers.distance_controller import DistanceController
from controllers.motor_controller import MotorController
from controllers.iot_hub_controller import IotHubController

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Controller')

        # Create the models
        self.__temperature = Temperature()
        self.__distance = Distance()
        self.__motor_status = MotorStatus()
        self.__control = Control()

        # Create the view
        self.__view = View(self)
        self.__view.grid(row=0, column=0, padx=15, pady=15)

        # Create and start the controllers threads
        self.__stop_threads = False

        self.__temperature_controller = TemperatureController(self.__temperature, self.__view)
        update_temperature_thread = Thread(target = self.__temperature_controller.update_temperature_thread, args = (lambda : self.__stop_threads, ))
        update_temperature_thread.start()
        
        self.__distance_controller = DistanceController(self.__distance, self.__view)
        update_distance_thread = Thread(target = self.__distance_controller.update_distance_thread, args = (lambda : self.__stop_threads, ))
        update_distance_thread.start()

        self.motor_controller = MotorController(self.__motor_status, self.__control, self.__temperature, self.__distance, self.__view)
        update_motor_status_thread = Thread(target = self.motor_controller.state_machine_thread, args = (lambda : self.__stop_threads, ))
        update_motor_status_thread.start()

        self.__iot_hub_controller = IotHubController(self.__temperature, self.__distance, self.__motor_status, self.__control)
        iot_hub_update_thread = Thread(target = self.__iot_hub_controller.iot_hub_update_thread, args = (lambda : self.__stop_threads, ))
        iot_hub_update_thread.start()
        iot_hub_control_thread = Thread(target = self.__iot_hub_controller.iot_hub_update_control_thread, args = (lambda : self.__stop_threads, ))
        iot_hub_control_thread.start()

def callback():
    app.__stop_threads = True
    app.destroy()

if __name__ == '__main__':
    logging.basicConfig(
        filename='logs.txt',
        filemode='w', 
        format='%(asctime)s %(levelname)s: %(message)s', 
        datefmt='%d/%m/%y %I:%M:%S %p', 
        level=logging.DEBUG)
    try:
        logging.info('Demarrage de l\'application')
        app = App()
        app.protocol("WM_DELETE_WINDOW", callback)
        app.mainloop()
    except KeyboardInterrupt:
        logging.warn('Interruption de l\'execution par l\'utilisateur')
