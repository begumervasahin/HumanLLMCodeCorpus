from tkinter import *
import random
Grafica = Tk()
Grafica.minsize(380, 600)
Grafica.title("Algoritmos de ordenamiento, practica 1")
Grafica.configure(background="turquoise")
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def CrearCajas():
    restante = numCajas.get()
    if restante < 5 or restante > 20:
        caja = Label(Grafica, text='Solo se pueden ordenar entre 5 y 20 numeros')
        caja.grid(row=restante+5, column=0, padx=15, pady=1, sticky=N)
    else:
        for i in range(restante):
            numeroDeArr = IntVar()
            lblElemento = Label(Grafica, text=i+1)
            lblElemento.grid(row=i+6, column=0, padx=10, pady=1, sticky=N)
            caja = Entry(Grafica, text='Teclee el numero a ordenar', textvariable=numeroDeArr)
            caja.grid(row=i+6, column=1, padx=15, pady=1, sticky=N)
            arreglo[i] = numeroDeArr
def Ordenar():
    valores = [arreglo[i].get() for i in range(len(arreglo))]
    bubble_sort(valores)
    cadenaOrdenada.config(text='El arreglo ordenado es: ' + str(valores))
arreglo = {}
bubbleButton = Button(Grafica, text='Bubble Sort', command=Ordenar)
bubbleButton.grid(row=1, column=0, ipadx=35, padx=40, pady=15, sticky=NW)
mergeButton = Button(Grafica, text='Merge Sort', command=Ordenar)
mergeButton.grid(row=1, column=1, ipadx=35, padx=40, pady=15, sticky=NE)
lblPregunta = Label(Grafica, text='¿Cuantos números deseas ordenar? (Minimo 5, máximo 20)')
lblPregunta.grid(row=2, padx=180, pady=20, sticky=N)
numCajas = IntVar()
textNum = Entry(Grafica, text='número', textvariable=numCajas)
textNum.grid(row=3, ipadx=30, padx=70, pady=5, sticky=N)
aceptar = Button(Grafica, text='aceptar', command=CrearCajas)
aceptar.grid(row=4, ipadx=30, padx=70, pady=5, sticky=N)
cadenaOrdenada = Label(Grafica, text='El arreglo ordenado es: ')
cadenaOrdenada.grid(row=5, ipadx=30, padx=70, pady=5, sticky=N)
Grafica.mainloop()