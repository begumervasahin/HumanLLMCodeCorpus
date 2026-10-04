import sys
from tkinter import *
import tkSimpleDialog
def busqueda():
    try:
        num_elements = int(entry_num_elements.get())
    except ValueError:
        label3.config(text="Please enter a valid number.")
        return
    search_number = tkSimpleDialog.askinteger("Input", "Ingresa el nÃºmero a buscar")
    if search_number is None:
        label3.config(text="Search operation canceled.")
        return
    numbers = get_numbers(num_elements)
    if numbers is None:
        label3.config(text="Operation canceled.")
        return
    Label2.config(text=f"Lista de nÃºmeros: {numbers}")
    search_result = secuencial(numbers, search_number)
    label3.config(text=search_result)
def get_numbers(num_elements):
    numbers = []
    for _ in range(num_elements):
        number = tkSimpleDialog.askinteger("Input", "Ingresa un nÃºmero:")
        if number is None:
            return None
        numbers.append(number)
    return numbers
def secuencial(numbers, search_number):
    for i, number in enumerate(numbers):
        if number == search_number:
            return f"Encontrado en la posiciÃ³n: {i}"
    return "NÃºmero no encontrado"
app = Tk()
app.title("Sequential Search")
app.geometry('300x250')
app.configure(bg='SkyBlue2')
Label1 = Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack(pady=10)
entry_num_elements = Entry(app, width=8)
entry_num_elements.pack(pady=5)
button1 = Button(app, text="Ok!", command=busqueda)
button1.pack(pady=10)
Label2 = Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=10)
label3 = Label(app, text="", bg='SkyBlue2')
label3.pack(pady=10)
app.mainloop()