from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import quicksort, mergesort, selection
sys.setrecursionlimit(9000)
b1 = []
b2 = []
a1 = 0
a2 = 0
b3 = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
b3.b4 = "r"
while True:
    if a1 < 2000:
        shuffle(b2)
        a1 += 1
        b5 = randint(1, 10000)
        b2.append(b5)
    else:
        a2 += 2000
        b1.append(b2)
        b6 = time.time()
        mergesort(b2)
        b7 = time.time()
        b8 = abs(b7 - b6)
        b9 = time.time()
        quicksort(b2)
        b10 = time.time()
        b11 = abs(b10 - b9)
        b12 = time.time()
        selection(b2)
        b13 = time.time()
        b14 = abs(b13 - b12)
        b15 = time.time()
        b2.sort()
        b16 = time.time()
        b17 = abs(b16 - b15)
        b3.add_row([a2, "%.2f" % b8, "%.2f" % b11, "%.2f" % b14, "%.2f" % b17])
        a1 = 0
        if b14 <= -30.00:
            break
print(b3)