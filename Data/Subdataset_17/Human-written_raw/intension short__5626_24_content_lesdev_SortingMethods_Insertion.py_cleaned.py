import sys
from tkinter import *
import tkSimpleDialog
def insertion():
	datos = int(entrynumeros.get())
	vector = []
	for i in range(0,datos):
		dialog = tkSimpleDialog.askinteger("","Ingresa el numero")
		vector.append(dialog)
	aux_impresion1 = str(vector)
	Label2.config(text=aux_impresion1)
	for i in range(1, len(vector)):
		j = i
		aux = vector[i]
		while j > 0 and aux < vector[j -1]:
			vector[j] = vector[j-1]
			j -= 1
			vector[j]= aux
	aux_impresion2 = str(vector)
	label3.config(text=aux_impresion2)
app = Tk()
app.title("Insertion Sort")
app.geometry('250x150')
app.configure(bg = 'SkyBlue2')
Label1 = Label(app, text="Cuantos numeros vas a ingresar?" , font="Helvetica 12", bg = 'SkyBlue2')
Label1.pack()
datos = 0
entrynumeros = Entry(app, width=8, textvariable=datos)
entrynumeros.pack()
button1 = Button(app, text="Ok!", command=insertion)
button1.pack(pady=(10,0))
Label2 = Label(app, text="", bg = 'SkyBlue2')
Label2.pack(pady=(10,0))
label3 = Label(app, text="",bg = 'SkyBlue2')
label3.pack(pady=(10,0))
app.mainloop()