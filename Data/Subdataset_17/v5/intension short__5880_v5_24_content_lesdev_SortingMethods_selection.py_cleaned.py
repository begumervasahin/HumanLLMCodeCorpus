import tkinter as tk
from tkinter import simpledialog
def select():
    try:
        num_elements = int(entry_numbers.get())
    except ValueError:
        label_original.config(text="Please enter a valid number.")
        return
    numbers = []
    for _ in range(num_elements):
        number = simpledialog.askinteger("Input", "Enter a number")
        if number is not None:
            numbers.append(number)
    label_original.config(text=f"Original List: {numbers}")
    sorted_numbers = selection_sort(numbers)
    label_sorted.config(text=f"Sorted List: {sorted_numbers}")
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
label_prompt = tk.Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
label_prompt.pack()
entry_numbers = tk.Entry(app, width=8)
entry_numbers.pack()
button_submit = tk.Button(app, text="Ok!", command=select)
button_submit.pack(pady=(10, 0))
label_original = tk.Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10, 0))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()