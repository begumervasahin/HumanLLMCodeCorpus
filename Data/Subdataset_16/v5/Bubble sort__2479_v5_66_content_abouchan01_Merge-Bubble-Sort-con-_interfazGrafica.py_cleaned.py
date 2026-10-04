from tkinter import *
def fonk1():
    b1 = b9.get()
    if b1 < 5 or b1 > 20:
        b2 = Label(
            b7, b3 = 'Solo se pueden ordenar entre 5 y 20 números', bg="turquoise"
        )
        b2.grid(b4 = b1 + 5, column=0, padx=15, pady=1, sticky=N)
    else:
        for i in range(b1, 0, -1):
            print(f"Creating entry box for element {i}")
            b5 = IntVar()
            Label(b7, b3 = i, bg="turquoise").grid(b4=i + 5, column=0, padx=10, pady=1, sticky=N)
            Entry(b7, b6 = b5).grid(b4=i + 5, column=1, padx=15, pady=1, sticky=N)
b7 = Tk()
b7.minsize(380, 600)
b7.title("Algoritmos de ordenamiento, practica 1")
b7.configure(b8 = "turquoise")
b9 = IntVar()
Button(b7, b3 = 'Bubble Sort').grid(b4=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
Button(b7, b3 = 'Merge Sort').grid(b4=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
Label(b7, b3 = '¿Cuántos números deseas ordenar? (Mínimo 5, máximo 20)', bg="turquoise").grid(
    b4 = 2, padx=180, pady=20, sticky=N
)
Entry(b7, b6 = b9).grid(b4=3, ipadx=30, padx=70, pady=5, sticky=N)
Button(b7, b3 = 'Aceptar', command=create_boxes).grid(b4=4, ipadx=30, padx=70, pady=5, sticky=N)
Label(b7, b3 = 'El arreglo ordenado es: ""arrOrd""', bg="turquoise").grid(
    b4 = 5, ipadx=30, padx=70, pady=5, sticky=N
)
b7.mainloop()