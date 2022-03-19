from tkinter import ttk

class LogFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.logs = ttk.Label(self, text=self.open_logs())
        self.logs.grid(column=0, row=0)

    def open_logs(self) -> str:
        logs = ''
        
        for line in reversed(open('logs.txt').readlines()):
            logs += line

        return logs
