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
b4.b5 = "lrrrr"
while b3:
    if a2 < 2000:
        shuffle(b2)
        a2 += 1
        b3 = randint(1, 10000)
        b2.append(b3)
    else:
        a3 += 2000
        b1.append(b2.copy())
        b6 = time.time()
        quicksort(b2.copy())
        b7 = time.time()
        b8 = b7 - b6
        b9 = time.time()
        mergesort(b2.copy())
        b10 = time.time()
        b11 = b10 - b9
        b12 = time.time()
        selection(b2.copy())
        b13 = time.time()
        b14 = b13 - b12
        b15 = time.time()
        b2.copy().sort()
        b16 = time.time()
        b17 = b16 - b15
        b4.add_row([a3, "%.2f" % abs(b11), "%.2f" % abs(b8), "%.2f" % abs(b14), "%.2f" % abs(b17)])
        a2 = 0
        b3 = b14 <= -30.00
        print(len(b2))
        b2.clear()
print(b4)