import tkinter as tk
from tkinter import simpledialog
def counting_sort(numbers, exp):
    n = len(numbers)
    output = [0] * n
    count = [0] * 10
    for number in numbers:
        index = (number
        count[index] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in reversed(range(n)):
        index = (numbers[i]
        output[count[index] - 1] = numbers[i]
        count[index] -= 1
    for i in range(n):
        numbers[i] = output[i]
def radix_sort(numbers):
    max_number = max(numbers)
    exp = 1
    while max_number
        counting_sort(numbers, exp)
        exp *= 10
def get_numbers_from_user():
    num_elements = int(entry_num.get())
    numbers = []
    for _ in range(num_elements):
        number = simpledialog.askinteger("Input", "Enter a number:")
        if number is not None:
            numbers.append(number)
    return numbers
def display_sorted_numbers():
    numbers = get_numbers_from_user()
    label_original.config(text=f"Original List: {numbers}")
    radix_sort(numbers)
    label_sorted.config(text=f"Sorted List: {numbers}")
app = tk.Tk()
app.title("Radix Sort Application")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
label_prompt.pack(pady=10)
entry_num = tk.Entry(app, width=8)
entry_num.pack()
button_sort = tk.Button(app, text="Sort", command=display_sorted_numbers)
button_sort.pack(pady=10)
label_original = tk.Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=5)
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=5)
app.mainloop()