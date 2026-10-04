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
b6 = Tk()
b7 = class2(b6, 1, 1)
b6.mainloop()