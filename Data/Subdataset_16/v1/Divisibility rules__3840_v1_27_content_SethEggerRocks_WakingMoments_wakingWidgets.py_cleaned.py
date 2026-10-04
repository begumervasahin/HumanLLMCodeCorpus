import math
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class class1(tk.Frame):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
        self.b1 = b1
        self.pack()
        self.fonk2()
    def fonk2(self):
        self.b2 = tk.Button(self, text="\n Let's pick a color!\n", command=self.pick_color)
        self.b2.pack(b3 = "top")
        self.b4 = tk.Button(self, text="QUIT", fg="red", command=self.b1.destroy)
        self.b4.pack(b3 = "bottom")
    def fonk3(self):
        print(askcolor((255, 255, 0), b16))
        self.b1.destroy()
        self.fonk4()
    def fonk4(self):
        print("Bye Felicia.")
        exit()
def fonk5():
    b5 = 24 * 60
    b6 = float(input("How many hours will you work today?\n")) * 60
    b7 = float(input("How many hours will you sleep today?\n")) * 60
    b8 = float(input("How many hours will you spend eating today?\n")) * 60
    b9 = float(input("How many hours will you spend driving today?\n")) * 60
    b10 = float(input("How many hours will you spend cleaning today?\n")) * 60
    b11 = b6 + b7 + b8 + b9 + b10
    b12 = b5 - b11
    b13 = b12
    b14 = b12 % 60
    print(f"{b14} minutes available today to do something thoughtful for someone.")
    print(f"{b13} b13 available today for creating something!")
def fonk6():
    b15 = input("Would you like to begin?\n").lower()
    if b15 = = "yes":
        global b16
        b16 = tk.Tk()
        b17 = class1(b1=b16)
        b18 = ttk.Style(b16)
        b18.theme_use('clam')
        b17.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    fonk5()
if b19 = = "__main__":
    fonk6()