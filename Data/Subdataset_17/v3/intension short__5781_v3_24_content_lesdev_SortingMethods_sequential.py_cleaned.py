import tkinter as tk
from tkinter import simpledialog
def obtener_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        numero = simpledialog.askinteger("Ingresar NÃºmero", f"Ingrese el nÃºmero {i + 1}:")
        if numero is not None:
            numeros.append(numero)
    return numeros
def buscar_en_lista(numeros, numero_buscado):
    for index, num in enumerate(numeros):
        if num == numero_buscado:
            return index
    return None
def buscar_numero():
    try:
        cantidad_numeros = int(entry_cantidad.get())
        numeros = obtener_numeros(cantidad_numeros)
        numero_buscado = simpledialog.askinteger("Buscar NÃºmero", "Ingresa el nÃºmero que deseas buscar:")
        lista_numeros = ', '.join(map(str, numeros))
        label_lista.config(text=f"NÃºmeros ingresados: {lista_numeros}")
        posicion = buscar_en_lista(numeros, numero_buscado)
        if posicion is not None:
            label_resultado.config(text=f"NÃºmero encontrado en la posiciÃ³n: {posicion}")
        else:
            label_resultado.config(text="NÃºmero no encontrado")
    except ValueError:
        label_resultado.config(text="Por favor, ingresa un nÃºmero vÃ¡lido")
def crear_interfaz():
    app = tk.Tk()
    app.title("BÃºsqueda Secuencial")
    app.geometry('300x200')
    app.configure(bg='SkyBlue2')
    tk.Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2').pack()
    global entry_cantidad
    entry_cantidad = tk.Entry(app, width=8)
    entry_cantidad.pack()
    tk.Button(app, text="Buscar", command=buscar_numero).pack(pady=(10, 0))
    global label_lista
    label_lista = tk.Label(app, text="", bg='SkyBlue2')
    label_lista.pack(pady=(10, 0))
    global label_resultado
    label_resultado = tk.Label(app, text="", bg='SkyBlue2')
    label_resultado.pack(pady=(10, 0))
    app.mainloop()
if __name__ == "__main__":
    crear_interfaz()