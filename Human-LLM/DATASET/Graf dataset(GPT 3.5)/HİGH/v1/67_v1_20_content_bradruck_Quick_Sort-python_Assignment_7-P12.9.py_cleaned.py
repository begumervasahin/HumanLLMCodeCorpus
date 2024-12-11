from random import randint
from time import time
def fonk1(values, start, to):
    if start >= to:
        return
    b1 = fonk2(values, start, to)
    fonk1(values, start, b1)
    fonk1(values, b1 + 1, to)
def fonk2(values, start, to):
    b2 = values[start]
    b3 = start - 1
    b4 = to + 1
    while b3 < b4:
        b3 += 1
        while values[b3] < b2:
            b3 += 1
        b4 -= 1
        while values[b4] > b2:
            b4 -= 1
        if b3 < b4:
            fonk4(values, b3, b4)
    return b4
def fonk3(values, start, to):
    if start >= to:
        return
    b2 = values[start]
    b5 = b3 = start
    b6 = to
    while b3 <= to:
        if values[b3] < b2:
            fonk4(values, b3, b5)
            b5 += 1
            b3 += 1
        elif values[b3] == b2:
            b3 += 1
        else:
            to -= 1
            fonk4(values, b3, b6)
    fonk3(values, start, b5)
    fonk3(values, b6, to)
def fonk4(values, b3, b4):
    b7 = values[b3]
    values[b3] = values[b4]
    values[b4] = b7
def fonk5():
    print()
    b8 = int(input("Enter the list size: "))
    print()
    print("Enter the maximum element number from which to build the list (the minimum is set at 1)")
    b9 = int(input("(Hint, the lower the number, the higher number of duplicate elements with which to prove the algorithm's speed): "))
    b10 = [randint(1, b9) for _ in range(b8)]
    b11 = b10.copy()
    b12 = time()
    fonk1(b10, 0, b8 - 1)
    b13 = time()
    print()
    print("The number of seconds for the 2-way sort was: %.8f" % (b13 - b12))
    b14 = time()
    fonk3(b11, 0, b8 - 1)
    b15 = time()
    print()
    print("The number of seconds for the 3-way sort was: %.8f" % (b15 - b14))
    print()
if b16 = = "__main__":
    fonk5()