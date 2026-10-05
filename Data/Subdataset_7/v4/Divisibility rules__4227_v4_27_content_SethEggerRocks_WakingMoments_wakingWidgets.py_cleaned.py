import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class class1(tk.Frame):
    def fonk1(self, b1 = None):
        super().fonk1(b1)
        self.pack()
        self.fonk2()
    def fonk2(self):
        self.fonk3("Let's pick a color!", self.pick_color)
        self.fonk3("Let's seriously pick a color!", self.pick_color)
        self.fonk4()
    def fonk3(self, text, command):
        b2 = tk.Button(self, text=f"\n{text}\n", command=command)
        b2.pack(b3 = "top")
    def fonk4(self):
        b4 = tk.Button(self, text="QUIT", fg="red", command=b6.destroy)
        b4.pack(b3 = "bottom")
    def fonk5(self):
        print(askcolor((255, 255, 0), b6))
        b7.destroy()
        self.fonk6()
    def fonk6(self):
        print("Bye Felicia.")
        exit()
def fonk7():
    b5 = input("Would you like to begin?\n").lower()
    if b5 = = "yes":
        b6 = tk.Tk()
        b7 = class1(b1=b6)
        fonk8(b6)
        b7.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    b8 = 24 * 60
    b9 = fonk9("work")
    b10 = fonk9("sleep")
    b11 = fonk9("eat")
    b12 = fonk9("drive")
    b13 = fonk9("clean")
    b14 = b8 - (b9 + b10 + b11 +
                                          b12 + b13)
    b17, b15 = fonk10(b14)
    print(f"{b15} Minutes available today to do something b15 for someone.")
    print(f"{b17} Sessions available today for creating something!")
def fonk8(b6):
    b16 = ttk.Style(b6)
    b16.theme_use('clam')
def fonk9(activity):
    return float(input(f"How many hours will you {activity} today?\n")) * 60
def fonk10(b14):
    b17 = b14
    b15 = b14 % 60
    return b17, b15
if b18 = = "__main__":
    fonk7()