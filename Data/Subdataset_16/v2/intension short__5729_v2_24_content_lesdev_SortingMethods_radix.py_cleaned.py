import tkinter as tk
from tkinter import simpledialog
def fonk1(b8):
    def fonk2(b8, a1):
        b1 = len(b8)
        b2 = [0] * b1
        b3 = [0] * 10
        for b9 in b8:
            b4 = b9
            b3[b4 % 10] += 1
        for b5 in range(1, 10):
            b3[b5] += b3[b5 - 1]
        b5 = b1 - 1
        while b5 >= 0:
            b4 = b8[b5]
            b2[b3[b4 % 10] - 1] = b8[b5]
            b3[b4 % 10] -= 1
            b5 -= 1
        for b5 in range(b1):
            b8[b5] = b2[b5]
    b6 = max(b8)
    a1 = 1
    while b6
        fonk2(b8, a1)
        a1 *= 10
def fonk3():
    b7 = int(b15.get())
    b8 = []
    for _ in range(b7):
        b9 = simpledialog.askinteger("Input", "Enter a b9:")
        b8.append(b9)
    b17.config(b10 = "Original List: " + str(b8))
    fonk1(b8)
    b18.config(b10 = "Sorted List: " + str(b8))
b11 = tk.Tk()
b11.title("Radix Sort Application")
b11.geometry('300x200')
b11.configure(b12 = 'SkyBlue2')
b13 = tk.Label(b11, b10="How many b8 will you enter?", font='Helvetica 12', b12='SkyBlue2')
b13.pack(b14 = 10)
b15 = tk.Entry(b11, width=8)
b15.pack()
b16 = tk.Button(b11, b10="Sort", command=get_numbers_and_sort)
b16.pack(b14 = 10)
b17 = tk.Label(b11, b10="", b12='SkyBlue2')
b17.pack(b14 = 5)
b18 = tk.Label(b11, b10="", b12='SkyBlue2')
b18.pack(b14 = 5)
b11.mainloop()