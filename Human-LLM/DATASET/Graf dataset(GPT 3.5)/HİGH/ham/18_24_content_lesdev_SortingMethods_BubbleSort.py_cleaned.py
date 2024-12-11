import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
	b1 = int(b11.get())
	b2 = []
	for i in range(0,b1):
		b3 = tkSimpleDialog.askinteger("","Ingresa el numero")
		b2.append(b3)
	b4 = str(b2)
	b14.config(b5 = b4)
	for i in range(0,len(b2)-1):
		for j in range(1,len(b2)):
			if b2[j] < b2[j-1]:
				b6 = b2[j-1]
				b2[j-1] = b2[j]
				b2[j] = b6
	b7 = str(b2)
	b15.config(b5 = b7)
b8 = Tk()
b8.title("Bubble Sort")
b8.geometry('250x150')
b8.configure(b9 = 'SkyBlue2')
b10 = Label(b8, b5="Cuantos numeros vas a ingresar?", font="Helvetica 12", b9 = 'SkyBlue2')
b10.pack()
b1 = 0
b11 = Entry(b8, width=8, textvariable=b1)
b11.pack()
b12 = Button(b8, b5="Ok!", command=bubble)
b12.pack(b13 = (10,0))
b14 = Label(b8, b5="",b9 = 'SkyBlue2')
b14.pack(b13 = (10,0))
b15 = Label(b8, b5="",b9 = 'SkyBlue2')
b15.pack(b13 = (10,0))
b8.mainloop()