import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1():
    b1 = int(b11.get())
    b2 = []
    b3 = tkSimpleDialog.askinteger("", "Enter the b4 to search for")
    for _ in range(b1):
        b4 = tkSimpleDialog.askinteger("", "Enter numbers in order")
        b2.append(b4)
    b14.config(b5 = str(b2))
    b6 = fonk2(b2, b3)
    if b6 is not None:
        b15.config(b5 = f"Found at b6: {b6}")
    else:
        b15.config(b5 = "Number not found")
def fonk2(b2, b3):
    for i, b7 in enumerate(b2):
        if b7 = = b3:
            return i
    return None
b8 = Tk()
b8.title("Sequential Search")
b8.geometry('250x150')
b8.configure(b9 = 'SkyBlue2')
b10 = Label(b8, b5="How many numbers will you enter?", font="Helvetica 12", b9='SkyBlue2')
b10.pack()
b11 = Entry(b8, width=8)
b11.pack()
b12 = Button(b8, b5="Ok!", command=search)
b12.pack(b13 = (10, 0))
b14 = Label(b8, b5="", b9='SkyBlue2')
b14.pack(b13 = (10, 0))
b15 = Label(b8, b5="", b9='SkyBlue2')
b15.pack(b13 = (10, 0))
b8.mainloop()