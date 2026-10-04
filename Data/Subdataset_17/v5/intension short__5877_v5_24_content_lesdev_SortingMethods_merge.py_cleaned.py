import tkinter as tk
from tkinter import simpledialog
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
def sorting():
    try:
        num_elements = int(entry_numeros.get())
    except ValueError:
        label2.config(text="Por favor, ingresa un nÃºmero vÃ¡lido.")
        return
    numbers = []
    for _ in range(num_elements):
        number = simpledialog.askinteger("NÃºmero", "Ingresa un nÃºmero:")
        if number is not None:
            numbers.append(number)
    label2.config(text=f"Original: {numbers}")
    merge_sort(numbers)
    label3.config(text=f"Ordenado: {numbers}")
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