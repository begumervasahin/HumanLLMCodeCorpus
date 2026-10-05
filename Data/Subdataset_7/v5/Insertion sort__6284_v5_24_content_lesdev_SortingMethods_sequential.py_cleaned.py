import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1():
    b1 = int(b10.get())
    b2 = tkSimpleDialog.askinteger("", "Enter the number to search for")
    b3 = [tkSimpleDialog.askinteger("", "Enter numbers in order") for _ in range(b1)]
    b13.config(b4 = str(b3))
    b5 = fonk2(b3, b2)
    if b5 is not None:
        b14.config(b4 = f"Found at b5: {b5}")
    else:
        b14.config(b4 = "Number not found")
def fonk2(b3, b2):
    for i, b6 in enumerate(b3):
        if b6 = = b2:
            return i
    return None
b7 = Tk()
b7.title("Sequential Search")
b7.geometry('250x150')
b7.configure(b8 = 'SkyBlue2')
b9 = Label(b7, b4="How many numbers will you enter?", font="Helvetica 12", b8='SkyBlue2')
b9.pack()
b10 = Entry(b7, width=8)
b10.pack()
b11 = Button(b7, b4="Ok!", command=search)
b11.pack(b12 = (10, 0))
b13 = Label(b7, b4="", b8='SkyBlue2')
b13.pack(b12 = (10, 0))
b14 = Label(b7, b4="", b8='SkyBlue2')
b14.pack(b12 = (10, 0))
b7.mainloop()