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

    def update_temperature(self, temperature):
        self.temp_value_label['text'] = temperature

    def update_distance(self, distance):
        self.dist_value_label['text'] = distance
