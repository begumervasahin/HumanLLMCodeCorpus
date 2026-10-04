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
        Label2.config(text=f"NÃºmeros ingresados: {numbers}")
        for i in range(len(numbers) - 1):
            min_index = i
            for j in range(i + 1, len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
        label3.config(text=f"NÃºmeros ordenados: {numbers}")
    except ValueError:
        Label2.config(text="Por favor ingresa un nÃºmero vÃ¡lido.")
app = tk.Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
Label1 = tk.Label(app, text="Â¿CuÃ¡ntos nÃºmeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack()
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack()
button1 = tk.Button(app, text="Ok!", command=select_numbers)
button1.pack(pady=(10, 0))
Label2 = tk.Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = tk.Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()