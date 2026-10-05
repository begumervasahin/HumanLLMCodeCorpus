from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1():
    b1 = int(b10.get())
    b2 = []
    for _ in range(b1):
        b3 = tkSimpleDialog.askinteger("", "Enter a b3")
        b2.append(b3)
    b13.config(b4 = str(b2))
    for i in range(1, len(b2)):
        b5 = i
        b6 = b2[i]
        while b5 > 0 and b6 < b2[b5 - 1]:
            b2[b5] = b2[b5 - 1]
            b5 -= 1
        b2[b5] = b6
    b14.config(b4 = str(b2))
b7 = Tk()
b7.title("Insertion Sort")
b7.geometry('250x150')
b7.configure(b8 = 'SkyBlue2')
b9 = Label(b7, b4="How many numbers will you enter?", font="Helvetica 12", b8='SkyBlue2')
b9.pack()
b10 = Entry(b7, width=8)
b10.pack()
b11 = Button(b7, b4="Ok!", command=insertion_sort)
b11.pack(b12 = (10, 0))
b13 = Label(b7, b4="", b8='SkyBlue2')
b13.pack(b12 = (10, 0))
b14 = Label(b7, b4="", b8='SkyBlue2')
b14.pack(b12 = (10, 0))
b7.mainloop()