import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
	b1 = int(b11.get())
	b2 = []
	b3 = tkSimpleDialog.askinteger("","Ingresa el numero a buscar")
	for i in range(0,b1):
	    b4 = tkSimpleDialog.askinteger("","Ingresa los numeros en orden")
	    b2.append(b4)
	b5 = str(b2)
	b14.config(b6 = b5)
	def fonk2(b2):
		for i in range(0,len(b2)):
			if b2[i] == b3:
				b7 = ("Encontrado en la posicion: %i" ) %i
				b15.config(b6 = b7),
	fonk2(b2)
b8 = Tk()
b8.title("Radix Sort")
b8.geometry('250x150')
b8.configure(b9 = 'SkyBlue2')
b10 = Label(b8, b6="Cuantos numeros vas a ingresar?",font='Helvetica 12', b9 = 'SkyBlue2')
b10.pack()
b1 = 0
b11 = Entry(b8, width=8, textvariable=b1)
b11.pack()
b12 = Button(b8, b6="Ok!", command=busqueda)
b12.pack(b13 = (10,0))
b14 = Label(b8, b6="",b9 = 'SkyBlue2')
b14.pack(b13 = (10,0))
b15 = Label(b8, b6="",b9 = 'SkyBlue2')
b15.pack(b13 = (10,0))
b8.mainloop()