from tkinter import *
def create_boxes():
    num_boxes = num_cajas.get()
    for widget in grafica.winfo_children():
        if int(widget.grid_info().get("row", 0)) > 4:
            widget.grid_forget()
    if num_boxes < 5 or num_boxes > 20:
        Label(grafica, text='Solo se pueden ordenar entre 5 y 20 números').grid(row=10, column=0, padx=15, pady=1, sticky=N)
    else:
        for i in range(num_boxes, 0, -1):
            num_var = IntVar()
            Label(grafica, text=f'Número {i}:').grid(row=i+5, column=0, padx=10, pady=1, sticky=N)
            Entry(grafica, textvariable=num_var).grid(row=i+5, column=1, padx=15, pady=1, sticky=N)
def bubble_sort():
    print("Bubble Sort clicked")
def merge_sort():
    print("Merge Sort clicked")
grafica = Tk()
grafica.minsize(380, 600)
grafica.title("Algoritmos de ordenamiento, práctica 1")
grafica.configure(background="turquoise")
Button(grafica, text='Bubble Sort', command=bubble_sort).grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
Button(grafica, text='Merge Sort', command=merge_sort).grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
Label(grafica, text='¿Cuántos números deseas ordenar? (Mínimo 5, máximo 20)').grid(row=2, padx=180, pady=20, sticky=N)
num_cajas = IntVar()
Entry(grafica, textvariable=num_cajas).grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
Button(grafica, text='Aceptar', command=create_boxes).grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
Label(grafica, text='El arreglo ordenado es: ""').grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
grafica.mainloop()