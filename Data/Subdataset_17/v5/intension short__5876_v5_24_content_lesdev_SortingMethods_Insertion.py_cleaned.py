import tkinter as tk
from tkinter import simpledialog
def get_numbers_from_user(count):
    numbers = []
    for _ in range(count):
        num = simpledialog.askinteger("Input", "Enter a number:")
        if num is not None:
            numbers.append(num)
    return numbers
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers
def on_sort_button_click():
    try:
        num_count = int(entry_num.get())
    except ValueError:
        label_unsorted.config(text="Please enter a valid number.")
        return
    numbers = get_numbers_from_user(num_count)
    if numbers:
        label_unsorted.config(text=f"Unsorted: {numbers}")
        sorted_numbers = insertion_sort(numbers)
        label_sorted.config(text=f"Sorted: {sorted_numbers}")
app = tk.Tk()
app.title("Insertion Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack(pady=(10, 5))
entry_num = tk.Entry(app, width=10)
entry_num.pack(pady=(5, 10))
button_sort = tk.Button(app, text="Sort", command=on_sort_button_click)
button_sort.pack(pady=(5, 10))
label_unsorted = tk.Label(app, text="", bg='SkyBlue2')
label_unsorted.pack(pady=(5, 10))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(5, 10))
app.mainloop()