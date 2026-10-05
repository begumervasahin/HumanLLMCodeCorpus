import tkinter as tk
import tkinter.simpledialog as simpledialog
def perform_selection_sort():
    data_count = int(entry_num_data_points.get())
    vector = []
    for _ in range(data_count):
        number = simpledialog.askinteger("", "Ingrese el número")
        vector.append(number)
    original_list_str = str(vector)
    label_original_list.config(text=original_list_str)
    for i in range(len(vector)-1):
        min_index = i
        for j in range(i+1, len(vector)):
            if vector[j] < vector[min_index]:
                min_index = j
        vector[i], vector[min_index] = vector[min_index], vector[i]
    sorted_list_str = str(vector)
    label_sorted_list.config(text=sorted_list_str)
app = tk.Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
label_num_data_points = tk.Label(app, text="Cuantos numeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
label_num_data_points.pack()
num_data_points = tk.IntVar()
entry_num_data_points = tk.Entry(app, width=8, textvariable=num_data_points)
entry_num_data_points.pack()
button_sort = tk.Button(app, text="Ok!", command=perform_selection_sort)
button_sort.pack(pady=(10, 0))
label_original_list = tk.Label(app, text="", bg='SkyBlue2')
label_original_list.pack(pady=(10, 0))
label_sorted_list = tk.Label(app, text="", bg='SkyBlue2')
label_sorted_list.pack(pady=(10, 0))
app.mainloop()