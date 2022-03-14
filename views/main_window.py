from tkinter import ttk
from .information_frame import InformationFrame
from .motor_status_frame import MotorStatusFrame
from .control_frame import ControlFrame
from .motor_percentage_frame import MotorPercentageFrame

class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.title = ttk.Label(self, text='Contrôle d\'une porte d\'aération d\'une serre')
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
        
    def update_open_percentage(self, open_percentage):
        self.motor_percentage_view.update_open_percentage(open_percentage)
    
    def update_temperature(self, temperature):
        self.information_view.update_temperature(temperature)

    def update_distance(self, distance):
        self.information_view.update_distance(distance)
        
    def update_rotation_speed(self, speed):
        self.motor_status_view = speed
    
    def update_rotation_direction(self, direction):
        self.motor_status_view = direction

    def set_automatic_mode(self, event):
        print('AUTO')

    def set_manuel_mode(self, event):
        print('MANUEL')

    def open_door_with_percentage(self, open_percentage):
        self.update_open_percentage(open_percentage)
        
    def open_door(self, event):
        print('OPEN')

    def close_door(self, event):
        print('CLOSE')

    def log_button_pressed(self, event):
        print('LOG')
