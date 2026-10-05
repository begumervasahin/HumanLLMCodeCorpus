import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector)
        left_half = vector[:mid]
        right_half = vector[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                vector[k] = left_half[i]
                i += 1
            else:
                vector[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            vector[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            vector[k] = right_half[j]
            j += 1
            k += 1
def sorting():
    num_elements = int(entry_element_count.get())
    vector = []
    for i in range(num_elements):
        dialog = tkSimpleDialog.askinteger("", "Ingresa el numero")
        vector.append(dialog)
    unsorted_str = str(vector)
    label_unsorted.config(text=unsorted_str)
    merge_sort(vector)
    sorted_str = str(vector)
    label_sorted.config(text=sorted_str)
app = Tk()
app.title("Merge Sort")
app.geometry('250x200')
app.configure(bg='SkyBlue2')
label_element_count = Label(app, text="Cuantos numeros vas a ingresar?", font="Helvetica 12", bg='SkyBlue2')
label_element_count.pack()
entry_element_count = Entry(app, width=8)
entry_element_count.pack()
button_sort = Button(app, text="Ok!", command=sorting)
button_sort.pack(pady=(10, 0))
label_unsorted = Label(app, text="", bg='SkyBlue2')
label_unsorted.pack(pady=(10, 0))
label_sorted = Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()