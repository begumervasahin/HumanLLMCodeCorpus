from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def radix_sort(vector):
    def counting_sort(vector, exp):
        n = len(vector)
        output = [0] * n
        count = [0] * 10
        for num in vector:
            index = (num
            count[index] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = (vector[i]
            output[count[index] - 1] = vector[i]
            count[index] -= 1
            i -= 1
        for i in range(n):
            vector[i] = output[i]
    def radix_sort_util(vector):
        max_num = max(vector)
        exp = 1
        while max_num
            counting_sort(vector, exp)
            exp *= 10
    radix_sort_util(vector)
def sorting():
    num_elements = int(entry_num.get())
    vector = [tkSimpleDialog.askinteger("", "Ingresa el numero") for _ in range(num_elements)]
    unsorted_str = str(vector)
    label_unsorted.config(text=unsorted_str)
    radix_sort(vector)
    sorted_str = str(vector)
    label_sorted.config(text=sorted_str)
app = Tk()
app.title("Radix Sort")
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