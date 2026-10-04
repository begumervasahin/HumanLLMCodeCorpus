import tkinter as tk
from tkinter import simpledialog
def fonk1(b7):
    b1 = []
    for _ in range(b7):
        b2 = simpledialog.askinteger("Input", "Enter a b2:")
        if b2 is not None:
            b1.append(b2)
    return b1
def fonk2(b12, b1, b3 = ""):
    b12.config(b4 = f"{b3}{b1}")
def fonk3(b1):
    for i in range(1, len(b1)):
        b5 = b1[i]
        b6 = i - 1
        while b6 >= 0 and b1[b6] > b5:
            b1[b6 + 1] = b1[b6]
            b6 -= 1
        b1[b6 + 1] = b5
    return b1
def fonk4():
    b7 = int(b18.get())
    b1 = fonk1(b7)
    fonk2(b20, b1, "Original List: ")
    b8 = fonk3(b1)
    fonk2(b21, b8, "Sorted List: ")
def fonk5():
    b9 = tk.Tk()
    b9.title("Insertion Sort")
    b9.geometry('300x200')
    b9.configure(b10 = 'SkyBlue2')
    return b9
def fonk6(b9, b4, b11 = "Helvetica 12", b13=(10, 0)):
    b12 = tk.Label(b9, b4=b4, b11=b11, b10='SkyBlue2')
    b12.pack(b13 = b13)
    return b12
def fonk7(b9, b14 = 8, b13=(5, 0)):
    b15 = tk.Entry(b9, b14=b14)
    b15.pack(b13 = b13)
    return b15
def fonk8(b9, b4, command, b13 = (10, 0)):
    b16 = tk.Button(b9, b4=b4, command=command)
    b16.pack(b13 = b13)
    return b16
b9 = fonk5()
b17 = fonk6(b9, "How many b1 will you enter?")
b18 = fonk7(b9)
b19 = fonk8(b9, "Sort", command=insertion_sort)
b20 = fonk6(b9, "")
b21 = fonk6(b9, "")
b9.mainloop()