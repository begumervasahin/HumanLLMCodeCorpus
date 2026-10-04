from tkinter import *
def fonk1():
    b1 = b7.get()
    for widget in b5.winfo_children():
        if int(widget.grid_info().get("row", 0)) > 4:
            widget.grid_forget()
    if b1 < 5 or b1 > 20:
        Label(b5, b2 = 'Solo se pueden ordenar entre 5 y 20 números').grid(row=10, column=0, padx=15, pady=1, sticky=N)
    else:
        for i in range(b1, 0, -1):
            b3 = IntVar()
            Label(b5, b2 = f'Número {i}:').grid(row=i+5, column=0, padx=10, pady=1, sticky=N)
            Entry(b5, b4 = b3).grid(row=i+5, column=1, padx=15, pady=1, sticky=N)
def fonk2():
    print("Bubble Sort clicked")
def fonk3():
    print("Merge Sort clicked")
b5 = Tk()
b5.minsize(380, 600)
b5.title("Algoritmos de ordenamiento, práctica 1")
b5.configure(b6 = "turquoise")
Button(b5, b2 = 'Bubble Sort', command=bubble_sort).grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
Button(b5, b2 = 'Merge Sort', command=merge_sort).grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
Label(b5, b2 = '¿Cuántos números deseas ordenar? (Mínimo 5, máximo 20)').grid(row=2, padx=180, pady=20, sticky=N)
b7 = IntVar()
Entry(b5, b4 = b7).grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
Button(b5, b2 = 'Aceptar', command=create_boxes).grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
Label(b5, b2 = 'El arreglo ordenado es: ""').grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
b5.mainloop()