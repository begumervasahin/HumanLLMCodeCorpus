import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1(b15):
    fonk2(b15, 0, len(b15) - 1)
def fonk2(b15, start, end):
    if start < end:
        b1 = fonk3(b15, start, end)
        fonk2(b15, start, b1 - 1)
        fonk2(b15, b1 + 1, end)
def fonk3(b15, start, end):
    b2 = b15[start]
    b3 = start + 1
    b4 = end
    b5 = False
    while not b5:
        while b3 <= b4 and b15[b3] <= b2:
            b3 += 1
        while b15[b4] >= b2 and b4 >= b3:
            b4 -= 1
        if b4 < b3:
            b5 = True
        else:
            b15[b3], b15[b4] = b15[b4], b15[b3]
    b15[start], b15[b4] = b15[b4], b15[start]
    return b4
def fonk4():
    b6 = Tk()
    b6.title("Quick Sort")
    b6.geometry('250x200')
    b6.configure(b7 = 'SkyBlue2')
    b8 = Label(b6, b18="Cuantos numeros vas a ingresar?", font='Helvetica 12', b7='SkyBlue2')
    b8.pack()
    b9 = Entry(b6, width=8)
    b9.pack()
    b10 = Button(b6, b18="Ok!", command=sorting)
    b10.pack(b11 = (10, 0))
    b12 = Label(b6, b18="", b7='SkyBlue2')
    b12.pack(b11 = (10, 0))
    b13 = Label(b6, b18="", b7='SkyBlue2')
    b13.pack(b11 = (10, 0))
    b6.mainloop()
def fonk5():
    b14 = int(b9.get())
    b15 = []
    for _ in range(b14):
        b16 = tkSimpleDialog.askinteger("", "Ingresa el numero")
        b15.append(b16)
    b17 = str(b15)
    b12.config(b18 = b17)
    fonk1(b15)
    b19 = str(b15)
    b13.config(b18 = b19)
if b20 = = "__main__":
    fonk4()