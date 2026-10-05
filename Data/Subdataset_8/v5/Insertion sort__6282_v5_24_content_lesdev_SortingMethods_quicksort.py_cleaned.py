import tkinter as tk
from tkinter import simpledialog
def quick_sort(arr):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    def _quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)
    _quick_sort(arr, 0, len(arr) - 1)
def sort_numbers():
    num_elements = int(entry_num.get())
    numbers = []
    for _ in range(num_elements):
        num = simpledialog.askinteger("", "Ingresa el numero")
        if num is not None:
            numbers.append(num)
    unsorted_str = str(numbers)
    label_unsorted.config(text=unsorted_str)
    quick_sort(numbers)
    sorted_str = str(numbers)
    label_sorted.config(text=sorted_str)
app = tk.Tk()
app.title("Quick Sort")
app.geometry('250x200')
app.configure(bg='SkyBlue2')
label_num = tk.Label(app, text="Cuantos numeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
label_num.pack()
entry_num = tk.Entry(app, width=8)
entry_num.pack()
button_sort = tk.Button(app, text="Ok!", command=sort_numbers)
button_sort.pack(pady=(10, 0))
label_unsorted = tk.Label(app, text="", bg='SkyBlue2')
label_unsorted.pack(pady=(10, 0))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()