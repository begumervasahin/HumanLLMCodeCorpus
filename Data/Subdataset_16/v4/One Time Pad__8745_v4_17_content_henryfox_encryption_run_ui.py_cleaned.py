import encrypt
from tkinter import *
class class1:
    def fonk1(self, window, text, grid_col, grid_row, function):
        b1 = Button(window, text=text, command=function)
        b1.grid(b2 = grid_col, row=grid_row)
class class2:
    def fonk2(self, window, grid_col, grid_row):
        self.b3 = Entry(window)
        self.b3.grid(b2 = grid_col, row=grid_row)
class class3:
    def fonk3(self, window, options, grid_col, grid_row):
        self.b4 = StringVar(window)
        self.b4.set(options[0])
        b5 = OptionMenu(window, self.b4, *options)
        b5.grid(b2 = grid_col, row=grid_row)
def fonk4():
    b6 = Tk()
    b6.title("Simple GUI")
    b7 = class2(b6, 1, 1)
    b1 = class1(b6, text="Submit", grid_col=2, grid_row=1, function=lambda: print("Button clicked!"))
    b5 = class3(b6, options=["Option 1", "Option 2", "Option 3"], grid_col=1, grid_row=2)
    b6.mainloop()
if b8 = = "__main__":
    fonk4()