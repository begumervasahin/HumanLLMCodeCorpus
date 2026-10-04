import tkinter as tk
from tkinter import simpledialog
def quicksort(arr):
    def sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            sort(arr, low, pivot_index - 1)
            sort(arr, pivot_index + 1, high)
    def partition(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high
        while True:
            while left <= right and arr[left] <= pivot:
                left += 1
            while right >= left and arr[right] >= pivot:
                right -= 1
            if right < left:
                break
            arr[left], arr[right] = arr[right], arr[left]
        arr[low], arr[right] = arr[right], arr[low]
        return right
    sort(arr, 0, len(arr) - 1)
def get_numbers():
    try:
        num_count = int(entry_numeros.get())
    except ValueError:
        label_original.config(text="Please enter a valid number.")
        return []
    numbers = []
    for _ in range(num_count):
        number = simpledialog.askinteger("Input", "Enter a number:")
        if number is not None:
            numbers.append(number)
    return numbers
def sorting():
    numbers = get_numbers()
    if not numbers:
        return
    label_original.config(text=f"Original List: {numbers}")
    quicksort(numbers)
    label_sorted.config(text=f"Sorted List: {numbers}")
app = tk.Tk()
app.title("Quick Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
label_prompt.pack(pady=(10, 0))
entry_numeros = tk.Entry(app, width=8)
entry_numeros.pack(pady=(5, 0))
button_sort = tk.Button(app, text="Sort", command=sorting)
button_sort.pack(pady=(10, 0))
label_original = tk.Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10, 0))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()