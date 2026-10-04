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
    return [random.randrange(0, a1) for _ in range(size)]
def fonk2(b8, b11, b2 = b1):
    b3 = []
    for func in b2:
        a3 = 0
        for _ in range(a2
            b4 = b8.copy() if not b11 else b8
            b5 = time.time()
            func(b4)
            a3 += (time.time() - b5)
        b6 = a3 / (a2
        b3.append(b6)
    b3.append(b3.index(min(b3)))
    return b3
def fonk3(start_size, end_size):
    b7 = []
    for size in range(start_size, end_size + 1, 100):
        print(f"Generating b9 for array size {size}")
        for b10 in range(3):
            b8 = fonk1(size)
            b9 = [size]
            if b10 = = 0:
                b11 = True
                b9.extend([1, 0, 0])
                b8.sort()
            else:
                b11 = False
                if b10 = = 1:
                    b9.extend([0, 1, 0])
                else:
                    b9.extend([0, 0, 1])
                    b8.sort(b12 = True)
            b9.extend(fonk2(b8, b11))
            b7.append(b9)
    return b7
def fonk4(filename, b9):
    with open(filename, "a", b13 = '') as file:
        b14 = csv.b14(file, dialect=csv.excel)
        b14.writerows(b9)
if b15 = = "__main__":
    random.seed(time.time())
    sys.setrecursionlimit(1000000)
    b7 = fonk3(1300, 4000)
    fonk4("b9.csv", b7)
    sys.setrecursionlimit(1000)