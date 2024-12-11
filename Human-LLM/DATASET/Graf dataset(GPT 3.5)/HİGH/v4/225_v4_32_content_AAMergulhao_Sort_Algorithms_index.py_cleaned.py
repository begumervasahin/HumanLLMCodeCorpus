from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import quicksort, mergesort, selection
sys.setrecursionlimit(9000)
b1 = []
b2 = []
a1 = 0
b3 = True
a2 = 0
b4 = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
b4.align["Elements"] = "l"
b4.align["Mergesort"] = "r"
b4.align["Quicksort"] = "r"
b4.align["Selection"] = "r"
b4.align["Native"] = "r"
while b3:
    if a1 < 2000:
        shuffle(b2)
        a1 += 1
        b3 = randint(1, 10000)
        b2.append(b3)
    else:
        a2 += 2000
        b1.append(b2)
        b5 = time.time()
        quicksort(b2)
        b6 = time.time()
        b7 = abs(b6 - b5)
        b5 = time.time()
        mergesort(b2)
        b6 = time.time()
        b8 = abs(b6 - b5)
        b5 = time.time()
        selection(b2)
        b6 = time.time()
        b9 = abs(b6 - b5)
        b5 = time.time()
        b2.sort()
        b6 = time.time()
        b10 = abs(b6 - b5)
        b4.add_row([a2, "%.2f" % b8, "%.2f" % b7, "%.2f" % b9, "%.2f" % b10])
        a1 = 0
        b3 = b9 <= -30.00
        print(len(b2))
print(b4)