import sys
from tkinter import *
import tkSimpleDialog
def busqueda():
    num_elements = int(entry_num_elements.get())
    numbers = []
    search_number = tkSimpleDialog.askinteger("", "Ingresa el nÃºmero a buscar")
    for i in range(num_elements):
        number = tkSimpleDialog.askinteger("", "Ingresa los nÃºmeros en orden")
        numbers.append(number)
    Label2.config(text=str(numbers))
    search_result = secuencial(numbers, search_number)
    label3.config(text=search_result)
def secuencial(numbers, search_number):
    for i, number in enumerate(numbers):
        if number == search_number:
            return f"Encontrado en la posiciÃ³n: {i}"
    return "NÃºmero no encontrado"
app = Tk()
app.title("Radix Sort")
app.geometry('250x200')
app.configure(bg='SkyBlue2')
Label1 = Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack()
entry_num_elements = Entry(app, width=8)
entry_num_elements.pack()
button1 = Button(app, text="Ok!", command=busqueda)
button1.pack(pady=(10, 0))
Label2 = Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()