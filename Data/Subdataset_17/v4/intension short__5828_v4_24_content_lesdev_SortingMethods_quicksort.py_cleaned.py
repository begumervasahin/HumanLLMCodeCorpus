import sys
from tkinter import *
import tkinter.simpledialog as simpledialog
def quicksort(vector):
    def sort(arr, low, high):
        if low < high:
            pivot_index = partition(arr, low, high)
            sort(arr, low, pivot_index - 1)
            sort(arr, pivot_index + 1, high)
    def partition(arr, low, high):
        pivot = arr[low]
        left = low + 1
        right = high
        done = False
        while not done:
            while left <= right and arr[left] <= pivot:
                left += 1
            while arr[right] >= pivot and right >= left:
                right -= 1
            if right < left:
                done = True
            else:
                arr[left], arr[right] = arr[right], arr[left]
        arr[low], arr[right] = arr[right], arr[low]
        return right
    sort(vector, 0, len(vector) - 1)
def sorting():
    try:
        num_count = int(entry_numeros.get())
    except ValueError:
        Label2.config(text="Please enter a valid number.")
        return
    vector = []
    for _ in range(num_count):
        num = simpledialog.askinteger("Input", "Enter a number:")
        if num is not None:
            vector.append(num)
    Label2.config(text=f"Original List: {vector}")
    quicksort(vector)
    label3.config(text=f"Sorted List: {vector}")
app = Tk()
app.title("Quick Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
Label1 = Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
Label1.pack(pady=(10, 0))
entry_numeros = Entry(app, width=8)
entry_numeros.pack(pady=(5, 0))
button1 = Button(app, text="Sort", command=sorting)
button1.pack(pady=(10, 0))
Label2 = Label(app, text="", bg='SkyBlue2')
Label2.pack(pady=(10, 0))
label3 = Label(app, text="", bg='SkyBlue2')
label3.pack(pady=(10, 0))
app.mainloop()