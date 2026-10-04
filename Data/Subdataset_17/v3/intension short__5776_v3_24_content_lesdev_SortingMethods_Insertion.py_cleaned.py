import tkinter as tk
from tkinter import simpledialog
def get_user_numbers(num_elements):
    numbers = []
    for _ in range(num_elements):
        number = simpledialog.askinteger("Input", "Enter a number:")
        if number is not None:
            numbers.append(number)
    return numbers
def display_numbers(label, numbers, prefix=""):
    label.config(text=f"{prefix}{numbers}")
def sort_numbers(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers
def insertion_sort():
    num_elements = int(entry_numbers.get())
    numbers = get_user_numbers(num_elements)
    display_numbers(label_original, numbers, "Original List: ")
    sorted_numbers = sort_numbers(numbers)
    display_numbers(label_sorted, sorted_numbers, "Sorted List: ")
def create_main_window():
    app = tk.Tk()
    app.title("Insertion Sort")
    app.geometry('300x200')
    app.configure(bg='SkyBlue2')
    return app
def create_label(app, text, font="Helvetica 12", pady=(10, 0)):
    label = tk.Label(app, text=text, font=font, bg='SkyBlue2')
    label.pack(pady=pady)
    return label
def create_entry(app, width=8, pady=(5, 0)):
    entry = tk.Entry(app, width=width)
    entry.pack(pady=pady)
    return entry
def create_button(app, text, command, pady=(10, 0)):
    button = tk.Button(app, text=text, command=command)
    button.pack(pady=pady)
    return button
app = create_main_window()
label_prompt = create_label(app, "How many numbers will you enter?")
entry_numbers = create_entry(app)
button_sort = create_button(app, "Sort", command=insertion_sort)
label_original = create_label(app, "")
label_sorted = create_label(app, "")
app.mainloop()