from tkinter import simpledialog, Label
from tkinter.ttk import Combobox
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        Label(self, b1 = "Choose component to plot:").pack()
        b2 = ["Ex", "Ey", "Ez", "Hx", "Hy", "Hz", "Ix", "Iy", "Iz"]
        self.b3 = Combobox(self, values = b2)
        self.b3.set(b2[0])
        self.b3.pack()
    def fonk2(self):
        self.b4 = self.b3.get()