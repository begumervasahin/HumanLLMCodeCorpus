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
        b2 = Entry(master, justify=CENTER)
        b2.grid(b3 = 0, column=1)
        b2.insert(END, '0')
        b4 = Entry(master, justify=CENTER)
        b4.grid(b3 = 1, column=1)
        b4.insert(END, '10')
        b5 = Entry(master, justify=CENTER)
        b5.grid(b3 = 2, column=1)
        b5.insert(END, '1')
        b6 = Entry(master, justify=CENTER)
        b6.grid(b3 = 3, column=1)
        b6.insert(END, '1000')
        return b2
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