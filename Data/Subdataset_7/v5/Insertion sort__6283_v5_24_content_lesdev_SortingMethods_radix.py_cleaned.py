import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1(b8):
    def fonk2(b8, a1):
        b1 = len(b8)
        b2 = [0] * b1
        b3 = [0] * 10
        for b5 in range(b1):
            b4 = int(b8[b5] / a1) % 10
            b3[b4] += 1
        for b5 in range(1, 10):
            b3[b5] += b3[b5 - 1]
        b5 = b1 - 1
        while b5 >= 0:
            b4 = int(b8[b5] / a1) % 10
            b2[b3[b4] - 1] = b8[b5]
            b3[b4] -= 1
            b5 -= 1
        for b5 in range(b1):
            b8[b5] = b2[b5]
    b6 = max(b8)
    a1 = 1
    while b6 / a1 > 0:
        fonk2(b8, a1)
        a1 *= 10
def fonk3():
    b7 = int(b16.get())
    b8 = []
    for _ in range(b7):
        b9 = tkSimpleDialog.askinteger("", "Ingresa el numero")
        b8.append(b9)
    b10 = str(b8)
    b19.config(b11 = b10)
    fonk1(b8)
    b12 = str(b8)
    b20.config(b11 = b12)
b13 = Tk()
b13.title("Radix Sort")
b13.geometry('250x200')
b13.configure(b14 = 'SkyBlue2')
b15 = Label(b13, b11="Cuantos numeros vas a ingresar?", font='Helvetica 12', b14='SkyBlue2')
b15.pack()
b16 = Entry(b13, width=8)
b16.pack()
b17 = Button(b13, b11="Ok!", command=sorting)
b17.pack(b18 = (10, 0))
b19 = Label(b13, b11="", b14='SkyBlue2')
b19.pack(b18 = (10, 0))
b20 = Label(b13, b11="", b14='SkyBlue2')
b20.pack(b18 = (10, 0))
b13.mainloop()