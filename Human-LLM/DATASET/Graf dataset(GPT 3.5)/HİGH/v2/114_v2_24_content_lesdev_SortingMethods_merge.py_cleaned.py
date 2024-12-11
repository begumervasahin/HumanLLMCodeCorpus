from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1(b5):
    if len(b5) > 1:
        b1 = len(b5)
        b2 = b5[:b1]
        b3 = b5[b1:]
        fonk1(b2)
        fonk1(b3)
        a1 = 0
        a2 = 0
        a3 = 0
        while a1 < len(b2) and a2 < len(b3):
            if b2[a1] < b3[a2]:
                b5[a3] = b2[a1]
                a1 += 1
            else:
                b5[a3] = b3[a2]
                a2 += 1
            a3 += 1
        while a1 < len(b2):
            b5[a3] = b2[a1]
            a1 += 1
            a3 += 1
        while a2 < len(b3):
            b5[a3] = b3[a2]
            a2 += 1
            a3 += 1
def fonk2():
    b4 = int(b13.get())
    b5 = []
    for a1 in range(b4):
        b6 = tkSimpleDialog.askinteger("", "Ingresa el numero")
        b5.append(b6)
    b7 = str(b5)
    b16.config(b8 = b7)
    fonk1(b5)
    b9 = str(b5)
    b17.config(b8 = b9)
b10 = Tk()
b10.title("Merge Sort")
b10.geometry('250x200')
b10.configure(b11 = 'SkyBlue2')
b12 = Label(b10, b8="Cuantos numeros vas a ingresar?", font="Helvetica 12", b11='SkyBlue2')
b12.pack()
b13 = Entry(b10, width=8)
b13.pack()
b14 = Button(b10, b8="Ok!", command=sorting)
b14.pack(b15 = (10, 0))
b16 = Label(b10, b8="", b11='SkyBlue2')
b16.pack(b15 = (10, 0))
b17 = Label(b10, b8="", b11='SkyBlue2')
b17.pack(b15 = (10, 0))
b10.mainloop()