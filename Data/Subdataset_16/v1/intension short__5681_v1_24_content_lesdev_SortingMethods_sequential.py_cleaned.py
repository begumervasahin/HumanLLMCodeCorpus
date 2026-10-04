import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b12.get())
        b2 = []
        b3 = simpledialog.askinteger("Buscar NÃºmero", "Ingresa el nÃºmero a buscar:")
        for i in range(b1):
            b4 = simpledialog.askinteger("Ingresar NÃºmero", f"Ingrese el nÃºmero {i + 1}:")
            b2.append(b4)
        b5 = ', '.join(map(str, b2))
        b15.config(b6 = f"NÃºmeros ingresados: {b5}")
        for i, b7 in enumerate(b2):
            if b7 = = b3:
                b8 = f"Encontrado en la posiciÃ³n: {i}"
                b16.config(b6 = b8)
                return
        b16.config(b6 = "NÃºmero no encontrado")
    except ValueError:
        b16.config(b6 = "Por favor, ingresa un nÃºmero vÃ¡lido")
b9 = tk.Tk()
b9.title("BÃºsqueda Secuencial")
b9.geometry('300x200')
b9.configure(b10 = 'SkyBlue2')
b11 = tk.Label(b9, b6="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', b10='SkyBlue2')
b11.pack()
b12 = tk.Entry(b9, width=8)
b12.pack()
b13 = tk.Button(b9, b6="Ok!", command=busqueda)
b13.pack(b14 = (10, 0))
b15 = tk.Label(b9, b6="", b10='SkyBlue2')
b15.pack(b14 = (10, 0))
b16 = tk.Label(b9, b6="", b10='SkyBlue2')
b16.pack(b14 = (10, 0))
b9.mainloop()