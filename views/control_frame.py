from models.enum_control_state import ControlState
from config import Constants
import tkinter as tk
from tkinter import ttk

class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container, text='Controles')
        self.container = container

        self.automatic_button = ttk.Button(self, text='Automatique', width=20)
        self.automatic_button.grid(column=0, row=0, sticky=tk.W)
        self.automatic_button.bind('<Button>', self.automatic_button_pressed)

        self.manual_button = ttk.Button(self, text='Manuel', width=20)
        self.manual_button.grid(column=0, row=1, sticky=tk.W)
        self.manual_button.bind('<Button>', self.manuel_button_pressed)

        self.percentage_entry = ttk.Entry(self, text='Pourcentage d\'ouverture', width=3)
        self.percentage_entry.grid(column=1, row=1, sticky=tk.E)
        self.percentage_entry.insert(0, Constants.DEFAULT_DOOR_OPEN_PERCENTAGE)
        self.percentage_entry.bind('<KeyRelease>', self.entry_key_released)

        self.label = ttk.Label(self, text='%')
        self.label.grid(column=2, row=1, sticky=tk.E)

        self.open_door_button = ttk.Button(self, text='Ouvrir la porte', width=20)
        self.open_door_button.grid(column=0, row=2, sticky=tk.W)
        self.open_door_button.bind('<Button>', self.open_button_pressed)

        self.close_door_button = ttk.Button(self, text='Fermer la porte', width=20)
        self.close_door_button.grid(column=0, row=3,  sticky=tk.W)
        self.close_door_button.bind('<Button>', self.close_button_pressed)

    def automatic_button_pressed(self, event):
        new_motor_state = ControlState.AUTOMATIQUE
        self.container.set_motor_state(new_motor_state)

    def manuel_button_pressed(self, event):
        new_motor_state = ControlState.MANUEL
        self.container.set_motor_state(new_motor_state)

    def entry_key_released(self, event):
        user_entry = self.percentage_entry.get()

        if not user_entry.isnumeric(): return

        user_entry = int(user_entry)

        if user_entry > 100 or user_entry < 0: return

        self.container.open_door_with_percentage(user_entry)

    def open_button_pressed(self, event):
        new_motor_state = ControlState.OUVRIR_PORTE
        self.container.set_motor_state(new_motor_state)

    def close_button_pressed(self, event):
        new_motor_state = ControlState.FERMER_PORTE
        self.container.set_motor_state(new_motor_state)
