import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def insertion_sort():
    num_elements = int(entry_num.get())
    vector = []
    for _ in range(num_elements):
        number = tkSimpleDialog.askinteger("", "Enter a number")
        vector.append(number)
    label_original.config(text=str(vector))
    for i in range(1, len(vector)):
        current_element = vector[i]
        j = i - 1
        while j >= 0 and current_element < vector[j]:
            vector[j + 1] = vector[j]
            j -= 1
        vector[j + 1] = current_element
    label_sorted.config(text=str(vector))
app = Tk()
app.title("Insertion Sort")
app.geometry('250x150')
app.configure(bg='SkyBlue2')
label_prompt = Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack()
entry_num = Entry(app, width=8)
entry_num.pack()
button_ok = Button(app, text="Ok!", command=insertion_sort)
button_ok.pack(pady=(10, 0))
label_original = Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10, 0))
label_sorted = Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()