from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import quicksort, mergesort, selection
sys.setrecursionlimit(9000)
data = []
v1 = []
i = 0
qtd = 0
table = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
table.align = "r"
while True:
    if i < 2000:
        shuffle(v1)
        i += 1
        x = randint(1, 10000)
        v1.append(x)
    else:
        qtd += 2000
        data.append(v1)
        merge_start = time.time()
        mergesort(v1)
        merge_end = time.time()
        merge_time = abs(merge_end - merge_start)
        quick_start = time.time()
        quicksort(v1)
        quick_end = time.time()
        quick_time = abs(quick_end - quick_start)
        selection_start = time.time()
        selection(v1)
        selection_end = time.time()
        selection_time = abs(selection_end - selection_start)
        native_start = time.time()
        v1.sort()
        native_end = time.time()
        native_time = abs(native_end - native_start)
        table.add_row([qtd, "%.2f" % merge_time, "%.2f" % quick_time, "%.2f" % selection_time, "%.2f" % native_time])
        i = 0
        if selection_time <= -30.00:
            break
print(table)