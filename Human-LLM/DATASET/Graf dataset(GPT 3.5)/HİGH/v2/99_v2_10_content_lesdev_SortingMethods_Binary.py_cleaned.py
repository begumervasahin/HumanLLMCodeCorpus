import tkinter as tk
import tkinter.simpledialog as tkSimpleDialog
def fonk1(nums, target):
    b3, b1 = 0, len(nums) - 1
    while b3 <= b1:
        b2 = (b3 + b1)
        if nums[b2] == target:
            return b2
        elif nums[b2] < target:
            b3 = b2 + 1
        else:
            b1 = b2 - 1
    return -1
def fonk2():
    b4 = int(b15.get())
    b5 = []
    b6 = tkSimpleDialog.askinteger("", "Enter the number to search for")
    for i in range(b4):
        b7 = tkSimpleDialog.askinteger("", "Enter the b5 in order")
        b5.append(b7)
    b8 = str(b5)
    b18.config(b9 = b8)
    b10 = fonk1(b5, b6)
    b11 = f"The number is at index: {b10}"
    b19.config(b9 = b11)
b12 = tk.Tk()
b12.title("Binary Search")
b12.geometry('250x200')
b12.configure(b13 = 'SkyBlue2')
b14 = tk.Label(b12, b9="How many b5 will you enter?", font='Helvetica 12', b13='SkyBlue2')
b14.pack()
b15 = tk.Entry(b12, width=8)
b15.pack()
b16 = tk.Button(b12, b9="Ok!", command=search)
b16.pack(b17 = (10, 0))
b18 = tk.Label(b12, b9="", b13='SkyBlue2')
b18.pack(b17 = (10, 0))
b19 = tk.Label(b12, b9="", b13='SkyBlue2')
b19.pack(b17 = (10, 0))
b12.mainloop()