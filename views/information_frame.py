from models.temperature import Temperature
from models.distance import Distance
from models.enum_temperature_unit import TemperatureUnit
from models.enum_distance_unit import DistanceUnit
import tkinter as tk
from tkinter import ttk

class InformationFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container, text='Informations')
        
        self.temp_description_label = ttk.Label(self, text='Température ambiante:')
        self.temp_description_label.grid(column=0, row=0, sticky=tk.W)

        self.temp_value_label = ttk.Label(self, text=0)
        self.temp_value_label.grid(column=1, row=0, sticky=tk.E)

        self.dist_description_label = ttk.Label(self, text='Distance d\'ouverture:')
        self.dist_description_label.grid(column=0, row=1, sticky=tk.W)

        self.dist_value_label = ttk.Label(self, text=0)
        self.dist_value_label.grid(column=1, row=1, sticky=tk.E)

    def update_temperature(self, temperature: Temperature):
        unit = TemperatureUnit(temperature.unit).name.lower()
        self.temp_value_label['text'] = temperature.value, unit

    def update_distance(self, distance: Distance):
        unit = DistanceUnit(distance.unit).name.lower()
        self.dist_value_label['text'] = distance.value, unit
