import math
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.create_widgets2()
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "\n Let's pick a color!\n"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")
    def create_widgets2(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "\n Let's seriously pick a color!\n"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")
    def say_hi(self):
        print(askcolor((255, 255, 0), root))
        app.destroy()
        self.pick_day()
    def pick_day(self):
        print("Bye Felicia.")
        exit()
colorOrNot = input("Would you like to begin?\n")
if colorOrNot == "yes":
    root = tk.Tk()
    app = Application(master=root)
    style = ttk.Style(root)
    style.theme_use('clam')
    app.mainloop()
else:
    print("Okay, goodbye.")
    exit()
todayMinutes = 24 * 60
workingMinutes = float(input("How many hours will you work today?\n")) * 60
sleepingMinutes = float(input("How many hours will you sleep of today?\n")) * 60
eatingMinutes = float(input("How many hours will you spend eating today?\n")) * 60
drivingMinutes = float(input("How many hours will you spend driving today?\n")) * 60
cleaningMinutes = float(input("How many hours will you spend cleaning today?\n")) * 60
whatIsLeft = todayMinutes - (workingMinutes + sleepingMinutes + eatingMinutes +
                            drivingMinutes + cleaningMinutes)
artisticWindows = 45
articisticBreaks = 15
aWaB = 60
sessions = whatIsLeft
thoughtFul = whatIsLeft % 60
print(str(thoughtFul) + " Minutes available today to do something thoughtful for someone.")
print(str(sessions) + " Sessions available today for creating something!")