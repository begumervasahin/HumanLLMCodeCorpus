import tkinter as tk
from tkinter import simpledialog
from tkinter import Label
from tkinter.ttk import Combobox
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        super().fonk1(master)
    def fonk2(self, master):
        Label(self, b1 = "Choose component to plot:").pack(pady=10)
        b2 = ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "Ix", "Iy", "Iz"]
        self.b3 = Combobox(self, values=b2)
        self.b3.set(b2[0])
        self.b3.pack(b4 = 10, pady=10)
    def fonk3(self):
        self.b5 = self.b3.get()
if b6 = = "__main__":
    b7 = tk.Tk()
    b7.withdraw()
    b8 = class1(b7)
    b7.wait_window(b8)
    if b8.b5:
        print(f"Selected component: {b8.b5}")
    else:
        print("No component selected.")