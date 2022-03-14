import tkinter as tk

# Import enums
from models.enum_control_status import ControlStatus
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
DEFAULT_MOTOR_STATUS = ControlStatus.AUTOMATIC

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Controller')

        # Create the model
        self.temperature = Temperature(0, DEFAULT_TEMPERATURE_UNIT)
        self.distance = Distance(0, DEFAULT_DISTANCE_UNIT)
        self.motor_status = MotorStatus(DEFAULT_MOTOR_STATUS, 0, 0)

        # Create the views
        self.view = View(self)
        self.view.grid(row=0, column=0, padx=15, pady=15)

        # Create and start the controllers
        temperature_controller_thread = TemperatureController(self.temperature, self.view)
        temperature_controller_thread.start()

        distance_controller_thread = DistanceController(self.distance, self.view)
        distance_controller_thread.start()

if __name__ == '__main__':
    try:
        app = App()
        app.mainloop()
    except KeyboardInterrupt:
        print("User interrupted the execution")
    except:
        print("Fatal: unexpected exception")
