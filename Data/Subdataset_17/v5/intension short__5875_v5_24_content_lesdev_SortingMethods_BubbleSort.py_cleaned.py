import tkinter as tk
from tkinter import simpledialog
def bubble_sort():
    try:
        num_elements = int(entry_num_elements.get())
        numbers = []
        for _ in range(num_elements):
            number = simpledialog.askinteger("Input", "Enter a number")
            if number is not None:
                numbers.append(number)
        label_original.config(text=f"Original: {numbers}")
        for i in range(len(numbers) - 1):
            for j in range(1, len(numbers)):
                if numbers[j] < numbers[j - 1]:
                    numbers[j], numbers[j - 1] = numbers[j - 1], numbers[j]
        label_sorted.config(text=f"Sorted: {numbers}")
    except ValueError:
        label_original.config(text="Please enter a valid integer.")
        label_sorted.config(text="")
def create_app():
    app = tk.Tk()
    app.title("Bubble Sort")
    app.geometry('300x200')
    app.configure(bg='SkyBlue2')
    label_prompt = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
    label_prompt.pack(pady=10)
    global entry_num_elements
    entry_num_elements = tk.Entry(app, width=8)
    entry_num_elements.pack()
    button_sort = tk.Button(app, text="Sort", command=bubble_sort)
    button_sort.pack(pady=10)
    global label_original, label_sorted
    label_original = tk.Label(app, text="", bg='SkyBlue2')
    label_original.pack(pady=10)
    label_sorted = tk.Label(app, text="", bg='SkyBlue2')
    label_sorted.pack(pady=10)
    return app
if __name__ == "__main__":
    app = create_app()
    app.mainloop()