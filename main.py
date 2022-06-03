import winsound
from tkinter import *
from tkinter import ttk
import threading
import datetime
import time
import os

class Timer(Tk):
    def __init__(self):
        super(Timer, self).__init__()
        self.configure(bg="White")
        s = ttk.Style()
        s.configure("TButton", font=("Tahoma", 8))
        s.configure("TLabel", font=("Monospace", 16), background="White")
        self.call('wm', 'attributes', '.', '-topmost', '1')
        self.title("Eye shield")
        self.Time = StringVar()
        self.Time.set("Выберете врямя")
        self.stop_check = BooleanVar()
        self.label = ttk.Label(textvariable=self.Time, font=("Monospace", 12))
        self.time_button_frame = ttk.Frame(self)
        self.time_button_1 = TimeSelector(self.time_button_frame, "15 мин", str(15))
        self.time_button_2 = TimeSelector(self.time_button_frame, "25 мин", str(25))
        self.time_button_3 = TimeSelector(self.time_button_frame, "40 мин", str(40))
        self.stop_button = ttk.Button(self, text="СТОП", command=self.stop_timer)

        self.label.pack(pady=(10, 5))
        self.time_button_frame.pack(padx=8)
        self.time_button_1.pack(side=LEFT)
        self.time_button_2.pack(side=LEFT)
        self.time_button_3.pack(side=LEFT)
        self.stop_button.pack(fill=BOTH, padx=8, pady=(1, 10))

    def stop_timer(self):
        self.stop_check.set(False)
        self.time_button_1["state"] = NORMAL
        self.time_button_2["state"] = NORMAL
        self.time_button_3["state"] = NORMAL


class TimeSelector(ttk.Button):
    def __init__(self, parent, text, value):
        self.value = value
        super(TimeSelector, self).__init__(parent, text=text, command=self.set_timer)

    def set_timer(self):
        def main():
            time_left = datetime.datetime.strptime(self.value, "%M")
            app.stop_check.set(True)
            while app.stop_check.get():
                if time_left > datetime.datetime.strptime("0", "%M"):
                    time_left -= datetime.timedelta(seconds=1)
                    app.Time.set(datetime.datetime.strftime(time_left, "%M:%S"))
                    app.label.update()
                    time.sleep(1)
                else:
                    app.stop_check.set(False)
                    winsound.Beep(470,700)
            app.Time.set("Выберете время")

        app.stop_timer()
        app.time_button_1["state"] = DISABLED
        app.time_button_2["state"] = DISABLED
        app.time_button_3["state"] = DISABLED

        try:
            threads[0].join()
            threads.pop()
        except IndexError:
            pass

        t = threading.Thread(target=main)
        t.start()
        threads.append(t)


if __name__ == '__main__':


    threads = []
    stop_check = False
    app = Timer()
    app.mainloop()
    try:
        threads[0].join()
        threads.pop()
    except IndexError:
        pass