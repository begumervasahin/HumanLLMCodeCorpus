import sys
import tkinter as tk
import tkinter.simpledialog
def selection_sort():
    num_of_numbers = int(entry_numbers.get())
    numbers_list = []
    for i in range(num_of_numbers):
        number = tkinter.simpledialog.askinteger("", "Enter the number")
        numbers_list.append(number)
    unsorted_text = str(numbers_list)
    unsorted_label.config(text=unsorted_text)
    for i in range(len(numbers_list) - 1):
        min_index = i
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[j] < numbers_list[min_index]:
                min_index = j
        numbers_list[i], numbers_list[min_index] = numbers_list[min_index], numbers_list[i]
    sorted_text = str(numbers_list)
    sorted_label.config(text=sorted_text)
app = tk.Tk()
app.title("Selection Sort")
app.configure(bg='SkyBlue2')
label_num_of_numbers = tk.Label(app, text="How many numbers do you want to enter?", font='Helvetica 12', bg='SkyBlue2')
label_num_of_numbers.pack()
entry_numbers = tk.Entry(app, width=8)
entry_numbers.pack()
button_sort = tk.Button(app, text="Sort", command=selection_sort)
button_sort.pack(pady=(10, 0))
unsorted_label = tk.Label(app, text="", bg='SkyBlue2')
unsorted_label.pack(pady=(10, 0))
sorted_label = tk.Label(app, text="", bg='SkyBlue2')
sorted_label.pack(pady=(10, 0))
app.mainloop()