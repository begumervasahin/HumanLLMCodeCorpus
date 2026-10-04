import tkinter as tk
from tkinter import simpledialog
def insertion_sort():
    num_elements = int(entry_numbers.get())
    numbers = []
    for _ in range(num_elements):
        number = simpledialog.askinteger("Input", "Enter a number:")
        if number is not None:
            numbers.append(number)
    label_original.config(text=f"Original List: {numbers}")
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    label_sorted.config(text=f"Sorted List: {numbers}")
app = tk.Tk()
app.title("Insertion Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack(pady=(10,0))
entry_numbers = tk.Entry(app, width=8)
entry_numbers.pack(pady=(5,0))
button_sort = tk.Button(app, text="Sort", command=insertion_sort)
button_sort.pack(pady=(10,0))
label_original = tk.Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10,0))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10,0))
app.mainloop()