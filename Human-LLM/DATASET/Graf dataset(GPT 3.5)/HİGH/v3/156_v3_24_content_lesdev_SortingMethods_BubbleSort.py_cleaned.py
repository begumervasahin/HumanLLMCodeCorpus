import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
def fonk1():
    b1 = int(b9.get())
    b2 = fonk2(b1)
    fonk3(b2)
    fonk4(b2)
    fonk5(b2)
def fonk2(b1):
    b3 = []
    for _ in range(b1):
        b4 = tkSimpleDialog.askinteger("", "Enter the b4")
        b3.append(b4)
    return b3
def fonk3(b2):
    b12.config(b5 = str(b2))
def fonk4(b2):
    for i in range(len(b2) - 1):
        for j in range(1, len(b2)):
            if b2[j] < b2[j - 1]:
                b2[j], b2[j - 1] = b2[j - 1], b2[j]
def fonk5(b2):
    b13.config(b5 = str(b2))
b6 = tk.Tk()
b6.title("Bubble Sort")
b6.geometry('250x250')
b6.configure(b7 = 'SkyBlue2')
b8 = tk.Label(b6, b5="How many b3 will you enter?", font="Helvetica 12", b7='SkyBlue2')
b8.pack()
b9 = tk.Entry(b6, width=8)
b9.pack()
b10 = tk.Button(b6, b5="OK!", command=bubble_sort)
b10.pack(b11 = (10, 0))
b12 = tk.Label(b6, b5="", b7='SkyBlue2')
b12.pack(b11 = (10, 0))
b13 = tk.Label(b6, b5="", b7='SkyBlue2')
b13.pack(b11 = (10, 0))
b6.mainloop()