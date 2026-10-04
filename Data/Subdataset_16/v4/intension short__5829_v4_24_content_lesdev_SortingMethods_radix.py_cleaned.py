import sys
from tkinter import *
from tkinter import simpledialog
def fonk1(b9):
    b1 = []
    for _ in range(b9):
        b2 = simpledialog.askinteger("Input", "Enter a b2:")
        if b2 is not None:
            b1.append(b2)
    return b1
def fonk2(arr, a1):
    b3 = len(arr)
    b4 = [0] * b3
    b5 = [0] * 10
    for b7 in range(b3):
        b6 = arr[b7]
        b5[b6 % 10] += 1
    for b7 in range(1, 10):
        b5[b7] += b5[b7 - 1]
    b7 = b3 - 1
    while b7 >= 0:
        b6 = arr[b7]
        b4[b5[b6 % 10] - 1] = arr[b7]
        b5[b6 % 10] -= 1
        b7 -= 1
    for b7 in range(b3):
        arr[b7] = b4[b7]
def fonk3(arr):
    b8 = max(arr)
    a1 = 1
    while b8
        fonk2(arr, a1)
        a1 *= 10
def fonk4():
    try:
        b9 = int(b15.get())
        b1 = fonk1(b9)
        b17.config(b10 = f"Original list: {b1}")
        fonk3(b1)
        b18.config(b10 = f"Sorted list: {b1}")
    except ValueError:
        b17.config(b10 = "Invalid input! Please enter a b2.")
b11 = Tk()
b11.title("Radix Sort")
b11.geometry('300x200')
b11.configure(b12 = 'SkyBlue2')
b13 = Label(b11, b10="How many b1 will you enter?", font='Helvetica 12', b12='SkyBlue2')
b13.pack(b14 = 10)
b15 = Entry(b11, width=8)
b15.pack()
b16 = Button(b11, b10="Sort", command=sorting)
b16.pack(b14 = 10)
b17 = Label(b11, b10="", b12='SkyBlue2')
b17.pack(b14 = 10)
b18 = Label(b11, b10="", b12='SkyBlue2')
b18.pack(b14 = 10)
b11.mainloop()