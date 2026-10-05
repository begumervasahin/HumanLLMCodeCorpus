from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import mergesort, quicksort, selection
sys.setrecursionlimit(9000)
def fonk1():
    return [randint(1, 10000) for _ in range(2000)]
def fonk2(sort_func, b3):
    b1 = time.time()
    sort_func(b3.copy())
    b2 = time.time()
    return b2 - b1
b3 = []
a1 = 0
b4 = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
b4.b5 = "lrrrr"
while True:
    b6 = fonk1()
    a1 += 2000
    b3.append(b6.copy())
    b7 = fonk2(mergesort, b6)
    b8 = fonk2(quicksort, b6)
    b9 = fonk2(selection, b6)
    b10 = fonk2(sorted, b6)
    b4.add_row([a1, "%.2f" % abs(b7), "%.2f" % abs(b8), "%.2f" % abs(b9), "%.2f" % abs(b10)])
    if b9 <= -30.00:
        break
print(b4)