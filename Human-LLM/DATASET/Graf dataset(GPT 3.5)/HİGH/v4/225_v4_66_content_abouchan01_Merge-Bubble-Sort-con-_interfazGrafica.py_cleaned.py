from tkinter import *
b1 = Tk()
b1.minsize(380, 600)
b1.title("Algoritmos de ordenamiento, practica 1")
b1.configure(b2 = "turquoise")
def fonk1():
    b3 = b12.get()
    b4 = b3
    if b3 < 5 or b3 > 20:
        b5 = Label(b1, text='Solo se pueden ordenar entre 5 y 20 numeros').grid(row=b4 + 5, column=0, padx=15, pady=1, sticky=N)
    else:
        while b4 >= 1:
            print("desc0ontando y prueba" + str(b3))
            b6 = IntVar()
            b7 = Label(b1, text=b4).grid(row=b4 + 5, column=0, padx=10, pady=1, sticky=N)
            b5 = Entry(b1, text='Teclee el numero a ordenar', textvariable=b6).grid(row=b4 + 5, column=1, padx=15, pady=1, sticky=N)
            b4 -= 1
b8 = {}
b9 = Button(b1, text='Bubble Sort').grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
b10 = Button(b1, text='Merge Sort').grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
b11 = Label(b1, text='¿Cuantos números deseas ordenar? (Minimo 5, máximo 20)').grid(row=2, padx=180, pady=20, sticky=N)
b12 = IntVar()
b13 = Entry(b1, text='número', textvariable=b12).grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
b14 = Button(b1, text='b14', command=CrearCajas).grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
b15 = Label(b1, text='El b8 ordenado es:').grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
b1.mainloop()