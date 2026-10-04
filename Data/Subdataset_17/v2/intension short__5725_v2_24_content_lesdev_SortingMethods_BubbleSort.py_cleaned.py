import tkinter as tk
from tkinter import simpledialog
def bubble_sort():
    try:
        num_elements = int(entry_numeros.get())
        numbers = []
        for i in range(num_elements):
            number = simpledialog.askinteger("Input", f"Enter number {i+1}:")
            if number is not None:
                numbers.append(number)
            else:
                break
        unsorted_text = f"Unsorted: {numbers}"
        label_unsorted.config(text=unsorted_text)
        n = len(numbers)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        sorted_text = f"Sorted: {numbers}"
        label_sorted.config(text=sorted_text)
    except ValueError:
        label_unsorted.config(text="Invalid input. Please enter a valid number.")
        label_sorted.config(text="")
app = tk.Tk()
app.title("Bubble Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers do you want to enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack(pady=(10, 5))
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack()
button_ok = tk.Button(app, text="Ok!", command=bubble_sort)
button_ok.pack(pady=(10, 0))
label_unsorted = tk.Label(app, text="", bg='SkyBlue2')
label_unsorted.pack(pady=(10, 0))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()