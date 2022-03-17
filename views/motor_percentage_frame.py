from threading import Thread
from time import sleep
from tkinter import ttk

TIME_BETWEEN_UPDATE = 0.001

class MotorPercentageFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container, text='Ouverture Porte')
        self.stop_threads = False

        self.percentageBar = ttk.Progressbar(self, orient='vertical', length=100)
        self.percentageBar.grid(column=0, row=0)

    def update_open_percentage(self, new_open_percentage):
        self.stop_threads = True

        new_open_percentage = int(new_open_percentage)
        current_value = int(self.percentageBar['value'])

        open_direction = None

        if current_value == new_open_percentage: return
        if current_value < new_open_percentage: open_direction = True
        if current_value > new_open_percentage: open_direction = False

        open_value = abs(current_value - new_open_percentage)

        thread = Thread(target = self.update_progress_bar_thread, args = (open_direction, open_value, lambda : self.stop_threads, ))
        self.stop_threads = False
        thread.start()

    def update_progress_bar_thread(self, open_direction, open_value, stop):
        for _ in range(open_value):
            if stop(): break
            elif open_direction:
                self.percentageBar['value'] += 1
            elif not open_direction:
                self.percentageBar['value'] -= 1
            sleep(TIME_BETWEEN_UPDATE)
