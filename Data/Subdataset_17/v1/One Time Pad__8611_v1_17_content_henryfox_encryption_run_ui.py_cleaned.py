import encrypt
from tkinter import *
class Btn:
    def __init__(self, window, text, grid_col, grid_row, function):
        button = Button(window, text=text, command=function)
        button.grid(column=grid_col, row=grid_row)
class Inp:
    def __init__(self, window, grid_col, grid_row):
        self.entry = Entry(window)
        self.entry.grid(column=grid_col, row=grid_row)
class DropDown:
    def __init__(self, window, options, grid_col, grid_row):
        self.variable = StringVar(window)
        self.variable.set(options[0])
        dropdown = OptionMenu(window, self.variable, *options)
        dropdown.grid(column=grid_col, row=grid_row)
root = Tk()
input_field = Inp(root, 1, 1)
root.mainloop()