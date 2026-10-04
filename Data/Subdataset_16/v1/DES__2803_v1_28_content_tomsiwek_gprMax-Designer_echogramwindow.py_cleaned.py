import tkinter as tk
from tkinter import simpledialog
from tkinter import Label
from tkinter.ttk import Combobox
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        super().fonk1(master)
    def fonk2(self, master):
        Label(self, b1 = "Choose component to plot:").pack()
        b2 = ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "Ix", "Iy", "Iz"]
        self.b3 = Combobox(self, values=b2)
        self.b3.set(b2[0])
        self.b3.pack()
    def fonk3(self):
        self.b4 = self.b3.get()
if b5 = = "__main__":
    b6 = tk.Tk()
    b6.withdraw()
    b7 = class1(b6)
    b6.wait_window(b7)
    if b7.b4:
        print(f"Selected component: {b7.b4}")
    else:
        print("No component selected.")