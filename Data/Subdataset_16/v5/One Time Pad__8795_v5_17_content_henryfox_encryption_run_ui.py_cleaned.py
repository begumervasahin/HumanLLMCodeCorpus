import encrypt
from tkinter import *
class class1:
    def fonk1(self, window, text, b2, row, command):
        self.b1 = Button(window, text=text, command=command)
        self.b1.grid(b2 = b2, row=row)
class class2:
    def fonk2(self, window, b2, row):
        self.b3 = Entry(window)
        self.b3.grid(b2 = b2, row=row)
class class3:
    def fonk3(self, window, options, b2, row):
        self.b4 = StringVar(window)
        self.b4.set(options[0])
        self.b5 = OptionMenu(window, self.b4, *options)
        self.b5.grid(b2 = b2, row=row)
def fonk4():
    b6 = Tk()
    b6.title("Simple GUI")
    b7 = class2(b6, b2=1, row=1)
    b8 = class1(b6, text="Submit", b2=2, row=1, command=lambda: print("Button clicked!"))
    b9 = class3(b6, options=["Option 1", "Option 2", "Option 3"], b2=1, row=2)
    b6.mainloop()
if b10 = = "__main__":
    fonk4()