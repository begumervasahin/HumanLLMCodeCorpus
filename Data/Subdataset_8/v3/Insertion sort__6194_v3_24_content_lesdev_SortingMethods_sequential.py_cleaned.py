import sys
from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def search():
    num_elements = int(entry_num.get())
    vector = []
    number_to_find = tkSimpleDialog.askinteger("", "Enter the number to search for")
    for _ in range(num_elements):
        number = tkSimpleDialog.askinteger("", "Enter numbers in order")
        vector.append(number)
    label_original.config(text=str(vector))
    position = sequential_search(vector, number_to_find)
    if position is not None:
        label_result.config(text=f"Found at position: {position}")
    else:
        label_result.config(text="Number not found")
def sequential_search(vector, number_to_find):
    for i, num in enumerate(vector):
        if num == number_to_find:
            return i
    return None
app = Tk()
app.title("Sequential Search")
app.geometry('250x150')
app.configure(bg='SkyBlue2')
label_prompt = Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack()
entry_num = Entry(app, width=8)
entry_num.pack()
button_ok = Button(app, text="Ok!", command=search)
button_ok.pack(pady=(10, 0))
label_original = Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10, 0))
label_result = Label(app, text="", bg='SkyBlue2')
label_result.pack(pady=(10, 0))
app.mainloop()