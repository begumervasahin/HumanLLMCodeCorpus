import tkinter as tk
from tkinter import simpledialog
def fonk1():
    try:
        b1 = int(b9.get())
        b2 = []
        for _ in range(b1):
            b3 = simpledialog.askinteger("Input", "Enter a b3")
            if b3 is not None:
                b2.append(b3)
        b11.config(b4 = f"Original: {b2}")
        for i in range(len(b2) - 1):
            for j in range(1, len(b2)):
                if b2[j] < b2[j - 1]:
                    b2[j], b2[j - 1] = b2[j - 1], b2[j]
        b12.config(b4 = f"Sorted: {b2}")
    except ValueError:
        b11.config(b4 = "Please enter a valid integer.")
        b12.config(b4 = "")
def fonk2():
    b5 = tk.Tk()
    b5.title("Bubble Sort")
    b5.geometry('300x200')
    b5.configure(b6 = 'SkyBlue2')
    b7 = tk.Label(b5, b4="How many b2 will you enter?", font="Helvetica 12", b6='SkyBlue2')
    b7.pack(b8 = 10)
    global b9
    b9 = tk.Entry(b5, width=8)
    b9.pack()
    b10 = tk.Button(b5, b4="Sort", command=bubble_sort)
    b10.pack(b8 = 10)
    global b11, b12
    b11 = tk.Label(b5, b4="", b6='SkyBlue2')
    b11.pack(b8 = 10)
    b12 = tk.Label(b5, b4="", b6='SkyBlue2')
    b12.pack(b8 = 10)
    return b5
if b13 = = "__main__":
    b5 = fonk2()
    b5.mainloop()