import tkinter as tk
from tkinter import simpledialog
def select_numbers():
    try:
        num_elements = int(entry_numeros.get())
        numbers = []
        for _ in range(num_elements):
            num = simpledialog.askinteger("Input", "Ingresa el nÃºmero", parent=app)
            if num is not None:
                numbers.append(num)
        label_input_numbers.config(text=f"NÃºmeros ingresados: {numbers}")
        sorted_numbers = selection_sort(numbers)
        label_sorted_numbers.config(text=f"NÃºmeros ordenados: {sorted_numbers}")
    except ValueError:
        label_input_numbers.config(text="Por favor ingresa un nÃºmero vÃ¡lido.")
def selection_sort(numbers):
    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    return numbers
app = tk.Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
label_prompt.pack()
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack()
button_sort = tk.Button(app, text="Ok!", command=select_numbers)
button_sort.pack(pady=(10, 0))
label_input_numbers = tk.Label(app, text="", bg='SkyBlue2')
label_input_numbers.pack(pady=(10, 0))
label_sorted_numbers = tk.Label(app, text="", bg='SkyBlue2')
label_sorted_numbers.pack(pady=(10, 0))
app.mainloop()