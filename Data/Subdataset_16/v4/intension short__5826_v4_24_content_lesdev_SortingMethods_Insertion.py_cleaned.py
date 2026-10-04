import tkinter as tk
from tkinter import simpledialog
def fonk1():
    b1 = int(b11.get())
    b2 = []
    for _ in range(b1):
        b3 = simpledialog.askinteger("Input", "Enter a number:")
        b2.append(b3)
    b13.config(b4 = f"Unsorted: {b2}")
    for i in range(1, len(b2)):
        b5 = b2[i]
        b6 = i - 1
        while b6 >= 0 and b5 < b2[b6]:
            b2[b6 + 1] = b2[b6]
            b6 -= 1
        b2[b6 + 1] = b5
    b14.config(b4 = f"Sorted: {b2}")
b7 = tk.Tk()
b7.title("Insertion Sort")
b7.geometry('300x200')
b7.configure(b8 = 'SkyBlue2')
b9 = tk.Label(b7, b4="How many b2 will you enter?", font="Helvetica 12", b8='SkyBlue2')
b9.pack(b10 = (10, 5))
b11 = tk.Entry(b7, width=10)
b11.pack(b10 = (5, 10))
b12 = tk.Button(b7, b4="Sort", command=insertion_sort)
b12.pack(b10 = (5, 10))
b13 = tk.Label(b7, b4="", b8='SkyBlue2')
b13.pack(b10 = (5, 10))
b14 = tk.Label(b7, b4="", b8='SkyBlue2')
b14.pack(b10 = (5, 10))
b7.mainloop()