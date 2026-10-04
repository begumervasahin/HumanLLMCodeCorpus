import tkinter as tk
from tkinter import simpledialog
def buscar_numero():
    try:
        cantidad_numeros = int(entry_cantidad.get())
        numeros = []
        numero_buscado = simpledialog.askinteger("Buscar NÃºmero", "Ingresa el nÃºmero que deseas buscar:")
        for i in range(cantidad_numeros):
            numero = simpledialog.askinteger("Ingresar NÃºmero", f"Ingrese el nÃºmero {i + 1}:")
            numeros.append(numero)
        lista_numeros = ', '.join(map(str, numeros))
        label_lista.config(text=f"NÃºmeros ingresados: {lista_numeros}")
        for index, num in enumerate(numeros):
            if num == numero_buscado:
                label_resultado.config(text=f"NÃºmero encontrado en la posiciÃ³n: {index}")
                return
        label_resultado.config(text="NÃºmero no encontrado")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un nÃºmero vÃ¡lido")
app = tk.Tk()
app.title("BÃºsqueda Secuencial")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_cantidad = tk.Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
label_cantidad.pack()
entry_cantidad = tk.Entry(app, width=8)
entry_cantidad.pack()
boton_buscar = tk.Button(app, text="Buscar", command=buscar_numero)
boton_buscar.pack(pady=(10, 0))
label_lista = tk.Label(app, text="", bg='SkyBlue2')
label_lista.pack(pady=(10, 0))
label_resultado = tk.Label(app, text="", bg='SkyBlue2')
label_resultado.pack(pady=(10, 0))
app.mainloop()