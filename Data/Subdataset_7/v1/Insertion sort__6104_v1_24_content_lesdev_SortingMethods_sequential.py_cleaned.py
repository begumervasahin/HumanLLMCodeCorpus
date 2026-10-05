import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1():
    b1 = int(b10.get())
    b2 = []
    b3 = tkSimpleDialog.askinteger("", "Enter the b4 to search for")
    for _ in range(b1):
        b4 = tkSimpleDialog.askinteger("", "Enter numbers in order")
        b2.append(b4)
    b13.config(b5 = str(b2))
    def fonk2(b2):
        for i in range(len(b2)):
            if b2[i] == b3:
                b6 = "Found at position: %i" % i
                b14.config(b5 = b6)
                return
        b14.config(b5 = "Number not found")
    fonk2(b2)
b7 = Tk()
b7.title("Sequential Search")
b7.geometry('250x150')
b7.configure(b8 = 'SkyBlue2')
b9 = Label(b7, b5="How many numbers will you enter?", font="Helvetica 12", b8='SkyBlue2')
b9.pack()
b10 = Entry(b7, width=8)
b10.pack()
b11 = Button(b7, b5="Ok!", command=search)
b11.pack(b12 = (10, 0))
b13 = Label(b7, b5="", b8='SkyBlue2')
b13.pack(b12 = (10, 0))
b14 = Label(b7, b5="", b8='SkyBlue2')
b14.pack(b12 = (10, 0))
b7.mainloop()