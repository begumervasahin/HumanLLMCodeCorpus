import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
def bubble_sort():
    num_elements = int(entry.get())
    vector = get_numbers_from_user(num_elements)
    display_original_vector(vector)
    bubble_sort_algorithm(vector)
    display_sorted_vector(vector)
def get_numbers_from_user(num_elements):
    numbers = []
    for _ in range(num_elements):
        number = tkSimpleDialog.askinteger("", "Enter the number")
        numbers.append(number)
    return numbers
def display_original_vector(vector):
    label_original.config(text=str(vector))
def bubble_sort_algorithm(vector):
    for i in range(len(vector) - 1):
        for j in range(1, len(vector)):
            if vector[j] < vector[j - 1]:
                vector[j], vector[j - 1] = vector[j - 1], vector[j]
def display_sorted_vector(vector):
    label_sorted.config(text=str(vector))
app = tk.Tk()
app.title("Bubble Sort")
app.geometry('250x250')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font="Helvetica 12", bg='SkyBlue2')
label_prompt.pack()
entry = tk.Entry(app, width=8)
entry.pack()
button_sort = tk.Button(app, text="OK!", command=bubble_sort)
button_sort.pack(pady=(10, 0))
label_original = tk.Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=(10, 0))
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=(10, 0))
app.mainloop()