from tkinter import *
b1 = Tk()
b1.minsize(380,600)
b1.title("Algoritmos de ordenamiento, practica 1")
b1.configure(b2 = "turquoise")
def fonk1():
	b3 = (b13.get())
	b4 = b3
	if b3 < 5 or b3 > 20:
		b5 = Label(b1,text='Solo se pueden ordenar entre 5 y 20 numeros') .grid(row= b4+5,column = 0, padx=15, pady=1, sticky = N)
	else:
		while b4 >= 1:
				print ("desc0ontando y prueba"+ str(b3))
				b6 = IntVar()
				b7 = Label(b1,text = b4 ) .grid(row= b4+5,column = 0, padx= 10, pady=1, sticky = N)
				b5 = Entry(b1,text='Teclee el numero a ordenar', textvariable = b6) .grid(row= b4+5,column = 1, padx=15, pady=1, sticky = N)
				b8 = Entry(b1)
				b4 -= 1
		pass
b9 = {}
b10 = Button(b1,text='Bubble Sort') .grid(row=1 , column= 0, ipadx = 35, padx= 40, pady = 15, sticky = NW)
b11 = Button(b1, text='Merge Sort') .grid(row=1 , column = 1 ,ipadx = 35,padx= 40 ,pady = 15, sticky= NE)
b12 = Label(b1,text='Â¿Cuantos nÃºmeros deseas ordenar? (Minimo 5,mÃ¡ximo 20)') .grid(row= 2, padx= 180, pady=20, sticky = N)
b13 = IntVar()
b14 = Entry(b1, text= 'nÃºmero', textvariable=b13).grid(row=3,ipadx=30, padx= 70, pady=5, sticky = N)
b15 = Button(b1, text= 'b15', command= CrearCajas) .grid(row=4,ipadx=30, padx= 70, pady=5, sticky = N)
b16 = Label(b1, text='El b9 ordenado es:+""arrOrd""',) .grid(row=5,ipadx=30, padx= 70, pady=5, sticky = N)
b1.mainloop()