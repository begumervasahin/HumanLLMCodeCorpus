import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1():
    b1 = int(b9.get())
    b2 = []
    for _ in range(b1):
        b3 = tkSimpleDialog.askinteger("", "Enter a b3")
        b2.append(b3)
    b12.config(b4 = str(b2))
    for i in range(len(b2)-1):
        b5 = i
        for j in range(i+1, len(b2)):
            if b2[j] < b2[b5]:
                b5 = j
        b2[i], b2[b5] = b2[b5], b2[i]
    b13.config(b4 = str(b2))
b6 = Tk()
b6.title("Selection Sort")
b6.configure(b7 = 'SkyBlue2')
b8 = Label(b6, b4="How many numbers will you enter?", font="Helvetica 12", b7='SkyBlue2')
b8.pack()
b9 = Entry(b6, width=8)
b9.pack()
b10 = Button(b6, b4="Ok!", command=selection_sort)
b10.pack(b11 = (10, 0))
b12 = Label(b6, b4="", b7='SkyBlue2')
b12.pack(b11 = (10, 0))
b13 = Label(b6, b4="", b7='SkyBlue2')
b13.pack(b11 = (10, 0))
b6.mainloop()