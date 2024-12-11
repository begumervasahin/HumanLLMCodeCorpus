from random import randint
from time import time
def fonk1(values, start, end):
    if start >= end:
        return
    b1 = fonk2(values, start, end)
    fonk1(values, start, b1)
    fonk1(values, b1 + 1, end)
def fonk2(values, start, end):
    b2 = values[start]
    b3 = start - 1
    b4 = end + 1
    while True:
        b3 += 1
        while values[b3] < b2:
            b3 += 1
        b4 -= 1
        while values[b4] > b2:
            b4 -= 1
        if b3 >= b4:
            return b4
        values[b3], values[b4] = values[b4], values[b3]
def fonk3(values, start, end):
    if start >= end:
        return
    b2 = values[start]
    b5 = i = start
    b6 = end
    while i <= b6:
        if values[i] < b2:
            values[i], values[b5] = values[b5], values[i]
            b5 += 1
            i += 1
        elif values[i] == b2:
            i += 1
        else:
            values[i], values[b6] = values[b6], values[i]
            b6 -= 1
    fonk3(values, start, b5)
    fonk3(values, b6 + 1, end)
def fonk4(b9, b10):
    return [randint(1, b10) for _ in range(b9)]
def fonk5(sort_func, values):
    b7 = time()
    sort_func(values, 0, len(values) - 1)
    b8 = time()
    return b8 - b7
def fonk6():
    print()
    b9 = int(input("Enter the list b9: "))
    print()
    b10 = int(input("Enter the maximum element number to build the list (minimum is 1): "))
    b11 = fonk4(b9, b10)
    b12 = b11.copy()
    b13 = fonk5(quick_sort_2_way, b11)
    b14 = fonk5(quick_sort_3_way, b12)
    print()
    print(f"The number of seconds for the 2-way sort was: {b13:.8f}")
    print(f"The number of seconds for the 3-way sort was: {b14:.8f}")
    print()
if b15 = = "__main__":
    fonk6()