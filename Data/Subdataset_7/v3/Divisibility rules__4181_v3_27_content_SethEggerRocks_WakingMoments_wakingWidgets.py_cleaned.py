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
        b4 = tk.Button(self, text="QUIT", fg="red", command=b5.destroy)
        b4.pack(b3 = "bottom")
    def fonk5(self):
        print(askcolor((255, 255, 0), b5))
        b6.destroy()
        self.fonk6()
    def fonk6(self):
        print("Bye Felicia.")
        exit()
def fonk7():
    if input("Would you like to begin?\n").lower() == "yes":
        b5 = tk.Tk()
        b6 = class1(b1=b5)
        fonk8(b5)
        b6.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    b7 = 24 * 60
    b8 = fonk9("work")
    b9 = fonk9("sleep")
    b10 = fonk9("eat")
    b11 = fonk9("drive")
    b12 = fonk9("clean")
    b13 = b7 - (b8 + b9 + b10 +
                                    b11 + b12)
    b16, b14 = fonk10(b13)
    print(f"{b14} Minutes available today to do something b14 for someone.")
    print(f"{b16} Sessions available today for creating something!")
def fonk8(b5):
    b15 = ttk.Style(b5)
    b15.theme_use('clam')
def fonk9(activity):
    return float(input(f"How many hours will you {activity} today?\n")) * 60
def fonk10(remaining_minutes):
    b16 = remaining_minutes
    b14 = remaining_minutes % 60
    return b16, b14
if b17 = = "__main__":
    fonk7()