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
        self.var = StringVar(window)
        self.var.set(options[0])
        dropdown = OptionMenu(window, self.var, *options)
        dropdown.grid(column=grid_col, row=grid_row)
def main():
    root = Tk()
    root.title("Simple GUI")
    input_field = Inp(root, 1, 1)
    button = Btn(root, text="Submit", grid_col=2, grid_row=1, function=lambda: print("Button clicked!"))
    dropdown = DropDown(root, options=["Option 1", "Option 2", "Option 3"], grid_col=1, grid_row=2)
    root.mainloop()
if __name__ == "__main__":
    main()