import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b10.get())
        b2 = []
        for _ in range(b1):
            b3 = simpledialog.askinteger("Input", "Ingresa el nÃºmero", parent=b7)
            if b3 is not None:
                b2.append(b3)
        b13.config(b4 = f"NÃºmeros ingresados: {b2}")
        b5 = fonk2(b2)
        b14.config(b4 = f"NÃºmeros ordenados: {b5}")
    except ValueError:
        b13.config(b4 = "Por favor ingresa un nÃºmero vÃ¡lido.")
def fonk2(b2):
    for i in range(len(b2) - 1):
        b6 = i
        for j in range(i + 1, len(b2)):
            if b2[j] < b2[b6]:
                b6 = j
        b2[i], b2[b6] = b2[b6], b2[i]
    return b2
b7 = tk.Tk()
b7.title("Selection Sort")
b7.configure(b8 = 'SkyBlue2')
b9 = tk.Label(b7, b4="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', b8='SkyBlue2')
b9.pack()
b10 = tk.Entry(b7, width=8)
b10.pack()
b11 = tk.Button(b7, b4="Ok!", command=select_numbers)
b11.pack(b12 = (10, 0))
b13 = tk.Label(b7, b4="", b8='SkyBlue2')
b13.pack(b12 = (10, 0))
b14 = tk.Label(b7, b4="", b8='SkyBlue2')
b14.pack(b12 = (10, 0))
b7.mainloop()