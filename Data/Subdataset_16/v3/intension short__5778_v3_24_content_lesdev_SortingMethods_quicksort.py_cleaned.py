import tkinter as tk
from tkinter import simpledialog
def fonk1(vector):
    def fonk2(vector, low, high):
        if low < high:
            b1 = fonk3(vector, low, high)
            fonk2(vector, low, b1 - 1)
            fonk2(vector, b1 + 1, high)
    def fonk3(vector, low, high):
        b2 = vector[low]
        b3 = low + 1
        b4 = high
        while True:
            while b3 <= b4 and vector[b3] <= b2:
                b3 += 1
            while b4 >= b3 and vector[b4] >= b2:
                b4 -= 1
            if b4 < b3:
                break
            else:
                vector[b3], vector[b4] = vector[b4], vector[b3]
        vector[low], vector[b4] = vector[b4], vector[low]
        return b4
    fonk2(vector, 0, len(vector) - 1)
def fonk4():
    try:
        b5 = int(b12.get())
    except ValueError:
        b15.config(b6 = "Please enter a valid integer.")
        return
    b7 = []
    for i in range(b5):
        b8 = simpledialog.askinteger("Input", f"Enter b8 {i + 1}:")
        if b8 is not None:
            b7.append(b8)
        else:
            b15.config(b6 = "Operation canceled.")
            return
    b16.config(b6 = f"Unsorted: {b7}")
    fonk1(b7)
    b17.config(b6 = f"Sorted: {b7}")
b9 = tk.Tk()
b9.title("Quick Sort")
b9.geometry('300x200')
b9.configure(b10 = 'SkyBlue2')
b11 = tk.Label(b9, b6="How many b7 will you enter?", font='Helvetica 12', b10='SkyBlue2')
b11.pack()
b12 = tk.Entry(b9, width=10)
b12.pack(b13 = 5)
b14 = tk.Button(b9, b6="Sort", command=handle_sorting)
b14.pack(b13 = 10)
b15 = tk.Label(b9, b6="", b10='SkyBlue2')
b15.pack()
b16 = tk.Label(b9, b6="", b10='SkyBlue2')
b16.pack(b13 = 5)
b17 = tk.Label(b9, b6="", b10='SkyBlue2')
b17.pack(b13 = 5)
b9.mainloop()