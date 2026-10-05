from tkinter import *
Grafica= Tk()
Grafica.minsize(380,600)
Grafica.title("Algoritmos de ordenamiento, practica 1")
Grafica.configure(background="turquoise")
def CrearCajas():
	restante = (numCajas.get())
	i = restante
	if restante < 5 or restante > 20:
		caja = Label(Grafica,text='Solo se pueden ordenar entre 5 y 20 numeros') .grid(row= i+5,column = 0, padx=15, pady=1, sticky = N)
	else:
		while i >= 1:
				print ("desc0ontando y prueba"+ str(restante))
				numeroDeArr = IntVar()
				lblElemento = Label(Grafica,text = i ) .grid(row= i+5,column = 0, padx= 10, pady=1, sticky = N)
				caja = Entry(Grafica,text='Teclee el numero a ordenar', textvariable = numeroDeArr) .grid(row= i+5,column = 1, padx=15, pady=1, sticky = N)
				texto = Entry(Grafica)
				i -= 1
		pass
arreglo = {}
bubbleButton = Button(Grafica,text='Bubble Sort') .grid(row=1 , column= 0, ipadx = 35, padx= 40, pady = 15, sticky = NW)
mergeButton = Button(Grafica, text='Merge Sort') .grid(row=1 , column = 1 ,ipadx = 35,padx= 40 ,pady = 15, sticky= NE)
lblPregunta = Label(Grafica,text='Â¿Cuantos nÃºmeros deseas ordenar? (Minimo 5,mÃ¡ximo 20)') .grid(row= 2, padx= 180, pady=20, sticky = N)
numCajas = IntVar()
textNum = Entry(Grafica, text= 'nÃºmero', textvariable=numCajas).grid(row=3,ipadx=30, padx= 70, pady=5, sticky = N)
aceptar = Button(Grafica, text= 'aceptar', command= CrearCajas) .grid(row=4,ipadx=30, padx= 70, pady=5, sticky = N)
cadenaOrdenada = Label(Grafica, text='El arreglo ordenado es:+""arrOrd""',) .grid(row=5,ipadx=30, padx= 70, pady=5, sticky = N)
Grafica.mainloop()