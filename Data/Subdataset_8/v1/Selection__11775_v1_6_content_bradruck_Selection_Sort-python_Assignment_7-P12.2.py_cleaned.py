from random import randint
from time import time
from tkinter import *
tableArray = []
def selectionSort(values):
    for i in range(len(values)):
        minPos = minimumPosition(values, i)
        temp = values[minPos]
        values[minPos] = values[i]
        values[i] = temp
def minimumPosition(values, start):
    minPos = start
    for i in range(start + 1, len(values)):
        if values[i] < values[minPos]:
            minPos = i
    return minPos
def main():
    print()
    nmin = int(input("Enter the minimum list size: "))
    print()
    nmax = int(input("Enter the maximum list size: "))
    print()
    runs = int(input("Enter the number of different measurements to run: "))
    n = nmin
    for i in range(runs):
        values = []
        for x in range(n):
            values.append(randint(1, 1000))
        startTime = time()
        selectionSort(values)
        endTime = time()
        tableArray.append([n, round((endTime - startTime), 3)])
        n = int(n + ((nmax - nmin) / (runs - 1))) - int(n + ((nmax - nmin) / (runs - 1))) % 5
    window = Tk()
    window.title("Results of Sample Runs - Selection Sort")
    t1 = Label(text='Sort Size')
    t2 = Label(text='Seconds to Sort')
    t1.grid(row=0, column=1, sticky=NSEW)
    t2.grid(row=0, column=2, sticky=NSEW)
    for i in range(runs):
        l1 = Label(text='%.0f' % tableArray[i][0], relief=RIDGE, width=20, height=2)
        l2 = Label(text='%.3f' % tableArray[i][1], relief=RIDGE, width=20, height=2)
        l1.grid(row=i + 1, column=1, sticky=NSEW)
        l2.grid(row=i + 1, column=2, sticky=NSEW)
    window.mainloop()
if __name__ == "__main__":
    main()