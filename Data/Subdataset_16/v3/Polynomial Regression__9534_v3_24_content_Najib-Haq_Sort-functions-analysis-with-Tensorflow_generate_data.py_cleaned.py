import random
import time
import csv
import sys
a1 = 10000000
a2 = 100000
def fonk1(b22):
    b1 = len(b22)
    for b8 in range(b1):
        for b4 in range(0, b1 - b8 - 1):
            if b22[b4] > b22[b4 + 1]:
                b22[b4], b22[b4 + 1] = b22[b4 + 1], b22[b4]
def fonk2(b22):
    b1 = len(b22)
    for b8 in range(b1):
        b2 = b8
        for b4 in range(b8 + 1, b1):
            if b22[b4] < b22[b2]:
                b2 = b4
        b22[b8], b22[b2] = b22[b2], b22[b8]
def fonk3(b22):
    for b8 in range(1, len(b22)):
        b3 = b22[b8]
        b4 = b8 - 1
        while b4 >= 0 and b3 < b22[b4]:
            b22[b4 + 1] = b22[b4]
            b4 -= 1
        b22[b4 + 1] = b3
def fonk4(b22):
    if len(b22) > 1:
        b5 = len(b22)
        b6 = b22[:b5]
        b7 = b22[b5:]
        fonk4(b6)
        fonk4(b7)
        b8 = b4 = k = 0
        while b8 < len(b6) and b4 < len(b7):
            if b6[b8] < b7[b4]:
                b22[k] = b6[b8]
                b8 += 1
            else:
                b22[k] = b7[b4]
                b4 += 1
            k += 1
        while b8 < len(b6):
            b22[k] = b6[b8]
            b8 += 1
            k += 1
        while b4 < len(b7):
            b22[k] = b7[b4]
            b4 += 1
            k += 1
def fonk5(b22):
    if len(b22) <= 1:
        return b22
    b9 = b22[len(b22)
    b10 = [x for x in b22 if x < b9]
    b11 = [x for x in b22 if x == b9]
    b12 = [x for x in b22 if x > b9]
    return fonk5(b10) + b11 + fonk5(b12)
def fonk6(b22):
    def fonk7(b22, b1, b8):
        b13 = b8
        b14 = 2 * b8 + 1
        b15 = 2 * b8 + 2
        if b14 < b1 and b22[b8] < b22[b14]:
            b13 = b14
        if b15 < b1 and b22[b13] < b22[b15]:
            b13 = b15
        if b13 != b8:
            b22[b8], b22[b13] = b22[b13], b22[b8]
            fonk7(b22, b1, b13)
    b1 = len(b22)
    for b8 in range(b1
        fonk7(b22, b1, b8)
    for b8 in range(b1 - 1, 0, -1):
        b22[b8], b22[0] = b22[0], b22[b8]
        fonk7(b22, b8, 0)
b16 = [bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort]
def fonk8(size):
    return [random.randrange(0, a1) for _ in range(size)]
def fonk9(b22, b25, b17 = b16):
    b18 = []
    for func in b17:
        a3 = 0
        for _ in range(a2
            b19 = b22.copy() if not b25 else b22
            b20 = time.time()
            func(b19)
            a3 += (time.time() - b20)
        b18.append(a3 / (a2
    b18.append(b18.index(min(b18)))
    return b18
def fonk10(a4, a5):
    b21 = []
    for size in range(a4, a5 + 1, 100):
        print(f"Generating b23 for array size {size}")
        for b24 in range(3):
            b22 = fonk8(size)
            b23 = [size]
            if b24 = = 0:
                b25 = True
                b23 += [1, 0, 0]
                b22.sort()
            elif b24 = = 1:
                b25 = False
                b23 += [0, 1, 0]
            else:
                b25 = False
                b23 += [0, 0, 1]
                b22.sort(b26 = True)
            b23 += fonk9(b22, b25)
            b21.append(b23)
    return b21
def fonk11(filename, b23):
    with open(filename, "a", b27 = '') as file:
        b28 = csv.b28(file, dialect=csv.excel)
        b28.writerows(b23)
if b29 = = "__main__":
    random.seed(time.time())
    sys.setrecursionlimit(1000000)
    a4 = 1300
    a5 = 4000
    b30 = "b23.csv"
    b21 = fonk10(a4, a5)
    fonk11(b30, b21)
    sys.setrecursionlimit(1000)