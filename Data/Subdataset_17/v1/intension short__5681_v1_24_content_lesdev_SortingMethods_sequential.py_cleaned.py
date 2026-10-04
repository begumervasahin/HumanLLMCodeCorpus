import tkinter as tk
from tkinter import simpledialog
def busqueda():
    try:
        datos = int(entry_numeros.get())
        vector = []
        numerito = simpledialog.askinteger("Buscar NÃºmero", "Ingresa el nÃºmero a buscar:")
        for i in range(datos):
            numero = simpledialog.askinteger("Ingresar NÃºmero", f"Ingrese el nÃºmero {i + 1}:")
            vector.append(numero)
        aux_impresion1 = ', '.join(map(str, vector))
        label_resultado_lista.config(text=f"NÃºmeros ingresados: {aux_impresion1}")
        for i, num in enumerate(vector):
            if num == numerito:
                resultado_final = f"Encontrado en la posiciÃ³n: {i}"
                label_resultado_busqueda.config(text=resultado_final)
                return
        label_resultado_busqueda.config(text="NÃºmero no encontrado")
    except ValueError:
        label_resultado_busqueda.config(text="Por favor, ingresa un nÃºmero vÃ¡lido")
app = tk.Tk()
app.title("BÃºsqueda Secuencial")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_instruccion = tk.Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
label_instruccion.pack()
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack()
button_buscar = tk.Button(app, text="Ok!", command=busqueda)
button_buscar.pack(pady=(10, 0))
label_resultado_lista = tk.Label(app, text="", bg='SkyBlue2')
label_resultado_lista.pack(pady=(10, 0))
label_resultado_busqueda = tk.Label(app, text="", bg='SkyBlue2')
label_resultado_busqueda.pack(pady=(10, 0))
app.mainloop()