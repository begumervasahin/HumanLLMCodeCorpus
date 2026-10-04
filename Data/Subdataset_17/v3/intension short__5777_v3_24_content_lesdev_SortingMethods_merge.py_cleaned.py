import tkinter as tk
from tkinter import simpledialog
def merge_sort(vector):
    if len(vector) <= 1:
        return vector
    mid = len(vector)
    left_half = merge_sort(vector[:mid])
    right_half = merge_sort(vector[mid:])
    return merge(left_half, right_half)
def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list
def sorting():
    try:
        num_count = int(entry_numeros.get())
        if num_count <= 0:
            raise ValueError
    except ValueError:
        label2.config(text="Please enter a valid positive number.")
        return
    vector = []
    for _ in range(num_count):
        num = simpledialog.askinteger("Input", "Enter a number:")
        if num is not None:
            vector.append(num)
    label2.config(text=f"Original list: {vector}")
    sorted_vector = merge_sort(vector)
    label3.config(text=f"Sorted list: {sorted_vector}")
def create_main_window():
    app = tk.Tk()
    app.title("Merge Sort")
    app.geometry('300x200')
    app.configure(bg='SkyBlue2')
    create_widgets(app)
    app.mainloop()
def create_widgets(app):
    label1 = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
    label1.pack(pady=(10, 5))
    global entry_numeros
    entry_numeros = tk.Entry(app, width=8)
    entry_numeros.pack(pady=(0, 10))
    button1 = tk.Button(app, text="Ok!", command=sorting)
    button1.pack(pady=(10, 0))
    global label2
    label2 = tk.Label(app, text="", bg='SkyBlue2')
    label2.pack(pady=(10, 0))
    global label3
    label3 = tk.Label(app, text="", bg='SkyBlue2')
    label3.pack(pady=(10, 0))
create_main_window()