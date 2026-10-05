from random import randint, shuffle
import time
from prettytable import PrettyTable
import sys
from algorithms import mergesort, quicksort, selection
sys.setrecursionlimit(9000)
def generate_random_list():
    return [randint(1, 10000) for _ in range(2000)]
def measure_sorting_time(sort_func, data):
    start_time = time.time()
    sort_func(data.copy())
    end_time = time.time()
    return end_time - start_time
data = []
qtd = 0
table = PrettyTable(["Elements", "Mergesort", "Quicksort", "Selection", "Native"])
table.align = "lrrrr"
while True:
    v1 = generate_random_list()
    qtd += 2000
    data.append(v1.copy())
    mergesort_time = measure_sorting_time(mergesort, v1)
    quicksort_time = measure_sorting_time(quicksort, v1)
    selection_time = measure_sorting_time(selection, v1)
    native_sort_time = measure_sorting_time(sorted, v1)
    table.add_row([qtd, "%.2f" % abs(mergesort_time), "%.2f" % abs(quicksort_time), "%.2f" % abs(selection_time), "%.2f" % abs(native_sort_time)])
    if selection_time <= -30.00:
        break
print(table)