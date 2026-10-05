from random import randint
from time import time
from tkinter import *
def fonk1(b4):
    for i in range(len(b4)):
        b1 = i
        for j in range(i + 1, len(b4)):
            if b4[j] < b4[b1]:
                b1 = j
        b4[i], b4[b1] = b4[b1], b4[i]
def fonk2(b10, b11, b12):
    b2 = []
    b3 = b10
    for _ in range(b12):
        b4 = [randint(1, 1000) for _ in range(b3)]
        b5 = time()
        fonk1(b4)
        b6 = time()
        b2.append([b3, round((b6 - b5), 3)])
        b3 += (b11 - b10)
        b3 -= b3 % 5
    return b2
def fonk3(b2):
    b7 = Tk()
    b7.title("Results of Sample Runs - Selection Sort")
    Label(b8 = 'Sort Size').grid(row=0, column=1, sticky=NSEW)
    Label(b8 = 'Seconds to Sort').grid(row=0, column=2, sticky=NSEW)
    for i, (size, time) in enumerate(b2, b9 = 1):
        Label(b8 = f'{size}', relief=RIDGE, width=20, height=2).grid(row=i, column=1, sticky=NSEW)
        Label(b8 = f'{time:.3f}', relief=RIDGE, width=20, height=2).grid(row=i, column=2, sticky=NSEW)
    b7.mainloop()
def fonk4():
    print()
    b10 = int(input("Enter the minimum list size: "))
    print()
    b11 = int(input("Enter the maximum list size: "))
    print()
    b12 = int(input("Enter the number of different b2 to run: "))
    b2 = fonk2(b10, b11, b12)
    fonk3(b2)
if b13 = = "__main__":
    fonk4()