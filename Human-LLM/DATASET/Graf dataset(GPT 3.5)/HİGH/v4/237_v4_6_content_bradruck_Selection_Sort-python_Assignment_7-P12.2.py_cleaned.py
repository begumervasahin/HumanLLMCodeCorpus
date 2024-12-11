from random import randint
from time import time
from tkinter import *
def fonk1(b8):
    for i in range(len(b8)):
        b1 = fonk2(b8, i)
        b2 = b8[b1]
        b8[b1] = b8[i]
        b8[i] = b2
def fonk2(b8, start):
    b1 = start
    for i in range(start + 1, len(b8)):
        if b8[i] < b8[b1]:
            b1 = i
    return b1
def fonk3():
    print()
    b3 = int(input("Enter the minimum list size: "))
    print()
    b4 = int(input("Enter the maximum list size: "))
    print()
    b5 = int(input("Enter the number of different measurements to run: "))
    b6 = b3
    b7 = []
    for i in range(b5):
        b8 = [randint(1, 1000) for _ in range(b6)]
        b9 = time()
        fonk1(b8)
        b10 = time()
        b7.append([b6, round((b10 - b9), 3)])
        b6 = int(b6 + ((b4 - b3) / (b5 - 1))) - int(b6 + ((b4 - b3) / (b5 - 1))) % 5
    b11 = Tk()
    b11.title("Results of Sample Runs - Selection Sort")
    b12 = Label(text='Sort Size')
    b13 = Label(text='Seconds to Sort')
    b12.grid(b14 = 0, column=1, sticky=NSEW)
    b13.grid(b14 = 0, column=2, sticky=NSEW)
    for i in range(b5):
        b15 = Label(text='%.0f' % b7[i][0], relief=RIDGE, width=20, height=2)
        b16 = Label(text='%.3f' % b7[i][1], relief=RIDGE, width=20, height=2)
        b15.grid(b14 = i + 1, column=1, sticky=NSEW)
        b16.grid(b14 = i + 1, column=2, sticky=NSEW)
    b11.mainloop()
fonk3()