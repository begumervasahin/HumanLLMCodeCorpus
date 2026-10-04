import sys
from tkinter import *
import tkinter.simpledialog as simpledialog
def fonk1(b8):
    def fonk2(arr, low, high):
        if low < high:
            b1 = fonk3(arr, low, high)
            fonk2(arr, low, b1 - 1)
            fonk2(arr, b1 + 1, high)
    def fonk3(arr, low, high):
        b2 = arr[low]
        b3 = low + 1
        b4 = high
        b5 = False
        while not b5:
            while b3 <= b4 and arr[b3] <= b2:
                b3 += 1
            while arr[b4] >= b2 and b4 >= b3:
                b4 -= 1
            if b4 < b3:
                b5 = True
            else:
                arr[b3], arr[b4] = arr[b4], arr[b3]
        arr[low], arr[b4] = arr[b4], arr[low]
        return b4
    fonk2(b8, 0, len(b8) - 1)
def fonk4():
    try:
        b6 = int(b14.get())
    except ValueError:
        b16.config(b7 = "Please enter a valid number.")
        return
    b8 = []
    for _ in range(b6):
        b9 = simpledialog.askinteger("Input", "Enter a number:")
        if b9 is not None:
            b8.append(b9)
    b16.config(b7 = f"Original List: {b8}")
    fonk1(b8)
    b17.config(b7 = f"Sorted List: {b8}")
b10 = Tk()
b10.title("Quick Sort")
b10.geometry('300x200')
b10.configure(b11 = 'SkyBlue2')
b12 = Label(b10, b7="How many numbers will you enter?", font='Helvetica 12', b11='SkyBlue2')
b12.pack(b13 = (10, 0))
b14 = Entry(b10, width=8)
b14.pack(b13 = (5, 0))
b15 = Button(b10, b7="Sort", command=sorting)
b15.pack(b13 = (10, 0))
b16 = Label(b10, b7="", b11='SkyBlue2')
b16.pack(b13 = (10, 0))
b17 = Label(b10, b7="", b11='SkyBlue2')
b17.pack(b13 = (10, 0))
b10.mainloop()