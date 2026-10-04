from tkinter import *
b1 = Tk()
b1.minsize(380, 600)
b1.title("Algoritmos de ordenamiento, practica 1")
b1.configure(b2 = "turquoise")
def fonk1():
    b3 = b6.get()
    if b3 < 5 or b3 > 20:
        Label(b1, b4 = 'Solo se pueden ordenar entre 5 y 20 números').grid(row=b3 + 5, column=0, padx=15, pady=1, sticky=N)
    else:
        for i in range(b3, 0, -1):
            print("Creating entry box for element " + str(i))
            b5 = IntVar()
            Label(b1, b4 = i).grid(row=i + 5, column=0, padx=10, pady=1, sticky=N)
            Entry(b1, b4 = 'Teclee el número a ordenar', textvariable=b5).grid(row=i + 5, column=1, padx=15, pady=1, sticky=N)
b6 = IntVar()
Button(b1, b4 = 'Bubble Sort').grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
Button(b1, b4 = 'Merge Sort').grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
Label(b1, b4 = '¿Cuántos números deseas ordenar? (Mínimo 5, máximo 20)').grid(row=2, padx=180, pady=20, sticky=N)
Entry(b1, b4 = 'Número', textvariable=b6).grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
Button(b1, b4 = 'Aceptar', command=create_boxes).grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
Label(b1, b4 = 'El arreglo ordenado es: ""arrOrd""').grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
b1.mainloop()