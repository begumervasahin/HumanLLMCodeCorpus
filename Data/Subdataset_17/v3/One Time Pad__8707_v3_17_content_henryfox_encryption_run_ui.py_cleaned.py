import tkinter as tk
from tkinter import Button, Entry, OptionMenu, StringVar
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
def example_function():
    print("Button clicked!")
def main():
    root = tk.Tk()
    root.title("Sample Application")
    input_field = Inp(root, 1, 1)
    button = Btn(root, "Click Me", 1, 2, example_function)
    options = ["Option 1", "Option 2", "Option 3"]
    dropdown = DropDown(root, options, 1, 3)
    root.mainloop()
if __name__ == '__main__':
    main()