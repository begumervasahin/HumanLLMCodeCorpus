import tkinter as tk
from tkinter import simpledialog
def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector)
        left_half = vector[:mid]
        right_half = vector[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vector[k] = left_half[i]
                i += 1
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            vector[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            vector[k] = right_half[j]
            j += 1
            k += 1
def sorting():
    try:
        num_count = int(entry_numeros.get())
    except ValueError:
        label2.config(text="Please enter a valid number.")
        return
    vector = []
    for _ in range(num_count):
        num = simpledialog.askinteger("Input", "Enter a number:")
        if num is not None:
            vector.append(num)
    label2.config(text=f"Original list: {vector}")
    merge_sort(vector)
    label3.config(text=f"Sorted list: {vector}")
app = tk.Tk()
app.title("Merge Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label1 = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label1.pack(pady=(10, 5))
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack(pady=(0, 10))
button1 = tk.Button(app, text="Ok!", command=sorting)
button1.pack(pady=(10, 0))
label2 = tk.Label(app, text="", bg='SkyBlue2')
label2.pack(pady=(10, 0))
label3 = tk.Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()