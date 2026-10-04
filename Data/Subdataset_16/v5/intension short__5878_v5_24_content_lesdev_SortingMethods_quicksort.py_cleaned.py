import tkinter as tk
from tkinter import simpledialog
def fonk1(arr):
    def fonk2(arr, low, high):
        if low < high:
            b1 = fonk3(arr, low, high)
            fonk2(arr, low, b1 - 1)
            fonk2(arr, b1 + 1, high)
    def fonk3(arr, low, high):
        b2 = arr[low]
        b3 = low + 1
        b4 = high
        while True:
            while b3 <= b4 and arr[b3] <= b2:
                b3 += 1
            while b4 >= b3 and arr[b4] >= b2:
                b4 -= 1
            if b4 < b3:
                break
            arr[b3], arr[b4] = arr[b4], arr[b3]
        arr[low], arr[b4] = arr[b4], arr[low]
        return b4
    fonk2(arr, 0, len(arr) - 1)
def fonk4():
    try:
        b5 = int(b13.get())
    except ValueError:
        b15.config(b6 = "Please enter a valid b8.")
        return []
    b7 = []
    for _ in range(b5):
        b8 = simpledialog.askinteger("Input", "Enter a b8:")
        if b8 is not None:
            b7.append(b8)
    return b7
def fonk5():
    b7 = fonk4()
    if not b7:
        return
    b15.config(b6 = f"Original List: {b7}")
    fonk1(b7)
    b16.config(b6 = f"Sorted List: {b7}")
b9 = tk.Tk()
b9.title("Quick Sort")
b9.geometry('300x200')
b9.configure(b10 = 'SkyBlue2')
b11 = tk.Label(b9, b6="How many b7 will you enter?", font='Helvetica 12', b10='SkyBlue2')
b11.pack(b12 = (10, 0))
b13 = tk.Entry(b9, width=8)
b13.pack(b12 = (5, 0))
b14 = tk.Button(b9, b6="Sort", command=sorting)
b14.pack(b12 = (10, 0))
b15 = tk.Label(b9, b6="", b10='SkyBlue2')
b15.pack(b12 = (10, 0))
b16 = tk.Label(b9, b6="", b10='SkyBlue2')
b16.pack(b12 = (10, 0))
b9.mainloop()