import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b11.get())
        b2 = []
        for i in range(b1):
            b3 = simpledialog.askinteger("Input", f"Enter number {i+1}:")
            if b3 is not None:
                b2.append(b3)
            else:
                break
        b4 = f"Unsorted: {b2}"
        b13.config(b5 = b4)
        for i in range(len(b2)-1):
            for j in range(0, len(b2)-i-1):
                if b2[j] > b2[j+1]:
                    b2[j], b2[j+1] = b2[j+1], b2[j]
        b6 = f"Sorted: {b2}"
        b14.config(b5 = b6)
    except ValueError:
        b13.config(b5 = "Invalid input. Please enter a valid number.")
        b14.config(b5 = "")
b7 = tk.Tk()
b7.title("Bubble Sort")
b7.geometry('300x200')
b7.configure(b8 = 'SkyBlue2')
b9 = tk.Label(b7, b5="How many numbers do you want to enter?", font="Helvetica 12", b8='SkyBlue2')
b9.pack(b10 = (10, 5))
b11 = tk.Entry(b7, width=8)
b11.pack()
b12 = tk.Button(b7, b5="Ok!", command=bubble)
b12.pack(b10 = (10, 0))
b13 = tk.Label(b7, b5="", b8='SkyBlue2')
b13.pack(b10 = (10, 0))
b14 = tk.Label(b7, b5="", b8='SkyBlue2')
b14.pack(b10 = (10, 0))
b7.mainloop()