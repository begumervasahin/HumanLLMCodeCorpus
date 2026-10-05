import sys
from tkinter import *
import tkSimpleDialog
def sorting():
    datos = int(entrynumeros.get())
    vector = []
    for i in range(0,datos):
        dialog = tkSimpleDialog.askinteger("","Ingresa el numero")
        vector.append(dialog)
    aux_impresion1 = str(vector)
    Label2.config(text=aux_impresion1)
    def sort(vector, exp1):
        n = len(vector)
        salida = [0] * (n)
        conteo = [0] * (10)
        for i in range(0, n):
            index = (vector[i]/exp1)
            conteo[ (index)%10 ] += 1
        for i in range(1,10):
            conteo[i] += conteo[i-1]
        i = n-1
        while i>=0:
            index = (vector[i]/exp1)
            salida[ conteo[ (index)%10 ] - 1] = vector[i]
            conteo[ (index)%10 ] -= 1
            i -= 1
        i = 0
        for i in range(0,len(vector)):
            vector[i] = salida[i]
    def radixSort(vector):
        max1 = max(vector)
        exp = 1
        while max1/exp > 0:
            sort(vector,exp)
            exp *= 10
    radixSort(vector)
    aux_impresion2 = str(vector)
    label3.config(text=aux_impresion2),
app = Tk()
app.title("Radix Sort")
app.geometry('250x150')
app.configure(bg = 'SkyBlue2')
Label1 = Label(app, text="Cuantos numeros vas a ingresar?",font='Helvetica 12', bg = 'SkyBlue2')
Label1.pack()
datos = 0
entrynumeros = Entry(app, width=8, textvariable=datos)
entrynumeros.pack()
button1 = Button(app, text="Ok!", command=sorting)
button1.pack(pady=(10,0))
Label2 = Label(app, text="",bg = 'SkyBlue2')
Label2.pack(pady=(10,0))
label3 = Label(app, text="",bg = 'SkyBlue2')
label3.pack(pady=(10,0))
app.mainloop()