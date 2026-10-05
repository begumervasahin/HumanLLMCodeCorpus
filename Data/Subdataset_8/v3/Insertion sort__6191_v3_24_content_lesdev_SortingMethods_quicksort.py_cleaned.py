import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def quick_sort(numbers):
    sort(numbers, 0, len(numbers) - 1)
def sort(numbers, start, end):
    if start < end:
        pivot = partition(numbers, start, end)
        sort(numbers, start, pivot - 1)
        sort(numbers, pivot + 1, end)
def partition(numbers, start, end):
    pivot_value = numbers[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and numbers[left] <= pivot_value:
            left += 1
        while numbers[right] >= pivot_value and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            numbers[left], numbers[right] = numbers[right], numbers[left]
    numbers[start], numbers[right] = numbers[right], numbers[start]
    return right
def setup_gui():
    app = Tk()
    app.title("Quick Sort")
    app.geometry('250x200')
    app.configure(bg='SkyBlue2')
    label_num = Label(app, text="Cuantos numeros vas a ingresar?", font='Helvetica 12', bg='SkyBlue2')
    label_num.pack()
    entry_num = Entry(app, width=8)
    entry_num.pack()
    button_sort = Button(app, text="Ok!", command=sorting)
    button_sort.pack(pady=(10, 0))
    label_unsorted = Label(app, text="", bg='SkyBlue2')
    label_unsorted.pack(pady=(10, 0))
    label_sorted = Label(app, text="", bg='SkyBlue2')
    label_sorted.pack(pady=(10, 0))
    app.mainloop()
def sorting():
    num_elements = int(entry_num.get())
    numbers = []
    for _ in range(num_elements):
        dialog = tkSimpleDialog.askinteger("", "Ingresa el numero")
        numbers.append(dialog)
    unsorted_str = str(numbers)
    label_unsorted.config(text=unsorted_str)
    quick_sort(numbers)
    sorted_str = str(numbers)
    label_sorted.config(text=sorted_str)
if __name__ == "__main__":
    setup_gui()