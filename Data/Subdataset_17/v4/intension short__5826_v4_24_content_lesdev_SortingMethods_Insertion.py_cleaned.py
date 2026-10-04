import tkinter as tk
from tkinter import simpledialog
def insertion_sort():
    num_count = int(entry_num.get())
    numbers = []
    for _ in range(num_count):
        num = simpledialog.askinteger("Input", "Enter a number:")
        numbers.append(num)
    Label_unsorted.config(text=f"Unsorted: {numbers}")
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    Label_sorted.config(text=f"Sorted: {numbers}")
app = tk.Tk()
app.title("Insertion Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
Label_prompt = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
Label_prompt.pack(pady=(10, 5))
entry_num = tk.Entry(app, width=10)
entry_num.pack(pady=(5, 10))
button_sort = tk.Button(app, text="Sort", command=insertion_sort)
button_sort.pack(pady=(5, 10))
Label_unsorted = tk.Label(app, text="", bg='SkyBlue2')
Label_unsorted.pack(pady=(5, 10))
Label_sorted = tk.Label(app, text="", bg='SkyBlue2')
Label_sorted.pack(pady=(5, 10))
app.mainloop()