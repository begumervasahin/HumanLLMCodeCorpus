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
def fonk4():
    print()
    b7 = int(input("Enter the size of the list: "))
    print()
    print("Enter the maximum value for list elements (minimum is set at 1)")
    b8 = int(input("(Hint: lower numbers result in more duplicate elements for testing algorithm speed): "))
    b9 = [randint(1, b8) for _ in range(b7)]
    b10 = b9.copy()
    b11 = time()
    fonk1(b9, 0, b7 - 1)
    b12 = time()
    print()
    print("Time taken for 2-way sort: %.8f seconds" % (b12 - b11))
    b13 = time()
    fonk3(b10, 0, b7 - 1)
    b14 = time()
    print()
    print("Time taken for 3-way sort: %.8f seconds" % (b14 - b13))
    print()
if b15 = = "__main__":
    fonk4()