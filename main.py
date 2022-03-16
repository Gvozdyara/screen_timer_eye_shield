from tkinter import *
import winsound as ws


def stop_timer():
    global stop_check
    stop_check = True
    ws.MessageBeep(-1)


class Root(Tk):
    def __init__(self, title):
        super().__init__()
        self.call('wm', 'attributes', '.', '-topmost', '1')
        # self.geometry("200x100")
        self.title(title)
        self.resizable(False, False)
        timer = Timer(self, "Выберете время")
        timer.pack()

        selector_frame = Frame(self)
        selector_frame.pack()

        for i in (15, 25, 40):
            Timer_selector(selector_frame, i, timer)

        stop = Button(self, text="СТОП", command=lambda: stop_timer(), width=32, font=200)
        stop.pack(side=BOTTOM)


class Timer_selector(Button):
    def __init__(self, frame, time_min, timer):
        super().__init__(frame, text=(str(time_min) + " мин"), command=self.set_timer, font=200, width=10)
        self.pack(side=RIGHT, pady=2)
        self.time = time_min
        self.timer = timer

    def set_timer(self, ):
        global stop_check
        time_sec = int(self.time) * 60
        time = int(time_sec)
        stop_check = False
        while time >= 0:
            if not stop_check:
                visible_time = f"{int(time / 60)} : {int(time - time // 60 * 60)}"
                self.timer.configure(text=visible_time)
                self.timer.update()
                time -= 1
                self.after(1000)
            else:
                break
        self.timer.configure(text="Выберете время")
        self.timer.update()
        if not stop_check:
            ws.Beep(1200, 1300)
        return


class Timer(Label):
    def __init__(self, frame, time):
        super().__init__(frame, text=time, font=400)


if __name__ == '__main__':
    root = Root("Eye shield")
    stop_check = False
    root.mainloop()
