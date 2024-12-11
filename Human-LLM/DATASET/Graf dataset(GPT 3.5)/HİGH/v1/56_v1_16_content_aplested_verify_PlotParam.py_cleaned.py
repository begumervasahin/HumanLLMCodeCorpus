import sys
from tkinter import *
from tkinter import simpledialog
class class1(simpledialog.Dialog):
    def fonk1(self, master):
        self.title('Enter new plot parameters...')
        Label(master, b1 = 'Min X:').grid(b3=0)
        Label(master, b1 = 'Max X:').grid(b3=1)
        Label(master, b1 = 'Bin width:').grid(b3=2)
        Label(master, b1 = 'Max Y:').grid(b3=3)
        self.b2 = Entry(master, justify=CENTER)
        self.b2.grid(b3 = 0, column=1)
        self.b2.insert(END, '0')
        self.b4 = Entry(master, justify=CENTER)
        self.b4.grid(b3 = 1, column=1)
        self.b4.insert(END, '10')
        self.b5 = Entry(master, justify=CENTER)
        self.b5.grid(b3 = 2, column=1)
        self.b5.insert(END, '1')
        self.b6 = Entry(master, justify=CENTER)
        self.b6.grid(b3 = 3, column=1)
        self.b6.insert(END, '1000')
        return self.b2
    def fonk2(self):
        self.b7 = int(self.b2.get())
        self.b8 = int(self.b4.get())
        self.b9 = int(self.b5.get())
        self.b10 = int(self.b6.get())
if b11 = = "__main__":
    b12 = Tk()
    b13 = class1(b12)
    print("Min X:", b13.b7)
    print("Max X:", b13.b8)
    print("Bin width:", b13.b9)
    print("Max Y:", b13.b10)
    b12.mainloop()