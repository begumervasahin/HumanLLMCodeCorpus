import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
    try:
        b1 = int(b11.get())
    except ValueError:
        b14.config(b2 = "Please enter a valid b6.")
        return
    b3 = tkSimpleDialog.askinteger("Input", "Ingresa el nÃºmero a buscar")
    if b3 is None:
        b14.config(b2 = "Search operation canceled.")
        return
    b4 = fonk2(b1)
    if b4 is None:
        b14.config(b2 = "Operation canceled.")
        return
    b13.config(b2 = f"Lista de nÃºmeros: {b4}")
    b5 = fonk3(b4, b3)
    b14.config(b2 = b5)
def fonk2(b1):
    b4 = []
    for _ in range(b1):
        b6 = tkSimpleDialog.askinteger("Input", "Ingresa un nÃºmero:")
        if b6 is None:
            return None
        b4.append(b6)
    return b4
def fonk3(b4, b3):
    for i, b6 in enumerate(b4):
        if b6 = = b3:
            return f"Encontrado en la posiciÃ³n: {i}"
    return "NÃºmero no encontrado"
b7 = Tk()
b7.title("Sequential Search")
b7.geometry('300x250')
b7.configure(b8 = 'SkyBlue2')
b9 = Label(b7, b2="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', b8='SkyBlue2')
b9.pack(b10 = 10)
b11 = Entry(b7, width=8)
b11.pack(b10 = 5)
b12 = Button(b7, b2="Ok!", command=busqueda)
b12.pack(b10 = 10)
b13 = Label(b7, b2="", b8='SkyBlue2')
b13.pack(b10 = 10)
b14 = Label(b7, b2="", b8='SkyBlue2')
b14.pack(b10 = 10)
b7.mainloop()