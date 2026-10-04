import tkinter as tk
from tkinter import simpledialog
def fonk1(b7):
    if len(b7) > 1:
        b1 = len(b7)
        b2 = b7[:b1]
        b3 = b7[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            if b2[b4] < b3[j]:
                b7[k] = b2[b4]
                b4 += 1
            else:
                b7[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            b7[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            b7[k] = b3[j]
            j += 1
            k += 1
def fonk2():
    try:
        b5 = int(b13.get())
    except ValueError:
        b15.config(b6 = "Please enter a valid number.")
        return
    b7 = []
    for _ in range(b5):
        b8 = simpledialog.askinteger("Input", "Enter a number:")
        if b8 is not None:
            b7.append(b8)
    b15.config(b6 = f"Original list: {b7}")
    fonk1(b7)
    b16.config(b6 = f"Sorted list: {b7}")
b9 = tk.Tk()
b9.title("Merge Sort")
b9.geometry('300x200')
b9.configure(b10 = 'SkyBlue2')
b11 = tk.Label(b9, b6="How many numbers will you enter?", font="Helvetica 12", b10='SkyBlue2')
b11.pack(b12 = (10, 5))
b13 = tk.Entry(b9, width=8)
b13.pack(b12 = (0, 10))
b14 = tk.Button(b9, b6="Ok!", command=sorting)
b14.pack(b12 = (10, 0))
b15 = tk.Label(b9, b6="", b10='SkyBlue2')
b15.pack(b12 = (10, 0))
b16 = tk.Label(b9, b6="", b10='SkyBlue2')
b16.pack(b12 = (10, 0))
b9.mainloop()