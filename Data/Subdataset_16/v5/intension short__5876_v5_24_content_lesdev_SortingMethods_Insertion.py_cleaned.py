import tkinter as tk
from tkinter import simpledialog
def fonk1(count):
    b1 = []
    for _ in range(count):
        b2 = simpledialog.askinteger("Input", "Enter a number:")
        if b2 is not None:
            b1.append(b2)
    return b1
def fonk2(b1):
    for i in range(1, len(b1)):
        b3 = b1[i]
        b4 = i - 1
        while b4 >= 0 and b3 < b1[b4]:
            b1[b4 + 1] = b1[b4]
            b4 -= 1
        b1[b4 + 1] = b3
    return b1
def fonk3():
    try:
        b5 = int(b12.get())
    except ValueError:
        b14.config(b6 = "Please enter a valid number.")
        return
    b1 = fonk1(b5)
    if b1:
        b14.config(b6 = f"Unsorted: {b1}")
        b7 = fonk2(b1)
        b15.config(b6 = f"Sorted: {b7}")
b8 = tk.Tk()
b8.title("Insertion Sort")
b8.geometry('300x200')
b8.configure(b9 = 'SkyBlue2')
b10 = tk.Label(b8, b6="How many b1 will you enter?", font="Helvetica 12", b9='SkyBlue2')
b10.pack(b11 = (10, 5))
b12 = tk.Entry(b8, width=10)
b12.pack(b11 = (5, 10))
b13 = tk.Button(b8, b6="Sort", command=on_sort_button_click)
b13.pack(b11 = (5, 10))
b14 = tk.Label(b8, b6="", b9='SkyBlue2')
b14.pack(b11 = (5, 10))
b15 = tk.Label(b8, b6="", b9='SkyBlue2')
b15.pack(b11 = (5, 10))
b8.mainloop()