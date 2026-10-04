import tkinter as tk
from tkinter import simpledialog
def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector)
        lefthalf = vector[:mid]
        righthalf = vector[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                vector[k] = lefthalf[i]
                i += 1
            else:
                vector[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            vector[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            vector[k] = righthalf[j]
            j += 1
            k += 1
def sorting():
    try:
        num_elements = int(entry_numeros.get())
    except ValueError:
        label2.config(text="Por favor, ingresa un nÃºmero vÃ¡lido.")
        return
    vector = []
    for _ in range(num_elements):
        number = simpledialog.askinteger("NÃºmero", "Ingresa un nÃºmero:")
        if number is not None:
            vector.append(number)
    label2.config(text=f"Original: {vector}")
    merge_sort(vector)
    label3.config(text=f"Ordenado: {vector}")
app = tk.Tk()
app.title("Merge Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label1 = tk.Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font="Helvetica 12", bg='SkyBlue2')
label1.pack(pady=(10, 5))
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack()
button1 = tk.Button(app, text="Ok!", command=sorting)
button1.pack(pady=(10, 5))
label2 = tk.Label(app, text="", bg='SkyBlue2')
label2.pack(pady=(10, 5))
label3 = tk.Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 5))
app.mainloop()