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
continue_loop = True
qtd = 0
table = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
table.align = "lrrrr"
while continue_loop:
    if i < 2000:
        shuffle(v1)
        i += 1
        continue_loop = randint(1, 10000)
        v1.append(continue_loop)
    else:
        qtd += 2000
        data.append(v1.copy())
        quicksort_start = time.time()
        quicksort(v1.copy())
        quicksort_end = time.time()
        quicksort_time = quicksort_end - quicksort_start
        mergesort_start = time.time()
        mergesort(v1.copy())
        mergesort_end = time.time()
        mergesort_time = mergesort_end - mergesort_start
        selection_start = time.time()
        selection(v1.copy())
        selection_end = time.time()
        selection_time = selection_end - selection_start
        native_sort_start = time.time()
        v1.copy().sort()
        native_sort_end = time.time()
        native_sort_time = native_sort_end - native_sort_start
        table.add_row([qtd, "%.2f" % abs(mergesort_time), "%.2f" % abs(quicksort_time), "%.2f" % abs(selection_time), "%.2f" % abs(native_sort_time)])
        i = 0
        continue_loop = selection_time <= -30.00
        print(len(v1))
        v1.clear()
print(table)