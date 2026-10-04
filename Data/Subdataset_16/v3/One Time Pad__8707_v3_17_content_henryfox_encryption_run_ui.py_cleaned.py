import tkinter as tk
from tkinter import Button, Entry, OptionMenu, StringVar
class class1:
    def fonk1(self, window, text, grid_col, grid_row, function):
        b1 = Button(window, text=text, command=function)
        b1.grid(b2 = grid_col, row=grid_row)
class class2:
    def fonk2(self, window, grid_col, grid_row):
        self.b3 = Entry(window)
        self.b3.grid(b2 = grid_col, row=grid_row)
class class3:
    def fonk3(self, window, b8, grid_col, grid_row):
        self.b4 = StringVar(window)
        self.b4.set(b8[0])
        b5 = OptionMenu(window, self.b4, *b8)
        b5.grid(b2 = grid_col, row=grid_row)
def fonk4():
    print("Button clicked!")
def fonk5():
    b6 = tk.Tk()
    b6.title("Sample Application")
    b7 = class2(b6, 1, 1)
    b1 = class1(b6, "Click Me", 1, 2, example_function)
    b8 = ["Option 1", "Option 2", "Option 3"]
    b5 = class3(b6, b8, 1, 3)
    b6.mainloop()
if b9 = = '__main__':
    fonk5()