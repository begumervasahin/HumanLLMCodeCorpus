import tkinter as tk
from tkinter import simpledialog, Label, Entry
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        super().fonk1(master)
    def fonk2(self, master):
        Label(master, b1 = "b9:").grid(b4=0, column=0, padx=10, pady=5)
        Label(master, b1 = "b8:").grid(b4=1, column=0, padx=10, pady=5)
        self.b2 = Entry(master)
        self.b3 = Entry(master)
        self.b2.grid(b4 = 0, column=1, padx=10, pady=5)
        self.b3.grid(b4 = 1, column=1, padx=10, pady=5)
    def fonk3(self):
        self.b5 = (self.b2.get(), self.b3.get())
def fonk4():
    b6 = tk.Tk()
    b6.withdraw()
    b7 = class1(b6)
    b6.wait_window(b7)
    if b7.b5:
        b9, b8 = b7.b5
        print(f"Model size: b9 = {b9}, b8={b8}")
    else:
        print("No model size entered.")
if b10 = = "__main__":
    fonk4()