import tkinter as tk
from tkinter import simpledialog, Label
from tkinter.ttk import Combobox
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        self.fonk2(master)
    def fonk2(self, master):
        Label(self, b1 = "Choose component to plot:").pack(pady=10)
        b2 = ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "Ix", "Iy", "Iz"]
        self.b3 = Combobox(self, values=b2)
        self.b3.set(b2[0])
        self.b3.pack(b4 = 10, pady=10)
    def fonk3(self):
        self.b5 = self.b3.get()
def fonk4():
    b6 = tk.Tk()
    b6.withdraw()
    b7 = class1(b6)
    b6.wait_window(b7)
    b8 = b7.b5
    if b8:
        print(f"Selected component: {b8}")
    else:
        print("No component selected.")
if b9 = = "__main__":
    fonk4()