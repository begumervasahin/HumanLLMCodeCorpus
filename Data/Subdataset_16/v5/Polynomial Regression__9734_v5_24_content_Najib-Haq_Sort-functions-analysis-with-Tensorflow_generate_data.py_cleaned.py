import sorting_algos as s
import random
import time
import csv
import sys
a1 = 10000000
a2 = 100000
b1 = [
    s.bubble_sort,
    s.selection_sort,
    s.insertion_sort,
    s.merge_sort,
    s.quick_sort,
    s.heap_sort
]
def fonk1(size):
    return [random.randint(0, a1) for _ in range(size)]
def fonk2(b8, is_sorted, b1 = b1):
    b2 = []
    for sort_func in b1:
        a3 = 0
        for _ in range(a2
            b3 = b8 if is_sorted else b8.copy()
            b4 = time.time()
            sort_func(b3)
            a3 += (time.time() - b4)
        b5 = a3 / (a2
        b2.append(b5)
    b6 = b2.index(min(b2))
    b2.append(b6)
    return b2
def fonk3(start_size, end_size):
    b7 = []
    for size in range(start_size, end_size + 1, 100):
        print(f"Generating b7 for b8 size {size}")
        for b10 in range(3):
            b8 = fonk1(size)
            b9 = [size]
            if b10 = = 0:
                b8.sort()
                b9.extend([1, 0, 0])
                b2 = fonk2(b8, True)
            elif b10 = = 1:
                b9.extend([0, 1, 0])
                b2 = fonk2(b8, False)
            else:
                b8.sort(b11 = True)
                b9.extend([0, 0, 1])
                b2 = fonk2(b8, False)
            b9.extend(b2)
            b7.append(b9)
    return b7
def fonk4(filename, b7):
    with open(filename, "a", b12 = '') as file:
        b13 = csv.b13(file)
        b13.writerows(b7)
if b14 = = "__main__":
    random.seed(time.time())
    sys.setrecursionlimit(1000000)
    b7 = fonk3(1300, 4000)
    fonk4("b7.csv", b7)
    sys.setrecursionlimit(1000)