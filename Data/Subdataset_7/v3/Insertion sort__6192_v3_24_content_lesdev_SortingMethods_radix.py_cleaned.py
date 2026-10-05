from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def fonk1(b8):
    def fonk2(b8, a1):
        b1 = len(b8)
        b2 = [0] * b1
        b3 = [0] * 10
        for num in b8:
            b4 = (num
            b3[b4] += 1
        for b5 in range(1, 10):
            b3[b5] += b3[b5 - 1]
        b5 = b1 - 1
        while b5 >= 0:
            b4 = (b8[b5]
            b2[b3[b4] - 1] = b8[b5]
            b3[b4] -= 1
            b5 -= 1
        for b5 in range(b1):
            b8[b5] = b2[b5]
    def fonk3(b8):
        b6 = max(b8)
        a1 = 1
        while b6
            fonk2(b8, a1)
            a1 *= 10
    fonk3(b8)
def fonk4():
    b7 = int(b15.get())
    b8 = [tkSimpleDialog.askinteger("", "Ingresa el numero") for _ in range(b7)]
    b9 = str(b8)
    b18.config(b10 = b9)
    fonk1(b8)
    b11 = str(b8)
    b19.config(b10 = b11)
b12 = Tk()
b12.title("Radix Sort")
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