import tkinter as tk
from tkinter import simpledialog
from tkinter import Label
from tkinter.ttk import Combobox
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        super().fonk1(master)
    def fonk2(self, master):
        self.fonk4(master)
    def fonk3(self):
        self.b1 = self.b4.get()
    def fonk4(self, master):
        Label(self, b2 = "Choose component to plot:").pack(pady=10)
        b3 = ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "Ix", "Iy", "Iz"]
        self.b4 = Combobox(self, values=b3)
        self.b4.set(b3[0])
        self.b4.pack(b5 = 10, pady=10)
if b6 = = "__main__":
    def fonk5():
        b7 = tk.Tk()
        b7.withdraw()
        b8 = class1(b7)
        b7.wait_window(b8)
        b9 = b8.b1
        if b9:
            print(f"Selected component: {b9}")
        else:
            print("No component selected.")
    fonk5()