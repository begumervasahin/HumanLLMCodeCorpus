import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b11.get())
        b2 = []
        b3 = simpledialog.askinteger("Buscar NÃºmero", "Ingresa el nÃºmero que deseas buscar:")
        for i in range(b1):
            b4 = simpledialog.askinteger("Ingresar NÃºmero", f"Ingrese el nÃºmero {i + 1}:")
            b2.append(b4)
        b5 = ', '.join(map(str, b2))
        b14.config(b6 = f"NÃºmeros ingresados: {b5}")
        for index, b7 in enumerate(b2):
            if b7 = = b3:
                b15.config(b6 = f"NÃºmero encontrado en la posiciÃ³n: {index}")
                return
        b15.config(b6 = "NÃºmero no encontrado")
    except ValueError:
        b15.config(b6 = "Por favor, ingresa un nÃºmero vÃ¡lido")
b8 = tk.Tk()
b8.title("BÃºsqueda Secuencial")
b8.geometry('300x200')
b8.configure(b9 = 'SkyBlue2')
b10 = tk.Label(b8, b6="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', b9='SkyBlue2')
b10.pack()
b11 = tk.Entry(b8, width=8)
b11.pack()
b12 = tk.Button(b8, b6="Buscar", command=buscar_numero)
b12.pack(b13 = (10, 0))
b14 = tk.Label(b8, b6="", b9='SkyBlue2')
b14.pack(b13 = (10, 0))
b15 = tk.Label(b8, b6="", b9='SkyBlue2')
b15.pack(b13 = (10, 0))
b8.mainloop()