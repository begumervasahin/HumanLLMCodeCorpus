import tkinter as tk
from tkinter import simpledialog
def quick_sort(vector):
    def sort(vector, low, high):
        if low < high:
            pivot_index = partition(vector, low, high)
            sort(vector, low, pivot_index - 1)
            sort(vector, pivot_index + 1, high)
    def partition(vector, low, high):
        pivot = vector[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and vector[left] <= pivot:
                left += 1
            while vector[right] >= pivot and right >= left:
                right -= 1
            if right < left:
                done = True
            else:
                vector[left], vector[right] = vector[right], vector[left]
        vector[low], vector[right] = vector[right], vector[low]
        return right
    sort(vector, 0, len(vector) - 1)
def sorting():
    try:
        num_elements = int(entry_numbers.get())
    except ValueError:
        label_info.config(text="Please enter a valid integer.")
        return
    numbers = []
    for i in range(num_elements):
        number = simpledialog.askinteger("Input", f"Enter number {i + 1}:")
        if number is not None:
            numbers.append(number)
        else:
            label_info.config(text="Operation canceled.")
            return
    label_unsorted.config(text=f"Unsorted: {numbers}")
    quick_sort(numbers)
    label_sorted.config(text=f"Sorted: {numbers}")
app = tk.Tk()
app.title("Quick Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
label_prompt.pack()
entry_numbers = tk.Entry(app, width=10)
entry_numbers.pack(pady=5)
button_sort = tk.Button(app, text="Sort", command=sorting)
button_sort.pack(pady=10)
label_info = tk.Label(app, text="", bg='SkyBlue2')
label_info.pack()
label_unsorted = tk.Label(app, text="", bg='SkyBlue2')
label_unsorted.pack(pady=5)
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=5)
app.mainloop()