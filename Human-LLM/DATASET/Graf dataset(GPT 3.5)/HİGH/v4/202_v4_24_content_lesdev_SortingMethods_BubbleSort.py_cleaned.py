import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1():
    b1 = int(b8.get())
    b2 = []
    for _ in range(b1):
        b3 = tkSimpleDialog.askinteger("", "Enter a b3")
        b2.append(b3)
    b11.config(b4 = str(b2))
    for i in range(len(b2) - 1):
        for j in range(1, len(b2)):
            if b2[j] < b2[j - 1]:
                b2[j], b2[j - 1] = b2[j - 1], b2[j]
    b12.config(b4 = str(b2))
b5 = Tk()
b5.title("Bubble Sort")
b5.geometry('250x150')
b5.configure(b6 = 'SkyBlue2')
b7 = Label(b5, b4="How many numbers will you enter?", font="Helvetica 12", b6='SkyBlue2')
b7.pack()
b8 = Entry(b5, width=8)
b8.pack()
b9 = Button(b5, b4="Ok!", command=bubble_sort)
b9.pack(b10 = (10, 0))
b11 = Label(b5, b4="", b6='SkyBlue2')
b11.pack(b10 = (10, 0))
b12 = Label(b5, b4="", b6='SkyBlue2')
b12.pack(b10 = (10, 0))
b5.mainloop()