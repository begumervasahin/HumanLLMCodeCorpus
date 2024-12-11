import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1(b7):
    fonk2(b7, 0, len(b7) - 1)
def fonk2(b7, x, y):
    if x < y:
        b1 = fonk3(b7, x, y)
        fonk2(b7, x, b1 - 1)
        fonk2(b7, b1 + 1, y)
def fonk3(b7, x, y):
    b2 = b7[x]
    b3 = x + 1
    b4 = y
    b5 = False
    while not b5:
        while b3 <= b4 and b7[b3] <= b2:
            b3 += 1
        while b7[b4] >= b2 and b4 >= b3:
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            b7[b3], b7[b4] = b7[b4], b7[b3]
    b7[x], b7[b4] = b7[b4], b7[x]
    return b4
def fonk4():
    b6 = int(b15.get())
    b7 = []
    for _ in range(b6):
        b8 = tkSimpleDialog.askinteger("", "Ingresa el numero")
        b7.append(b8)
    b9 = str(b7)
    b18.config(b10 = b9)
    fonk1(b7)
    b11 = str(b7)
    b19.config(b10 = b11)
b12 = Tk()
b12.title("Quick Sort")
b12.geometry('250x200')
b12.configure(b13 = 'SkyBlue2')
b14 = Label(b12, b10="Cuantos numeros vas a ingresar?", font='Helvetica 12', b13='SkyBlue2')
b14.pack()
b15 = Entry(b12, width=8)
b15.pack()
b16 = Button(b12, b10="Ok!", command=sorting)
b16.pack(b17 = (10, 0))
b18 = Label(b12, b10="", b13='SkyBlue2')
b18.pack(b17 = (10, 0))
b19 = Label(b12, b10="", b13='SkyBlue2')
b19.pack(b17 = (10, 0))
b12.mainloop()