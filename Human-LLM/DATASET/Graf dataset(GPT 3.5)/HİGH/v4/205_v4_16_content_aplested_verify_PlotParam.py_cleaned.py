import sys
if sys.version_info[0] < 3:
    from Tkinter import *
    import tkSimpleDialog
else:
    from tkinter import *
    from tkinter import simpledialog as tkSimpleDialog
b1 = "remis"
b2 = "$27-May-2009 23:02:26$"
class class1(tkSimpleDialog.Dialog):
    def fonk1(self, master):
        self.title('Enter new plot parameters...')
        Label(master, b3 = 'Min X:').grid(b5=0)
        Label(master, b3 = 'Max X:').grid(b5=1)
        Label(master, b3 = 'Bin width:').grid(b5=2)
        Label(master, b3 = 'Max Y:').grid(b5=3)
        self.b4 = Entry(master, justify=CENTER)
        self.b4.grid(b5 = 0, column=1)
        self.b4.insert(END, '0')
        self.b6 = Entry(master, justify=CENTER)
        self.b6.grid(b5 = 1, column=1)
        self.b6.insert(END, '10')
        self.b7 = Entry(master, justify=CENTER)
        self.b7.grid(b5 = 2, column=1)
        self.b7.insert(END, '1')
        self.b8 = Entry(master, justify=CENTER)
        self.b8.grid(b5 = 3, column=1)
        self.b8.insert(END, '1000')
        return self.b4
    def fonk2(self):
        self.b9 = int(self.b4.get())
        self.b10 = int(self.b6.get())
        self.b11 = int(self.b7.get())
        self.b12 = int(self.b8.get())