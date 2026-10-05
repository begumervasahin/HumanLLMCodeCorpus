from tkinter import *
def fonk1():
    b1 = b7.get()
    b2 = b1
    if b1 < 5 or b1 > 20:
        Label(b5, b3 = 'Solo se pueden ordenar entre 5 y 20 numeros').grid(row=b2 + 5, column=0, padx=15, pady=1, sticky=N)
    else:
        while b2 >= 1:
            print("Counting down and trying" + str(b1))
            b4 = IntVar()
            Label(b5, b3 = b2).grid(row=b2 + 5, column=0, padx=10, pady=1, sticky=N)
            Entry(b5, b3 = 'Teclee el numero a ordenar', textvariable=b4).grid(row=b2 + 5, column=1, padx=15, pady=1, sticky=N)
            b2 -= 1
b5 = Tk()
b5.minsize(380, 600)
b5.title("Algoritmos de ordenamiento, practica 1")
b5.configure(b6 = "turquoise")
Button(b5, b3 = 'Bubble Sort').grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
Button(b5, b3 = 'Merge Sort').grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
Label(b5, b3 = '¿Cuantos números deseas ordenar? (Minimo 5, máximo 20)').grid(row=2, padx=180, pady=20, sticky=N)
b7 = IntVar()
Entry(b5, b3 = 'número', textvariable=b7).grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
Button(b5, b3 = 'aceptar', command=create_entry_boxes).grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
Label(b5, b3 = 'El arreglo ordenado es:').grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
b5.mainloop()