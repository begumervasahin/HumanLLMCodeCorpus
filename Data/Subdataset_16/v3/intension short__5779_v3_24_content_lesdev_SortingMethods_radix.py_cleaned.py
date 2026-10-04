import tkinter as tk
from tkinter import simpledialog
def fonk1(b7, a1):
    b1 = len(b7)
    b2 = [0] * b1
    b3 = [0] * 10
    for b8 in b7:
        b4 = (b8
        b3[b4] += 1
    for i in range(1, 10):
        b3[i] += b3[i - 1]
    for i in reversed(range(b1)):
        b4 = (b7[i]
        b2[b3[b4] - 1] = b7[i]
        b3[b4] -= 1
    for i in range(b1):
        b7[i] = b2[i]
def fonk2(b7):
    b5 = max(b7)
    a1 = 1
    while b5
        fonk1(b7, a1)
        a1 *= 10
def fonk3():
    b6 = int(b14.get())
    b7 = []
    for _ in range(b6):
        b8 = simpledialog.askinteger("Input", "Enter a b8:")
        if b8 is not None:
            b7.append(b8)
    return b7
def fonk4():
    b7 = fonk3()
    b16.config(b9 = f"Original List: {b7}")
    fonk2(b7)
    b17.config(b9 = f"Sorted List: {b7}")
b10 = tk.Tk()
b10.title("Radix Sort Application")
b10.geometry('300x200')
b10.configure(b11 = 'SkyBlue2')
b12 = tk.Label(b10, b9="How many b7 will you enter?", font='Helvetica 12', b11='SkyBlue2')
b12.pack(b13 = 10)
b14 = tk.Entry(b10, width=8)
b14.pack()
b15 = tk.Button(b10, b9="Sort", command=display_sorted_numbers)
b15.pack(b13 = 10)
b16 = tk.Label(b10, b9="", b11='SkyBlue2')
b16.pack(b13 = 5)
b17 = tk.Label(b10, b9="", b11='SkyBlue2')
b17.pack(b13 = 5)
b10.mainloop()