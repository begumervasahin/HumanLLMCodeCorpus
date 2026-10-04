import tkinter as tk
from tkinter import simpledialog
def fonk1(b8):
    if len(b8) <= 1:
        return b8
    b1 = len(b8)
    b2 = fonk1(b8[:b1])
    b3 = fonk1(b8[b1:])
    return fonk2(b2, b3)
def fonk2(left, right):
    b4 = []
    b5 = j = 0
    while b5 < len(left) and j < len(right):
        if left[b5] < right[j]:
            b4.append(left[b5])
            b5 += 1
        else:
            b4.append(right[j])
            j += 1
    b4.extend(left[b5:])
    b4.extend(right[j:])
    return b4
def fonk3():
    try:
        b6 = int(b15.get())
        if b6 <= 0:
            raise ValueError
    except ValueError:
        b17.config(b7 = "Please enter a valid positive number.")
        return
    b8 = []
    for _ in range(b6):
        b9 = simpledialog.askinteger("Input", "Enter a number:")
        if b9 is not None:
            b8.append(b9)
    b17.config(b7 = f"Original list: {b8}")
    b10 = fonk1(b8)
    b18.config(b7 = f"Sorted list: {b10}")
def fonk4():
    b11 = tk.Tk()
    b11.title("Merge Sort")
    b11.geometry('300x200')
    b11.configure(b12 = 'SkyBlue2')
    fonk5(b11)
    b11.mainloop()
def fonk5(b11):
    b13 = tk.Label(b11, b7="How many numbers will you enter?", font="Helvetica 12", b12='SkyBlue2')
    b13.pack(b14 = (10, 5))
    global b15
    b15 = tk.Entry(b11, width=8)
    b15.pack(b14 = (0, 10))
    b16 = tk.Button(b11, b7="Ok!", command=sorting)
    b16.pack(b14 = (10, 0))
    global b17
    b17 = tk.Label(b11, b7="", b12='SkyBlue2')
    b17.pack(b14 = (10, 0))
    global b18
    b18 = tk.Label(b11, b7="", b12='SkyBlue2')
    b18.pack(b14 = (10, 0))
fonk4()