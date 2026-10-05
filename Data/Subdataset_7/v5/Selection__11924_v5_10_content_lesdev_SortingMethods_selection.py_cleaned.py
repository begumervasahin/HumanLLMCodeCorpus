import sys
import tkinter as tk
import tkinter.simpledialog
def fonk1():
    b1 = int(b11.get())
    b2 = []
    for i in range(b1):
        b3 = tkinter.simpledialog.askinteger("", "Enter the b3")
        b2.append(b3)
    b4 = str(b2)
    b14.config(b5 = b4)
    for i in range(len(b2) - 1):
        b6 = i
        for j in range(i + 1, len(b2)):
            if b2[j] < b2[b6]:
                b6 = j
        b2[i], b2[b6] = b2[b6], b2[i]
    b7 = str(b2)
    b15.config(b5 = b7)
b8 = tk.Tk()
b8.title("Selection Sort")
b8.configure(b9 = 'SkyBlue2')
b10 = tk.Label(b8, b5="How many numbers do you want to enter?", font='Helvetica 12', b9='SkyBlue2')
b10.pack()
b11 = tk.Entry(b8, width=8)
b11.pack()
b12 = tk.Button(b8, b5="Sort", command=selection_sort)
b12.pack(b13 = (10, 0))
b14 = tk.Label(b8, b5="", b9='SkyBlue2')
b14.pack(b13 = (10, 0))
b15 = tk.Label(b8, b5="", b9='SkyBlue2')
b15.pack(b13 = (10, 0))
b8.mainloop()