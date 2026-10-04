import math
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class class1(tk.Frame):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
        self.pack()
        self.fonk2()
        self.fonk3()
    def fonk2(self):
        self.b2 = tk.Button(self)
        self.b2["text"] = "\n Let's pick a color!\n"
        self.b2["command"] = self.say_hi
        self.b2.pack(b3 = "top")
        self.b4 = tk.Button(self, text="QUIT", fg="red", command=b7.destroy)
        self.b4.pack(b3 = "bottom")
    def fonk3(self):
        self.b5 = tk.Button(self)
        self.b5["text"] = "\n Let's seriously pick a color!\n"
        self.b5["command"] = self.say_hi
        self.b5.pack(b3 = "top")
    def fonk4(self):
        print(askcolor((255, 255, 0), b7))
        b8.destroy()
        self.fonk5()
    def fonk5(self):
        print("Bye Felicia.")
        exit()
def fonk6():
    b6 = input("Would you like to begin? (yes/no)\n").strip().lower()
    if b6 = = "yes":
        b7 = tk.Tk()
        b8 = class1(b1=b7)
        b9 = ttk.Style(b7)
        b9.theme_use('clam')
        b8.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    b10 = 24 * 60
    b11 = float(input("How many hours will you work today?\n")) * 60
    b12 = float(input("How many hours will you sleep today?\n")) * 60
    b13 = float(input("How many hours will you spend eating today?\n")) * 60
    b14 = float(input("How many hours will you spend driving today?\n")) * 60
    b15 = float(input("How many hours will you spend cleaning today?\n")) * 60
    b16 = b11 + b12 + b13 + b14 + b15
    b17 = b10 - b16
    a1 = 45
    a2 = 15
    a3 = 60
    b18 = b17
    b19 = b17 % a3
    print(f"{b19} minutes available today to do something thoughtful for someone.")
    print(f"{b18} b18 available today for creating something!")
if b20 = = "__main__":
    fonk6()