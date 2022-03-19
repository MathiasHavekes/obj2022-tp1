from threading import Thread
import tkinter as tk
import logging

# Import enums
from models.enum_control_state import ControlState
from models.enum_temperature_units import TemperatureUnits
from models.enum_distance_units import DistanceUnits

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

DEFAULT_TEMPERATURE_UNIT = TemperatureUnits.CELSUS
DEFAULT_DISTANCE_UNIT = DistanceUnits.CENTIMETER
DEFAULT_MOTOR_STATE = ControlState.AUTOMATIC

DEFAULT_MIN_VALUE = 0
DEFAULT_MAX_VALUE = 15

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Controller')

        # Create the model
        self.temperature = Temperature(0, DEFAULT_TEMPERATURE_UNIT)
        self.distance = Distance(0, DEFAULT_DISTANCE_UNIT, DEFAULT_MIN_VALUE, DEFAULT_MAX_VALUE)
        self.motor_status = MotorStatus(DEFAULT_MOTOR_STATE, 0, 0)

        # Create the views
        self.view = View(self)
        self.view.grid(row=0, column=0, padx=15, pady=15)

        # Create and start the controllers threads
        self.stop_threads = False

        self.temperature_controller = TemperatureController(self.temperature, self.view)
        update_temperature_thread = Thread(target = self.temperature_controller.update_temperature_thread, args = (lambda : self.stop_threads, ))
        update_temperature_thread.start()
        
        self.distance_controller = DistanceController(self.distance, self.view)
        update_distance_thread = Thread(target = self.distance_controller.update_distance_thread, args = (lambda : self.stop_threads, ))
        update_distance_thread.start()

        self.motor_controller = MotorController(self.motor_status, self.temperature, self.view)
        update_motor_status_thread = Thread(target = self.motor_controller.state_machine_thread, args = (lambda : self.stop_threads, ))
        update_motor_status_thread.start()

def callback():
    app.stop_threads = True
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
