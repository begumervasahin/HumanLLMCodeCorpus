import sys
from tkinter import *
from tkinter import simpledialog
def get_numbers_from_user(num_count):
    numbers = []
    for _ in range(num_count):
        number = simpledialog.askinteger("Input", "Enter a number:")
        if number is not None:
            numbers.append(number)
    return numbers
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i]
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i]
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num
        counting_sort(arr, exp)
        exp *= 10
def sorting():
    try:
        num_count = int(entry_numbers.get())
        numbers = get_numbers_from_user(num_count)
        label_original.config(text=f"Original list: {numbers}")
        radix_sort(numbers)
        label_sorted.config(text=f"Sorted list: {numbers}")
    except ValueError:
        label_original.config(text="Invalid input! Please enter a valid number.")
app = Tk()
app.title("Radix Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
label_prompt.pack(pady=10)
entry_numbers = Entry(app, width=8)
entry_numbers.pack()
button_sort = Button(app, text="Sort", command=sorting)
button_sort.pack(pady=10)
label_original = Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=10)
label_sorted = Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=10)
app.mainloop()