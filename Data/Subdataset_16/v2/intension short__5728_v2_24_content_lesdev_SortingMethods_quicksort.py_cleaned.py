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
        b5 = False
        while not b5:
            while b3 <= b4 and vector[b3] <= b2:
                b3 += 1
            while vector[b4] >= b2 and b4 >= b3:
                b4 -= 1
            if b4 < b3:
                b5 = True
            else:
                vector[b3], vector[b4] = vector[b4], vector[b3]
        vector[low], vector[b4] = vector[b4], vector[low]
        return b4
    fonk2(vector, 0, len(vector) - 1)
def fonk4():
    try:
        b6 = int(b13.get())
    except ValueError:
        b16.config(b7 = "Please enter a valid integer.")
        return
    b8 = []
    for i in range(b6):
        b9 = simpledialog.askinteger("Input", f"Enter b9 {i + 1}:")
        if b9 is not None:
            b8.append(b9)
        else:
            b16.config(b7 = "Operation canceled.")
            return
    b17.config(b7 = f"Unsorted: {b8}")
    fonk1(b8)
    b18.config(b7 = f"Sorted: {b8}")
b10 = tk.Tk()
b10.title("Quick Sort")
b10.geometry('300x200')
b10.configure(b11 = 'SkyBlue2')
b12 = tk.Label(b10, b7="How many b8 will you enter?", font='Helvetica 12', b11='SkyBlue2')
b12.pack()
b13 = tk.Entry(b10, width=10)
b13.pack(b14 = 5)
b15 = tk.Button(b10, b7="Sort", command=sorting)
b15.pack(b14 = 10)
b16 = tk.Label(b10, b7="", b11='SkyBlue2')
b16.pack()
b17 = tk.Label(b10, b7="", b11='SkyBlue2')
b17.pack(b14 = 5)
b18 = tk.Label(b10, b7="", b11='SkyBlue2')
b18.pack(b14 = 5)
b10.mainloop()