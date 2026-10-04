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
        self.b4 = tk.Button(self, text="QUIT", fg="red", command=self.quit_app)
        self.b4.pack(b3 = "bottom")
    def fonk3(self):
        self.b5 = tk.Button(self)
        self.b5["text"] = "\n Let's seriously pick a color!\n"
        self.b5["command"] = self.say_hi
        self.b5.pack(b3 = "top")
    def fonk4(self):
        print(askcolor((255, 255, 0), b10))
        self.fonk5()
    def fonk5(self):
        b10.destroy()
        self.fonk6()
    @staticmethod
    def fonk6():
        print("Bye Felicia.")
        exit()
def fonk7():
    fonk8()
    b6 = 24 * 60
    b7 = fonk9()
    b8 = b6 - sum(b7.values())
    fonk10(b8)
def fonk8():
    b9 = input("Would you like to begin? (yes/no)\n").strip().lower()
    if b9 = = "yes":
        global b10
        b10 = tk.Tk()
        b11 = class1(b1=b10)
        b12 = ttk.Style(b10)
        b12.theme_use('clam')
        b11.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
def fonk9():
    b13 = ["work", "sleep", "eat", "drive", "clean"]
    b7 = {}
    for activity in b13:
        b14 = float(input(f"How many b14 will you spend {activity} today?\n"))
        b7[activity] = b14 * 60
    return b7
def fonk10(b8):
    a1 = 60
    b15 = b8
    b16 = b8 % a1
    print(f"{b16} minutes available today to do something thoughtful for someone.")
    print(f"{b15} b15 available today for creating something!")
if b17 = = "__main__":
    fonk7()