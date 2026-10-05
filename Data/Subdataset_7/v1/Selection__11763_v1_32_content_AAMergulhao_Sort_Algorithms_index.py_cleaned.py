from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import mergesort, quicksort, selection
sys.setrecursionlimit(9000)
b1 = []
a1 = 0
b2 = []
a2 = 0
b3 = True
a3 = 0
b4 = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
b4.align["Elements"] = "l"
b4.align["Mergesort"] = "r"
b4.align["Quicksort"] = "r"
b4.align["Selection"] = "r"
b4.align["Native"] = "r"
while b3:
    if a2 < 2000:
        shuffle(b2)
        a2 += 1
        b3 = randint(1, 10000)
        b2.append(b3)
    else:
        a3 += 2000
        b1.append(b2.copy())
        b5 = time.time()
        quicksort(b2.copy())
        b6 = time.time()
        b7 = b6 - b5
        b5 = time.time()
        mergesort(b2.copy())
        b6 = time.time()
        b8 = b6 - b5
        b5 = time.time()
        selection(b2.copy())
        b6 = time.time()
        b9 = b6 - b5
        b5 = time.time()
        b2.copy().sort()
        b6 = time.time()
        b10 = b6 - b5
        b4.add_row([a3, "%.2f" % abs(b8), "%.2f" % abs(b7), "%.2f" % abs(b9), "%.2f" % abs(b10)])
        a2 = 0
        b3 = b9 <= -30.00
        print(len(b2))
        b2.clear()
print(b4)