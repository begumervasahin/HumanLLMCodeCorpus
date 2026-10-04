import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
    b1 = int(b10.get())
    b2 = []
    b3 = tkSimpleDialog.askinteger("", "Ingresa el nÃºmero a buscar")
    for i in range(b1):
        b4 = tkSimpleDialog.askinteger("", "Ingresa los nÃºmeros en orden")
        b2.append(b4)
    b13.config(b5 = str(b2))
    b6 = fonk2(b2, b3)
    b14.config(b5 = b6)
def fonk2(b2, b3):
    for i, b4 in enumerate(b2):
        if b4 = = b3:
            return f"Encontrado en la posiciÃ³n: {i}"
    return "NÃºmero no encontrado"
b7 = Tk()
b7.title("Radix Sort")
b7.geometry('250x200')
b7.configure(b8 = 'SkyBlue2')
b9 = Label(b7, b5="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', b8='SkyBlue2')
b9.pack()
b10 = Entry(b7, width=8)
b10.pack()
b11 = Button(b7, b5="Ok!", command=busqueda)
b11.pack(b12 = (10, 0))
b13 = Label(b7, b5="", b8='SkyBlue2')
b13.pack(b12 = (10, 0))
b14 = Label(b7, b5="", b8='SkyBlue2')
b14.pack(b12 = (10, 0))
b7.mainloop()