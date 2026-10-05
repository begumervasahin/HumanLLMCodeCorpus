import sys
from tkinter import *
import tkSimpleDialog
def selection_sort():
    num_elements = int(entry_num.get())
    vector = []
    for _ in range(num_elements):
        number = tkSimpleDialog.askinteger("", "Enter a number")
        vector.append(number)
    label_original.config(text=str(vector))
    for i in range(len(vector) - 1):
        min_index = i
        for j in range(i + 1, len(vector)):
            if vector[j] < vector[min_index]:
                min_index = j
        vector[i], vector[min_index] = vector[min_index], vector[i]
    label_sorted.config(text=str(vector))
app = Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
label_prompt = Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack()
entry_num = Entry(app, width=8)
entry_num.pack()
button_ok = Button(app, text="Ok!", command=selection_sort)
button_ok.pack(pady=(10, 0))
label_original = Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10, 0))
label_sorted = Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()