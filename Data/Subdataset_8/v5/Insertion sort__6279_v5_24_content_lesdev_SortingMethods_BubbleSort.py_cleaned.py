import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
def bubble_sort():
    num_elements = int(entry_num.get())
    vector = []
    for _ in range(num_elements):
        number = tkSimpleDialog.askinteger("", "Enter a number")
        vector.append(number)
    label_original.config(text=str(vector))
    for i in range(len(vector) - 1):
        for j in range(1, len(vector)):
            if vector[j] < vector[j - 1]:
                vector[j], vector[j - 1] = vector[j - 1], vector[j]
    label_sorted.config(text=str(vector))
app = tk.Tk()
app.title("Bubble Sort")
app.geometry('250x150')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack()
entry_num = tk.Entry(app, width=8)
entry_num.pack()
button_ok = tk.Button(app, text="Ok!", command=bubble_sort)
button_ok.pack(pady=(10, 0))
label_original = tk.Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10, 0))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()