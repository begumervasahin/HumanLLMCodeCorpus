import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1(b6):
    if len(b6) > 1:
        b1 = len(b6)
        b2 = b6[:b1]
        b3 = b6[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            if b2[b4] < b3[j]:
                b6[k] = b2[b4]
                b4 += 1
            else:
                b6[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            b6[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            b6[k] = b3[j]
            j += 1
            k += 1
def fonk2():
    b5 = int(b14.get())
    b6 = []
    for b4 in range(b5):
        b7 = tkSimpleDialog.askinteger("", "Ingresa el numero")
        b6.append(b7)
    b8 = str(b6)
    b17.config(b9 = b8)
    fonk1(b6)
    b10 = str(b6)
    b18.config(b9 = b10)
b11 = Tk()
b11.title("Merge Sort")
b11.geometry('250x200')
b11.configure(b12 = 'SkyBlue2')
b13 = Label(b11, b9="Cuantos numeros vas a ingresar?", font="Helvetica 12", b12='SkyBlue2')
b13.pack()
b14 = Entry(b11, width=8)
b14.pack()
b15 = Button(b11, b9="Ok!", command=handle_sorting)
b15.pack(b16 = (10, 0))
b17 = Label(b11, b9="", b12='SkyBlue2')
b17.pack(b16 = (10, 0))
b18 = Label(b11, b9="", b12='SkyBlue2')
b18.pack(b16 = (10, 0))
b11.mainloop()