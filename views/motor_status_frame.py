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

    def update_rotation_speed(self, speed):
        self.speed_value_label['text'] = speed
    
    def update_rotation_direction(self, direction):
        self.direction_value_label['text'] = direction
