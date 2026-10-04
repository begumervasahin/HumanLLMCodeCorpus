import tkinter as tk
from tkinter import simpledialog
def radix_sort(vector):
    def counting_sort(vector, exp1):
        n = len(vector)
        output = [0] * n
        count = [0] * 10
        for i in range(n):
            index = (vector[i]
            count[(index % 10)] += 1
        for i in range(1, 10):
            count[i] += count[i - 1]
        i = n - 1
        while i >= 0:
            index = (vector[i]
            output[count[(index % 10)] - 1] = vector[i]
            count[(index % 10)] -= 1
            i -= 1
        for i in range(n):
            vector[i] = output[i]
    max1 = max(vector)
    exp = 1
    while max1
        counting_sort(vector, exp)
        exp *= 10
def sorting():
    num_elements = int(entry_num.get())
    vector = []
    for _ in range(num_elements):
        num = simpledialog.askinteger("Input", "Enter a number:")
        vector.append(num)
    label_original.config(text="Original List: " + str(vector))
    radix_sort(vector)
    label_sorted.config(text="Sorted List: " + str(vector))
app = tk.Tk()
app.title("Radix Sort")
app.geometry('300x200')
app.configure(bg='SkyBlue2')
label_prompt = tk.Label(app, text="How many numbers will you enter?", font='Helvetica 12', bg='SkyBlue2')
label_prompt.pack(pady=10)
entry_num = tk.Entry(app, width=8)
entry_num.pack()
button_sort = tk.Button(app, text="Sort", command=sorting)
button_sort.pack(pady=10)
label_original = tk.Label(app, text="", bg='SkyBlue2')
label_original.pack(pady=5)
label_sorted = tk.Label(app, text="", bg='SkyBlue2')
label_sorted.pack(pady=5)
app.mainloop()