from tkinter import Toplevel, ttk
from models.enums.enum_motor_direction import MotorDirection
from models.enums.enum_control_state import ControlState
from models.motor_status import MotorStatus
from models.temperature import Temperature
from models.distance import Distance
from .information_frame import InformationFrame
from .motor_status_frame import MotorStatusFrame
from .control_frame import ControlFrame
from .motor_percentage_frame import MotorPercentageFrame
from .log_frame import LogFrame

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__parent = parent

        self.title = ttk.Label(self, text='Contrôle d\'une porte d\'aération de serre')
        self.title.grid(row=0, column=0, columnspan=3, padx=20, pady=20)

        self.information_view = InformationFrame(self)
        self.information_view.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        self.motor_status_view = MotorStatusFrame(self)
        self.motor_status_view.grid(row=1, column=2, padx=20, pady=20)

        self.control_view = ControlFrame(self)
        self.control_view.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        self.motor_percentage_view = MotorPercentageFrame(self)
        self.motor_percentage_view.grid(row=2, column=2, padx=20, pady=20)

        self.log_button = ttk.Button(self, text='Afficher les logs')
        self.log_button.grid(row=3, column=0, columnspan=3, padx=20, pady=20)
        self.log_button.bind('<Button>', self.log_button_pressed)
        
    def update_open_percentage(self, open_percentage: int):
        self.motor_percentage_view.update_open_percentage(open_percentage)
    
    def update_temperature(self, temperature: Temperature):
        self.information_view.update_temperature(temperature)

    def update_distance(self, distance: Distance):
        self.information_view.update_distance(distance)
        
    def update_rotation_speed(self, speed: int):
        self.motor_status_view.update_rotation_speed(speed)
    
    def update_rotation_direction(self, direction: MotorDirection):
        self.motor_status_view.update_rotation_direction(direction)

    def set_motor_state(self, motor_state: ControlState, opening_percentage: int):
        self.__parent.motor_controller.update_motor_state(motor_state, opening_percentage)

    def log_button_pressed(self, event):
        popup = Toplevel(self.__parent)
        popup.title('Logs')
        log_view = LogFrame(popup)
        log_view.grid(row=0, column=0)
