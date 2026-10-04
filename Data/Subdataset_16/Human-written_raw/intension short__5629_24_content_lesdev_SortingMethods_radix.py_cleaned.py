import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
    b1 = int(b16.get())
    b2 = []
    for b10 in range(0,b1):
        b3 = tkSimpleDialog.askinteger("","Ingresa el numero")
        b2.append(b3)
    b4 = str(b2)
    b19.config(b5 = b4)
    def fonk2(b2, exp1):
        b6 = len(b2)
        b7 = [0] * (b6)
        b8 = [0] * (10)
        for b10 in range(0, b6):
            b9 = (b2[b10]/exp1)
            b8[ (b9)%10 ] += 1
        for b10 in range(1,10):
            b8[b10] += b8[b10-1]
        b10 = b6-1
        while b10>=0:
            b9 = (b2[b10]/exp1)
            b7[ b8[ (b9)%10 ] - 1] = b2[b10]
            b8[ (b9)%10 ] -= 1
            b10 -= 1
        b10 = 0
        for b10 in range(0,len(b2)):
            b2[b10] = b7[b10]
    def fonk3(b2):
        b11 = max(b2)
        a1 = 1
        while b11/a1 > 0:
            fonk2(b2,a1)
            a1 *= 10
    fonk3(b2)
    b12 = str(b2)
    b20.config(b5 = b12),
b13 = Tk()
b13.title("Radix Sort")
b13.geometry('250x150')
b13.configure(b14 = 'SkyBlue2')
b15 = Label(b13, b5="Cuantos numeros vas a ingresar?",font='Helvetica 12', b14 = 'SkyBlue2')
b15.pack()
b1 = 0
b16 = Entry(b13, width=8, textvariable=b1)
b16.pack()
b17 = Button(b13, b5="Ok!", command=sorting)
b17.pack(b18 = (10,0))
b19 = Label(b13, b5="",b14 = 'SkyBlue2')
b19.pack(b18 = (10,0))
b20 = Label(b13, b5="",b14 = 'SkyBlue2')
b20.pack(b18 = (10,0))
b13.mainloop()