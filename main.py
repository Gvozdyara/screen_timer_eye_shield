from tkinter import *
from tkinter import ttk
import winsound as ws
import threading
import datetime

class Timer(Tk):
    def __init__(self):
        super(Timer, self).__init__()
        self.title("Eye shield")
        self.Time = StringVar()
        self.stop_check = BooleanVar()
        self.label = ttk.Label(textvariable=self.Time)
        self.time_button_frame = ttk.Frame(self)
        self.time_button_1 = TimeSelector(self.time_button_frame, "15 мин", 15)
        self.time_button_2 = TimeSelector(self.time_button_frame, "25 мин", 25)
        self.time_button_3 = TimeSelector(self.time_button_frame, "40 мин", 40)
        self.stop_button = ttk.Button(self, text="СТОП")

        self.label.pack()
        self.time_button_frame.pack()
        self.time_button_1.pack()
        self.time_button_2.pack()
        self.time_button_3.pack()

    def stop_timer(self):
        self.stop_check.set(True)

class TimeSelector(ttk.Button):
    def __init__(self, parent, text, value):
        self.value = value
        super(TimeSelector, self).__init__(parent, text=text, command=self.set_timer)

    def set_timer(self):
        pass



if __name__ == '__main__':
    stop_check = False

    root = Root("Eye shield")
    root.mainloop()
