from models.enum_motor_direction import MotorDirection
import tkinter as tk
from tkinter import ttk

class MotorStatusFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container, text='Status du moteur')
        
        self.speed_description_label = ttk.Label(self, text='Vitesse :')
        self.speed_description_label.grid(column=0, row=0, sticky=tk.W)

        self.speed_value_label = ttk.Label(self, text=0)
        self.speed_value_label.grid(column=1, row=0, sticky=tk.E)

        self.direction_description_label = ttk.Label(self, text='Direction :')
        self.direction_description_label.grid(column=0, row=1, sticky=tk.W)

        self.direction_value_label = ttk.Label(self, text='Aucun')
        self.direction_value_label.grid(column=1, row=1, sticky=tk.E)

    def update_rotation_speed(self, speed: int):
        self.speed_value_label['text'] = round(speed / 100, 1), 'tour/min'
    
    def update_rotation_direction(self, direction: MotorDirection):
        direction_name = MotorDirection(direction).name.lower()
        self.direction_value_label['text'] = direction_name
