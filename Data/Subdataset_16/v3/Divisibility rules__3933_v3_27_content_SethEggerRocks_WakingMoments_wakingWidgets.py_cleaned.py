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
        print(askcolor((255, 255, 0), self.b1))
        self.b1.destroy()
        self.fonk4()
    def fonk4(self):
        print("Bye Felicia.")
        exit()
def fonk5(prompt):
    b5 = float(input(prompt))
    return b5 * 60
def fonk6():
    b6 = 24 * 60
    b7 = [
        "How many b5 will you work today?\n",
        "How many b5 will you sleep today?\n",
        "How many b5 will you spend eating today?\n",
        "How many b5 will you spend driving today?\n",
        "How many b5 will you spend cleaning today?\n"
    ]
    b8 = sum(fonk5(prompt) for prompt in b7)
    b9 = b6 - b8
    b10 = b9
    b11 = b9 % 60
    print(f"{b11} minutes available today to do something thoughtful for someone.")
    print(f"{b10} b10 available today for creating something!")
def fonk7():
    b12 = input("Would you like to begin?\n").strip().lower()
    if b12 = = "yes":
        b13 = tk.Tk()
        b14 = class1(b1=b13)
        b15 = ttk.Style(b13)
        b15.theme_use('clam')
        b14.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    fonk6()
if b16 = = "__main__":
    fonk7()