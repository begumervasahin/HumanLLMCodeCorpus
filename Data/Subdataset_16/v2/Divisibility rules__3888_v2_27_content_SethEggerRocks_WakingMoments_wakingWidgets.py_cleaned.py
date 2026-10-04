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
def fonk5():
    b5 = 24 * 60
    b6 = [
        ("work", "How many hours will you work today?\n"),
        ("sleep", "How many hours will you sleep today?\n"),
        ("eat", "How many hours will you spend eating today?\n"),
        ("drive", "How many hours will you spend driving today?\n"),
        ("clean", "How many hours will you spend cleaning today?\n")
    ]
    b7 = sum(float(input(prompt)) * 60 for _, prompt in b6)
    b8 = b5 - b7
    b9 = b8
    b10 = b8 % 60
    print(f"{b10} minutes available today to do something thoughtful for someone.")
    print(f"{b9} b9 available today for creating something!")
def fonk6():
    b11 = input("Would you like to begin?\n").strip().lower()
    if b11 = = "yes":
        b12 = tk.Tk()
        b13 = class1(b1=b12)
        b14 = ttk.Style(b12)
        b14.theme_use('clam')
        b13.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    fonk5()
if b15 = = "__main__":
    fonk6()