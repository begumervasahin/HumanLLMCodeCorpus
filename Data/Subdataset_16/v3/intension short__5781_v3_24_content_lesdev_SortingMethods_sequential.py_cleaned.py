import tkinter as tk
from tkinter import simpledialog
def fonk1(cantidad):
    b1 = []
    for i in range(cantidad):
        b2 = simpledialog.askinteger("Ingresar NÃºmero", f"Ingrese el nÃºmero {i + 1}:")
        if b2 is not None:
            b1.append(b2)
    return b1
def fonk2(b1, b5):
    for index, b3 in enumerate(b1):
        if b3 = = b5:
            return index
    return None
def fonk3():
    try:
        b4 = int(b11.get())
        b1 = fonk1(b4)
        b5 = simpledialog.askinteger("Buscar NÃºmero", "Ingresa el nÃºmero que deseas buscar:")
        b6 = ', '.join(map(str, b1))
        b12.config(b7 = f"NÃºmeros ingresados: {b6}")
        b8 = fonk2(b1, b5)
        if b8 is not None:
            b14.config(b7 = f"NÃºmero encontrado en la posiciÃ³n: {b8}")
        else:
            b14.config(b7 = "NÃºmero no encontrado")
    except ValueError:
        b14.config(b7 = "Por favor, ingresa un nÃºmero vÃ¡lido")
def fonk4():
    b9 = tk.Tk()
    b9.title("BÃºsqueda Secuencial")
    b9.geometry('300x200')
    b9.configure(b10 = 'SkyBlue2')
    tk.Label(b9, b7 = "Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', b10='SkyBlue2').pack()
    global b11
    b11 = tk.Entry(b9, width=8)
    b11.pack()
    tk.Button(b9, b7 = "Buscar", command=buscar_numero).pack(b13=(10, 0))
    global b12
    b12 = tk.Label(b9, b7="", b10='SkyBlue2')
    b12.pack(b13 = (10, 0))
    global b14
    b14 = tk.Label(b9, b7="", b10='SkyBlue2')
    b14.pack(b13 = (10, 0))
    b9.mainloop()
if b15 = = "__main__":
    fonk4()