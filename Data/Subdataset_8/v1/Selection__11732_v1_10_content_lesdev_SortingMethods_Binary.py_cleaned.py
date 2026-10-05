import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
def busqueda():
    datos = int(entrynumeros.get())
    vector = []
    numerito = tkSimpleDialog.askinteger("", "Ingresa el numero a buscar")
    for i in range(0, datos):
        dialog = tkSimpleDialog.askinteger("", "Ingresa los numeros en orden")
        vector.append(dialog)
    aux_impresion1 = str(vector)
    Label2.config(text=aux_impresion1)
    def busqueda_binaria(vector, numerito):
        izq = 0
        der = len(vector) - 1
        while izq <= der:
            medio = (izq + der)
            if vector[medio] == numerito:
                return medio
            elif vector[medio] > numerito:
                der = medio - 1
            else:
                izq = medio + 1
        return -1
    resultado = busqueda_binaria(vector, numerito)
    resultado_final = ("El numero esta en la posicion: %s" % resultado)
    label3.config(text=resultado_final)
app = tk.Tk()
app.title("Radix Sort")
app.geometry('250x150')
app.configure(bg='SkyBlue2')
Label1 = tk.Label(app, text="Cuantos numeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack()
datos = 0
entrynumeros = tk.Entry(app, width=8, textvariable=datos)
entrynumeros.pack()
button1 = tk.Button(app, text="Ok!", command=busqueda)
button1.pack(pady=(10, 0))
Label2 = tk.Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = tk.Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()