import tkinter as tk
import tkinter.simpledialog as simpledialog
def select():
    data_count = int(entrynumeros.get())
    vector = []
    for i in range(data_count):
        number = simpledialog.askinteger("", "Ingrese el número")
        vector.append(number)
    original_list_str = str(vector)
    Label2.config(text=original_list_str)
    for i in range(len(vector)-1):
        min_index = i
        for j in range(i+1, len(vector)):
            if vector[j] < vector[min_index]:
                min_index = j
        vector[i], vector[min_index] = vector[min_index], vector[i]
    sorted_list_str = str(vector)
    label3.config(text=sorted_list_str)
app = tk.Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
Label1 = tk.Label(app, text="Cuantos numeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack()
datos = tk.IntVar()
entrynumeros = tk.Entry(app, width=8, textvariable=datos)
entrynumeros.pack()
button1 = tk.Button(app, text="Ok!", command=select)
button1.pack(pady=(10, 0))
Label2 = tk.Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = tk.Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()