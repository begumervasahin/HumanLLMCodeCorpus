import sys
from tkinter import *
import tkSimpleDialog
def sorting():
	datos = int(entrynumeros.get())
	vector = []
	for i in range(0,datos):
		dialog = tkSimpleDialog.askinteger("","Ingresa el numero")
		vector.append(dialog)
	aux_impresion1 = str(vector)
	Label2.config(text=aux_impresion1)
	def mergeSort(vector):
	    if len(vector)>1:
	        mid = len(vector)
	        lefthalf = vector[:mid]
	        righthalf = vector[mid:]
	        mergeSort(lefthalf)
	        mergeSort(righthalf)
	        i=0
	        j=0
	        k=0
	        while i < len(lefthalf) and j < len(righthalf):
	            if lefthalf[i] < righthalf[j]:
	                vector[k] = lefthalf[i]
	                i += 1
	            else:
	                vector[k]=righthalf[j]
	                j += 1
	            k += 1
	        while i < len(lefthalf):
	            vector[k] = lefthalf[i]
	            i += 1
	            k += 1
	        while j < len(righthalf):
	            vector[k]=righthalf[j]
	            j += 1
	            k += 1
	mergeSort(vector)
	aux_impresion2 = str(vector)
	label3.config(text=aux_impresion2),
app = Tk()
app.title("Merge Sort")
app.geometry('250x150')
app.configure(bg = 'SkyBlue2')
Label1 = Label(app, text="Cuantos numeros vas a ingresar?", font="Helvetica 12", bg = 'SkyBlue2')
Label1.pack()
datos = 0
entrynumeros = Entry(app, width=8, textvariable=datos)
entrynumeros.pack()
button1 = Button(app, text="Ok!", command=sorting)
button1.pack(pady=(10,0))
Label2 = Label(app, text="",bg = 'SkyBlue2')
Label2.pack(pady=(10,0))
label3 = Label(app, text="",bg = 'SkyBlue2')
label3.pack(pady=(10,0))
app.mainloop()