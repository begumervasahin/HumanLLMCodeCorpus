import tkinter as tk
from tkinter import simpledialog
def select():
    try:
        datos = int(entry_numeros.get())
        vector = []
        for i in range(datos):
            num = simpledialog.askinteger("Input", "Ingresa el numero", parent=app)
            if num is not None:
                vector.append(num)
        Label2.config(text=f"NÃºmeros ingresados: {vector}")
        for i in range(len(vector) - 1):
            min_index = i
            for j in range(i + 1, len(vector)):
                if vector[j] < vector[min_index]:
                    min_index = j
            vector[i], vector[min_index] = vector[min_index], vector[i]
        label3.config(text=f"NÃºmeros ordenados: {vector}")
    except ValueError:
        Label2.config(text="Por favor ingresa un nÃºmero vÃ¡lido.")
app = tk.Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
Label1 = tk.Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack()
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack()
button1 = tk.Button(app, text="Ok!", command=select)
button1.pack(pady=(10, 0))
Label2 = tk.Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = tk.Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()