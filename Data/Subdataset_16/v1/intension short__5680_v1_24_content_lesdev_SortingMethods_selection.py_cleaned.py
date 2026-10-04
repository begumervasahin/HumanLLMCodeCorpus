import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b9.get())
        b2 = []
        for i in range(b1):
            b3 = simpledialog.askinteger("Input", "Ingresa el numero", parent=b6)
            if b3 is not None:
                b2.append(b3)
        b12.config(b4 = f"NÃºmeros ingresados: {b2}")
        for i in range(len(b2) - 1):
            b5 = i
            for j in range(i + 1, len(b2)):
                if b2[j] < b2[b5]:
                    b5 = j
            b2[i], b2[b5] = b2[b5], b2[i]
        b13.config(b4 = f"NÃºmeros ordenados: {b2}")
    except ValueError:
        b12.config(b4 = "Por favor ingresa un nÃºmero vÃ¡lido.")
b6 = tk.Tk()
b6.title("Selection Sort")
b6.configure(b7 = 'SkyBlue2')
b8 = tk.Label(b6, b4="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', b7='SkyBlue2')
b8.pack()
b9 = tk.Entry(b6, width=8)
b9.pack()
b10 = tk.Button(b6, b4="Ok!", command=select)
b10.pack(b11 = (10, 0))
b12 = tk.Label(b6, b4="", b7='SkyBlue2')
b12.pack(b11 = (10, 0))
b13 = tk.Label(b6, b4="", b7='SkyBlue2')
b13.pack(b11 = (10, 0))
b6.mainloop()