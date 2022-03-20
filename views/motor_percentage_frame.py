from config import Constants
from threading import Thread
from time import sleep
import tkinter as tk
from tkinter import ttk

class MotorPercentageFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container, text='Ouverture de la porte')
        self.stop_threads = False

        self.percentage_bar = ttk.Progressbar(self, orient='vertical', length=100)
        self.percentage_bar.grid(column=0, row=0)

        self.dist_open_percentage = ttk.Label(self, text=0)
        self.dist_open_percentage.grid(column=1, row=0, sticky=tk.EW)

        self.percentage = ttk.Label(self, text='%')
        self.percentage.grid(column=3, row=0, sticky=tk.EW)

    def update_open_percentage(self, new_open_percentage: int):
        self.stop_threads = True

        new_open_percentage = int(new_open_percentage) 
        current_value = int(self.percentage_bar['value'])

        if new_open_percentage < 0: return
        if new_open_percentage > 100: return

        self.dist_open_percentage['text'] = new_open_percentage

        open_direction = None

        if current_value == new_open_percentage: return
        if current_value < new_open_percentage: open_direction = True
        if current_value > new_open_percentage: open_direction = False

        open_value = abs(current_value - new_open_percentage)

        thread = Thread(target = self.update_progress_bar_thread, args = (open_direction, open_value, lambda : self.stop_threads, ))
        self.stop_threads = False
        thread.start()

    def update_progress_bar_thread(self, open_direction: int, open_value: int, stop):
        for _ in range(open_value):
            if stop(): break
            elif open_direction:
                self.percentage_bar['value'] += 1
            elif not open_direction:
                self.percentage_bar['value'] -= 1
            sleep(Constants.TIME_BETWEEN_PERCENTAGE_BAR_UPDATE)
