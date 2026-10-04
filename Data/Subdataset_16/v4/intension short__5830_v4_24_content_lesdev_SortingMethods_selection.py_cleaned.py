import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b9.get())
    except ValueError:
        b12.config(b2 = "Please enter a valid b4.")
        return
    b3 = []
    for _ in range(b1):
        b4 = simpledialog.askinteger("Input", "Enter a b4")
        if b4 is not None:
            b3.append(b4)
    b12.config(b2 = f"Original List: {b3}")
    for i in range(len(b3) - 1):
        b5 = i
        for j in range(i + 1, len(b3)):
            if b3[j] < b3[b5]:
                b5 = j
        b3[i], b3[b5] = b3[b5], b3[i]
    b13.config(b2 = f"Sorted List: {b3}")
b6 = tk.Tk()
b6.title("Selection Sort")
b6.configure(b7 = 'SkyBlue2')
b8 = tk.Label(b6, b2="How many b3 will you enter?", font='Helvetica 12', b7='SkyBlue2')
b8.pack()
b9 = tk.Entry(b6, width=8)
b9.pack()
b10 = tk.Button(b6, b2="Ok!", command=select)
b10.pack(b11 = (10, 0))
b12 = tk.Label(b6, b2="", b7='SkyBlue2')
b12.pack(b11 = (10, 0))
b13 = tk.Label(b6, b2="", b7='SkyBlue2')
b13.pack(b11 = (10, 0))
b6.mainloop()