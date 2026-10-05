from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import mergesort, quicksort, selection
sys.setrecursionlimit(9000)
data = []
iterations = 0
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
        data.append(v1.copy())
        start = time.time()
        quicksort(v1.copy())
        end = time.time()
        quicksort_time = end - start
        start = time.time()
        mergesort(v1.copy())
        end = time.time()
        mergesort_time = end - start
        start = time.time()
        selection(v1.copy())
        end = time.time()
        selection_time = end - start
        start = time.time()
        v1.copy().sort()
        end = time.time()
        native_sort_time = end - start
        table.add_row([qtd, "%.2f" % abs(mergesort_time), "%.2f" % abs(quicksort_time), "%.2f" % abs(selection_time), "%.2f" % abs(native_sort_time)])
        i = 0
        x = selection_time <= -30.00
        print(len(v1))
        v1.clear()
print(table)