import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def perform_merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector)
        left_half = vector[:mid]
        right_half = vector[mid:]
        perform_merge_sort(left_half)
        perform_merge_sort(right_half)
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
def handle_sorting():
    num_elements = int(entry_num_elements.get())
    vector = []
    for i in range(num_elements):
        num = tkSimpleDialog.askinteger("", "Ingresa el numero")
        vector.append(num)
    unsorted_str = str(vector)
    label_unsorted.config(text=unsorted_str)
    perform_merge_sort(vector)
    sorted_str = str(vector)
    label_sorted.config(text=sorted_str)
app = Tk()
app.title("Merge Sort")
app.geometry('250x200')
app.configure(bg='SkyBlue2')
label_num_elements = Label(app, text="Cuantos numeros vas a ingresar?", font="Helvetica 12", bg='SkyBlue2')
label_num_elements.pack()
entry_num_elements = Entry(app, width=8)
entry_num_elements.pack()
button_sort = Button(app, text="Ok!", command=handle_sorting)
button_sort.pack(pady=(10, 0))
label_unsorted = Label(app, text="", bg='SkyBlue2')
label_unsorted.pack(pady=(10, 0))
label_sorted = Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()