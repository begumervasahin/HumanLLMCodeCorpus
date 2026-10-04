import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b12.get())
        b2 = []
        for i in range(b1):
            b3 = simpledialog.askinteger("Input", f"Enter b3 {i+1}:")
            if b3 is not None:
                b2.append(b3)
            else:
                break
        b4 = f"Unsorted: {b2}"
        b14.config(b5 = b4)
        b6 = len(b2)
        for i in range(b6 - 1):
            for j in range(b6 - i - 1):
                if b2[j] > b2[j + 1]:
                    b2[j], b2[j + 1] = b2[j + 1], b2[j]
        b7 = f"Sorted: {b2}"
        b15.config(b5 = b7)
    except ValueError:
        b14.config(b5 = "Invalid input. Please enter a valid b3.")
        b15.config(b5 = "")
b8 = tk.Tk()
b8.title("Bubble Sort")
b8.geometry('300x200')
b8.configure(b9 = 'SkyBlue2')
b10 = tk.Label(b8, b5="How many b2 do you want to enter?", font="Helvetica 12", b9='SkyBlue2')
b10.pack(b11 = (10, 5))
b12 = tk.Entry(b8, width=8)
b12.pack()
b13 = tk.Button(b8, b5="Ok!", command=bubble_sort)
b13.pack(b11 = (10, 0))
b14 = tk.Label(b8, b5="", b9='SkyBlue2')
b14.pack(b11 = (10, 0))
b15 = tk.Label(b8, b5="", b9='SkyBlue2')
b15.pack(b11 = (10, 0))
b8.mainloop()