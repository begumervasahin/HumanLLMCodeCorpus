from tkinter import *
root = Tk()
root.minsize(380, 600)
root.title("Algoritmos de ordenamiento, practica 1")
root.configure(background="turquoise")
def create_boxes():
    remaining = num_boxes.get()
    if remaining < 5 or remaining > 20:
        Label(root, text='Solo se pueden ordenar entre 5 y 20 números').grid(row=remaining + 5, column=0, padx=15, pady=1, sticky=N)
    else:
        for i in range(remaining, 0, -1):
            print("Creating entry box for element " + str(i))
            num_var = IntVar()
            Label(root, text=i).grid(row=i + 5, column=0, padx=10, pady=1, sticky=N)
            Entry(root, text='Teclee el número a ordenar', textvariable=num_var).grid(row=i + 5, column=1, padx=15, pady=1, sticky=N)
num_boxes = IntVar()
Button(root, text='Bubble Sort').grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
Button(root, text='Merge Sort').grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
Label(root, text='¿Cuántos números deseas ordenar? (Mínimo 5, máximo 20)').grid(row=2, padx=180, pady=20, sticky=N)
Entry(root, text='Número', textvariable=num_boxes).grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
Button(root, text='Aceptar', command=create_boxes).grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
Label(root, text='El arreglo ordenado es: ""arrOrd""').grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
root.mainloop()