import tkinter as tk
from tkinter import simpledialog
def select():
    try:
        num_elements = int(entry_numbers.get())
    except ValueError:
        Label2.config(text="Please enter a valid number.")
        return
    numbers = []
    for _ in range(num_elements):
        number = simpledialog.askinteger("Input", "Enter a number")
        if number is not None:
            numbers.append(number)
    Label2.config(text=f"Original List: {numbers}")
    for i in range(len(numbers) - 1):
        min_index = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[min_index]:
                min_index = j
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
    label3.config(text=f"Sorted List: {numbers}")
app = tk.Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
Label1 = tk.Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack()
entry_numbers = tk.Entry(app, width=8)
entry_numbers.pack()
button1 = tk.Button(app, text="Ok!", command=select)
button1.pack(pady=(10, 0))
Label2 = tk.Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = tk.Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()