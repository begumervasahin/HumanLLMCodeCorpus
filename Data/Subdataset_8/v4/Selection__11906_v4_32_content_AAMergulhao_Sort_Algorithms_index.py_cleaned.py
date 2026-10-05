from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import quicksort, mergesort, selection
sys.setrecursionlimit(9000)
data = []
v1 = []
i = 0
x = True
qtd = 0
table = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
table.align["Elements"] = "l"
table.align["Mergesort"] = "r"
table.align["Quicksort"] = "r"
table.align["Selection"] = "r"
table.align["Native"] = "r"
while x:
    if i < 2000:
        shuffle(v1)
        i += 1
        x = randint(1, 10000)
        v1.append(x)
    else:
        qtd += 2000
        data.append(v1)
        c = time.time()
        quicksort(v1)
        f = time.time()
        q = abs(f - c)
        c = time.time()
        mergesort(v1)
        f = time.time()
        m = abs(f - c)
        c = time.time()
        selection(v1)
        f = time.time()
        s = abs(f - c)
        c = time.time()
        v1.sort()
        f = time.time()
        n = abs(f - c)
        table.add_row([qtd, "%.2f" % m, "%.2f" % q, "%.2f" % s, "%.2f" % n])
        i = 0
        x = s <= -30.00
        print(len(v1))
print(table)