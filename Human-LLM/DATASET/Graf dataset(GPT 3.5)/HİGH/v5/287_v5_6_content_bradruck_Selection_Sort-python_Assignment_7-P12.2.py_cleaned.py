from random import randint
from time import time
from tkinter import *
def fonk1(b5):
    for i in range(len(b5)):
        b1 = fonk2(b5, i)
        b2 = b5[b1]
        b5[b1] = b5[i]
        b5[i] = b2
def fonk2(b5, start):
    b1 = start
    for i in range(start + 1, len(b5)):
        if b5[i] < b5[b1]:
            b1 = i
    return b1
def fonk3(b14, b15, b16):
    b3 = b14
    b4 = []
    for i in range(b16):
        b5 = [randint(1, 1000) for _ in range(b3)]
        b6 = time()
        fonk1(b5)
        b7 = time()
        b4.append([b3, round((b7 - b6), 3)])
        b3 = int(b3 + ((b15 - b14) / (b16 - 1))) - int(b3 + ((b15 - b14) / (b16 - 1))) % 5
    return b4
def fonk4(b4):
    b8 = Tk()
    b8.title("Results of Sample Runs - Selection Sort")
    b9 = Label(text='Sort Size')
    b10 = Label(text='Seconds to Sort')
    b9.grid(b11 = 0, column=1, sticky=NSEW)
    b10.grid(b11 = 0, column=2, sticky=NSEW)
    for i, (size, time_taken) in enumerate(b4):
        b12 = Label(text='%.0f' % size, relief=RIDGE, width=20, height=2)
        b13 = Label(text='%.3f' % time_taken, relief=RIDGE, width=20, height=2)
        b12.grid(b11 = i + 1, column=1, sticky=NSEW)
        b13.grid(b11 = i + 1, column=2, sticky=NSEW)
    b8.mainloop()
def fonk5():
    print()
    b14 = int(input("Enter the minimum list size: "))
    print()
    b15 = int(input("Enter the maximum list size: "))
    print()
    b16 = int(input("Enter the number of different measurements to run: "))
    b4 = fonk3(b14, b15, b16)
    fonk4(b4)
fonk5()