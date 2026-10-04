import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b10.get())
    except ValueError:
        b13.config(b2 = "Please enter a valid b4.")
        return
    b3 = []
    for _ in range(b1):
        b4 = simpledialog.askinteger("Input", "Enter a b4")
        if b4 is not None:
            b3.append(b4)
    b13.config(b2 = f"Original List: {b3}")
    b5 = fonk2(b3)
    b14.config(b2 = f"Sorted List: {b5}")
def fonk2(b3):
    for i in range(len(b3) - 1):
        b6 = i
        for j in range(i + 1, len(b3)):
            if b3[j] < b3[b6]:
                b6 = j
        b3[i], b3[b6] = b3[b6], b3[i]
    return b3
b7 = tk.Tk()
b7.title("Selection Sort")
b7.configure(b8 = 'SkyBlue2')
b9 = tk.Label(b7, b2="How many b3 will you enter?", font='Helvetica 12', b8='SkyBlue2')
b9.pack()
b10 = tk.Entry(b7, width=8)
b10.pack()
b11 = tk.Button(b7, b2="Ok!", command=select)
b11.pack(b12 = (10, 0))
b13 = tk.Label(b7, b2="", b8='SkyBlue2')
b13.pack(b12 = (10, 0))
b14 = tk.Label(b7, b2="", b8='SkyBlue2')
b14.pack(b12 = (10, 0))
b7.mainloop()