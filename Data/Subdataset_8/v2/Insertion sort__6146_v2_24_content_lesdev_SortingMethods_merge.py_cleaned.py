from tkinter import *
import tkinter.simpledialog as tkSimpleDialog
def merge_sort(vector):
    if len(vector) > 1:
        mid = len(vector)
        lefthalf = vector[:mid]
        righthalf = vector[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                vector[k] = lefthalf[i]
                i += 1
            else:
                vector[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            vector[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            vector[k] = righthalf[j]
            j += 1
            k += 1
def sorting():
    num_elements = int(entry_num_elements.get())
    vector = []
    for i in range(num_elements):
        num = tkSimpleDialog.askinteger("", "Ingresa el numero")
        vector.append(num)
    unsorted_list_str = str(vector)
    label_unsorted.config(text=unsorted_list_str)
    merge_sort(vector)
    sorted_list_str = str(vector)
    label_sorted.config(text=sorted_list_str)
app = Tk()
app.title("Merge Sort")
app.geometry('250x200')
app.configure(bg='SkyBlue2')
label_num_elements = Label(app, text="Cuantos numeros vas a ingresar?", font="Helvetica 12", bg='SkyBlue2')
label_num_elements.pack()
entry_num_elements = Entry(app, width=8)
entry_num_elements.pack()
button_sort = Button(app, text="Ok!", command=sorting)
button_sort.pack(pady=(10, 0))
label_unsorted = Label(app, text="", bg='SkyBlue2')
label_unsorted.pack(pady=(10, 0))
label_sorted = Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()