import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b11.get())
        b2 = fonk2(b1)
        if not b2:
            b13.config(b3 = "No b2 entered.")
            return
        fonk4(b13, "Unsorted", b2)
        b4 = fonk3(b2)
        fonk4(b14, "Sorted", b4)
    except ValueError:
        b13.config(b3 = "Invalid input. Please enter a valid b5.")
        b14.config(b3 = "")
def fonk2(b1):
    b2 = []
    for i in range(b1):
        b5 = simpledialog.askinteger("Input", f"Enter b5 {i+1}:")
        if b5 is not None:
            b2.append(b5)
        else:
            break
    return b2
def fonk3(b2):
    b6 = len(b2)
    for i in range(b6 - 1):
        for j in range(b6 - i - 1):
            if b2[j] > b2[j + 1]:
                b2[j], b2[j + 1] = b2[j + 1], b2[j]
    return b2
def fonk4(label, title, lst):
    b3 = f"{title}: {lst}"
    label.config(b3 = b3)
b7 = tk.Tk()
b7.title("Bubble Sort")
b7.geometry('300x200')
b7.configure(b8 = 'SkyBlue2')
b9 = tk.Label(b7, b3="How many b2 do you want to enter?", font="Helvetica 12", b8='SkyBlue2')
b9.pack(b10 = (10, 5))
b11 = tk.Entry(b7, width=8)
b11.pack()
b12 = tk.Button(b7, b3="Ok!", command=bubble_sort)
b12.pack(b10 = (10, 0))
b13 = tk.Label(b7, b3="", b8='SkyBlue2')
b13.pack(b10 = (10, 0))
b14 = tk.Label(b7, b3="", b8='SkyBlue2')
b14.pack(b10 = (10, 0))
b7.mainloop()