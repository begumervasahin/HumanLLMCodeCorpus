import sys
from tkinter import *
import tkinter.simpledialog
def fonk1():
    b1 = int(b14.get())
    b2 = []
    b3 = tkinter.simpledialog.askinteger("", "Ingresa el numero a buscar")
    for i in range(0, b1):
        b4 = tkinter.simpledialog.askinteger("", "Ingresa los numeros en orden")
        b2.append(b4)
    b5 = str(b2)
    b17.config(b6 = b5)
    def fonk2(b2, b3):
        a1 = 0
        b7 = len(b2) - 1
        while a1 <= b7:
            b8 = (a1 + b7)
            if b2[b8] == b3:
                return b8
            elif b2[b8] > b3:
                b7 = b8 - 1
            else:
                a1 = b8 + 1
        return -1
    b9 = fonk2(b2, b3)
    b10 = "El numero esta en la posicion: %s" % (b9)
    b18.config(b6 = b10)
b11 = Tk()
b11.title("Radix Sort")
b11.geometry('250x150')
b11.configure(b12 = 'SkyBlue2')
b13 = Label(b11, b6="Cuantos numeros vas a ingresar?", font='Helvetica 12', b12='SkyBlue2')
b13.pack()
b1 = 0
b14 = Entry(b11, width=8, textvariable=b1)
b14.pack()
b15 = Button(b11, b6="Ok!", command=busqueda)
b15.pack(b16 = (10, 0))
b17 = Label(b11, b6="", b12='SkyBlue2')
b17.pack(b16 = (10, 0))
b18 = Label(b11, b6="", b12='SkyBlue2')
b18.pack(b16 = (10, 0))
b11.mainloop()