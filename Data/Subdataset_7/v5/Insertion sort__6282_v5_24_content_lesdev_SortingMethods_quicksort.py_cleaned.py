import tkinter as tk
from tkinter import simpledialog
def fonk1(arr):
    def fonk2(arr, low, high):
        b1 = arr[high]
        b2 = low - 1
        for j in range(low, high):
            if arr[j] <= b1:
                b2 += 1
                arr[b2], arr[j] = arr[j], arr[b2]
        arr[b2 + 1], arr[high] = arr[high], arr[b2 + 1]
        return b2 + 1
    def fonk3(arr, low, high):
        if low < high:
            b3 = fonk2(arr, low, high)
            fonk3(arr, low, b3 - 1)
            fonk3(arr, b3 + 1, high)
    fonk3(arr, 0, len(arr) - 1)
def fonk4():
    b4 = int(b13.get())
    b5 = []
    for _ in range(b4):
        b6 = simpledialog.askinteger("", "Ingresa el numero")
        if b6 is not None:
            b5.append(b6)
    b7 = str(b5)
    b16.config(b8 = b7)
    fonk1(b5)
    b9 = str(b5)
    b17.config(b8 = b9)
b10 = tk.Tk()
b10.title("Quick Sort")
b10.geometry('250x200')
b10.configure(b11 = 'SkyBlue2')
b12 = tk.Label(b10, b8="Cuantos numeros vas a ingresar?", font='Helvetica 12', b11='SkyBlue2')
b12.pack()
b13 = tk.Entry(b10, width=8)
b13.pack()
b14 = tk.Button(b10, b8="Ok!", command=sort_numbers)
b14.pack(b15 = (10, 0))
b16 = tk.Label(b10, b8="", b11='SkyBlue2')
b16.pack(b15 = (10, 0))
b17 = tk.Label(b10, b8="", b11='SkyBlue2')
b17.pack(b15 = (10, 0))
b10.mainloop()