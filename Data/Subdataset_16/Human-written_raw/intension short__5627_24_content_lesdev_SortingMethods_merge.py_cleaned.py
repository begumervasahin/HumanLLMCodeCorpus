import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
	b1 = int(b13.get())
	b2 = []
	for a1 in range(0,b1):
		b3 = tkSimpleDialog.askinteger("","Ingresa el numero")
		b2.append(b3)
	b4 = str(b2)
	b16.config(b5 = b4)
	def fonk2(b2):
	    if len(b2)>1:
	        b6 = len(b2)
	        b7 = b2[:b6]
	        b8 = b2[b6:]
	        fonk2(b7)
	        fonk2(b8)
	        a1 = 0
	        a2 = 0
	        a3 = 0
	        while a1 < len(b7) and a2 < len(b8):
	            if b7[a1] < b8[a2]:
	                b2[a3] = b7[a1]
	                a1 += 1
	            else:
	                b2[a3]=b8[a2]
	                a2 += 1
	            a3 += 1
	        while a1 < len(b7):
	            b2[a3] = b7[a1]
	            a1 += 1
	            a3 += 1
	        while a2 < len(b8):
	            b2[a3]=b8[a2]
	            a2 += 1
	            a3 += 1
	fonk2(b2)
	b9 = str(b2)
	b17.config(b5 = b9),
b10 = Tk()
b10.title("Merge Sort")
b10.geometry('250x150')
b10.configure(b11 = 'SkyBlue2')
b12 = Label(b10, b5="Cuantos numeros vas a ingresar?", font="Helvetica 12", b11 = 'SkyBlue2')
b12.pack()
b1 = 0
b13 = Entry(b10, width=8, textvariable=b1)
b13.pack()
b14 = Button(b10, b5="Ok!", command=sorting)
b14.pack(b15 = (10,0))
b16 = Label(b10, b5="",b11 = 'SkyBlue2')
b16.pack(b15 = (10,0))
b17 = Label(b10, b5="",b11 = 'SkyBlue2')
b17.pack(b15 = (10,0))
b10.mainloop()