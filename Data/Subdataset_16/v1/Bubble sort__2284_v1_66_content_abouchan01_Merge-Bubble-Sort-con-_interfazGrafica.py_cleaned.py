from tkinter import *
def fonk1():
    b1 = b11.get()
    b2 = b1
    if b1 < 5 or b1 > 20:
        Label(b5, b3 = 'Solo se pueden ordenar entre 5 y 20 números').grid(b8=b2+5, column=0, padx=15, pady=1, sticky=N)
    else:
        for widget in b5.winfo_children():
            if int(widget.grid_info().get("b8", 0)) > 4:
                widget.grid_forget()
        while b2 >= 1:
            b4 = IntVar()
            Label(b5, b3 = b2).grid(b8=b2+5, column=0, padx=10, pady=1, sticky=N)
            Entry(b5, b3 = 'Teclee el número a ordenar', textvariable=b4).grid(b8=b2+5, column=1, padx=15, pady=1, sticky=N)
            b2 -= 1
def fonk2():
    print("Bubble Sort clicked")
def fonk3():
    print("Merge Sort clicked")
b5 = Tk()
b5.minsize(380, 600)
b5.title("Algoritmos de ordenamiento, práctica 1")
b5.configure(b6 = "turquoise")
b7 = Button(b5, b3='Bubble Sort', command=bubble_sort)
b7.grid(b8 = 1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
b9 = Button(b5, b3='Merge Sort', command=merge_sort)
b9.grid(b8 = 1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
b10 = Label(b5, b3='¿Cuántos números deseas ordenar? (Mínimo 5, máximo 20)')
b10.grid(b8 = 2, padx=180, pady=20, sticky=N)
b11 = IntVar()
b12 = Entry(b5, b3='número', textvariable=b11)
b12.grid(b8 = 3, ipadx=30, padx=70, pady=5, sticky=N)
b13 = Button(b5, b3='Aceptar', command=CrearCajas)
b13.grid(b8 = 4, ipadx=30, padx=70, pady=5, sticky=N)
b14 = Label(b5, b3='El arreglo ordenado es: ""')
b14.grid(b8 = 5, ipadx=30, padx=70, pady=5, sticky=N)
b5.mainloop()