import tkinter as tk
from tkinter import simpledialog, Label, Entry
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        super().fonk1(master)
    def fonk2(self, master):
        Label(master, b1 = "b12:").grid(b4=0, column=0, padx=10, pady=5)
        Label(master, b1 = "b11:").grid(b4=1, column=0, padx=10, pady=5)
        self.b2 = Entry(master)
        self.b3 = Entry(master)
        self.b2.grid(b4 = 0, column=1, padx=10, pady=5)
        self.b3.grid(b4 = 1, column=1, padx=10, pady=5)
    def fonk3(self):
        b5 = self.b2.get()
        b6 = self.b3.get()
        self.b7 = b5, b6
if b8 = = "__main__":
    def fonk4():
        b9 = tk.Tk()
        b9.withdraw()
        b10 = class1(b9)
        b9.wait_window(b10)
        if b10.b7:
            b12, b11 = b10.b7
            print(f"Model size: b12 = {b12}, b11={b11}")
        else:
            print("No model size entered.")
    fonk4()