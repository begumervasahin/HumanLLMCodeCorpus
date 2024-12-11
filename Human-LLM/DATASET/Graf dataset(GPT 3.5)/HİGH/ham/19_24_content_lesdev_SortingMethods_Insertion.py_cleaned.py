import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
	b1 = int(b12.get())
	b2 = []
	for i in range(0,b1):
		b3 = tkSimpleDialog.askinteger("","Ingresa el numero")
		b2.append(b3)
	b4 = str(b2)
	b15.config(b5 = b4)
	for i in range(1, len(b2)):
		b6 = i
		b7 = b2[i]
		while b6 > 0 and b7 < b2[b6 -1]:
			b2[b6] = b2[b6-1]
			b6 -= 1
			b2[b6]= b7
	b8 = str(b2)
	b16.config(b5 = b8)
b9 = Tk()
b9.title("Insertion Sort")
b9.geometry('250x150')
b9.configure(b10 = 'SkyBlue2')
b11 = Label(b9, b5="Cuantos numeros vas a ingresar?" , font="Helvetica 12", b10 = 'SkyBlue2')
b11.pack()
b1 = 0
b12 = Entry(b9, width=8, textvariable=b1)
b12.pack()
b13 = Button(b9, b5="Ok!", command=insertion)
b13.pack(b14 = (10,0))
b15 = Label(b9, b5="", b10 = 'SkyBlue2')
b15.pack(b14 = (10,0))
b16 = Label(b9, b5="",b10 = 'SkyBlue2')
b16.pack(b14 = (10,0))
b9.mainloop()