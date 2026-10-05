import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def quick_sort(vector):
    sort(vector, 0, len(vector) - 1)
def sort(vector, start, end):
    if start < end:
        pivot = partition(vector, start, end)
        sort(vector, start, pivot - 1)
        sort(vector, pivot + 1, end)
def partition(vector, start, end):
    pivot_value = vector[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and vector[left] <= pivot_value:
            left += 1
        while vector[right] >= pivot_value and right >= left:
            right -= 1
        if right < left:
            done = True
        else:
            vector[left], vector[right] = vector[right], vector[left]
    vector[start], vector[right] = vector[right], vector[start]
    return right
def sorting():
    num_elements = int(entry_num.get())
    vector = []
    for _ in range(num_elements):
        dialog = tkSimpleDialog.askinteger("", "Ingresa el numero")
        vector.append(dialog)
    unsorted_str = str(vector)
    label_unsorted.config(text=unsorted_str)
    quick_sort(vector)
    sorted_str = str(vector)
    label_sorted.config(text=sorted_str)
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