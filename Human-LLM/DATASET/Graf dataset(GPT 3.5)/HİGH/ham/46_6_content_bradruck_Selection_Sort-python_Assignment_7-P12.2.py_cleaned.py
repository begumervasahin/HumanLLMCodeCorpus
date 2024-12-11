from random import randint
from time import time
from tkinter import *
b1 = []
def fonk1(b8) :
    for i in range(len(b8)) :
        b2 = fonk2(b8, i)
        b3 = b8[b2]
        b8[b2] = b8[i]
        b8[i] = b3
def fonk2(b8, start) :
    b2 = start
    for i in range(start +1, len(b8)) :
        if b8[i] < b8[b2] :
            b2 = i
    return b2
def fonk3() :
    print()
    b4 = int(input("Enter the minimum list size: "))
    print()
    b5 = int(input("Enter the maximmum list size: "))
    print()
    b6 = int(input("Enter the number of different measurements to run: "))
    b7 = b4
    for i in range(b6) :
        b8 = []
        for x in range(b7):
            b8.append(randint(1, 1000))
        b9 = time()
        fonk1(b8)
        b10 = time()
        b1.append([b7, round((b10 - b9), 3)])
        b7 = int(b7 + ((b5 - b4) / (b6 - 1))) - int(b7 + ((b5 - b4) / (b6 - 1))) % 5
    b11 = Tk()
    b11.title("Results of Sample Runs - Selection Sort")
    b12 = Label(text='Sort Size')
    b13 = Label(text='Seconds to Sort')
    b12.grid(b14 = 0, column=1, sticky=NSEW)
    b13.grid(b14 = 0, column=2, sticky=NSEW)
    for i in range(b6):
        b15 = Label(text='%.0f' % b1[i][0], relief=RIDGE, width=20, height=2)
        b16 = Label(text='%.3f' % b1[i][1], relief=RIDGE, width=20, height=2)
        b15.grid(b14 = i+1, column=1, sticky=NSEW)
        b16.grid(b14 = i+1, column=2, sticky=NSEW)
    b11.mainloop()
fonk3()