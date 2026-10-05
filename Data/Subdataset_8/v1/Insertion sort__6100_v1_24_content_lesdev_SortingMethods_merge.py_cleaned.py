from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector)
        lefthalf = vector[:mid]
        righthalf = vector[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                vector[k] = lefthalf[i]
                i += 1
            else:
                vector[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            vector[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            vector[k] = righthalf[j]
            j += 1
            k += 1
def sorting():
    datos = int(entrynumeros.get())
    vector = []
    for i in range(0, datos):
        dialog = tkSimpleDialog.askinteger("", "Ingresa el numero")
        vector.append(dialog)
    aux_impresion1 = str(vector)
    Label2.config(text=aux_impresion1)
    merge_sort(vector)
    aux_impresion2 = str(vector)
    label3.config(text=aux_impresion2)
app = Tk()
app.title("Merge Sort")
app.geometry('250x200')
app.configure(bg='SkyBlue2')
Label1 = Label(app, text="Cuantos numeros vas a ingresar?", font="Helvetica 12", bg='SkyBlue2')
Label1.pack()
entrynumeros = Entry(app, width=8)
entrynumeros.pack()
button1 = Button(app, text="Ok!", command=sorting)
button1.pack(pady=(10, 0))
Label2 = Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()