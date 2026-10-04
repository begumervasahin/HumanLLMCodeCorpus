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
    while True:
        b3 += 1
        while values[b3] < b2:
            b3 += 1
        b4 -= 1
        while values[b4] > b2:
            b4 -= 1
        if b3 >= b4:
            return b4
        fonk4(values, b3, b4)
def fonk3(values, start, to):
    if start >= to:
        return
    b2 = values[start]
    b5 = b3 = start
    b6 = to
    while b3 <= b6:
        if values[b3] < b2:
            fonk4(values, b3, b5)
            b5 += 1
            b3 += 1
        elif values[b3] == b2:
            b3 += 1
        else:
            fonk4(values, b3, b6)
            b6 -= 1
    fonk3(values, start, b5 - 1)
    fonk3(values, b6 + 1, to)
def fonk4(values, b3, b4):
    values[b3], values[b4] = values[b4], values[b3]
def fonk5():
    print()
    b7 = int(input("Enter the list size: "))
    print()
    print("Enter the maximum element number from which to build the list (the minimum is set at 1)")
    b8 = int(input("(Hint, the lower the number, the higher number of duplicate elements with which to prove the algorithm's speed): "))
    b9 = [randint(1, b8) for _ in range(b7)]
    b10 = b9[:]
    b11 = time()
    fonk1(b9, 0, b7 - 1)
    b12 = time()
    print()
    print("The number of seconds for the 2-way sort was:  %.8f" % (b12 - b11))
    b13 = time()
    fonk3(b10, 0, b7 - 1)
    b14 = time()
    print()
    print("The number of seconds for the 3-way sort was:  %.8f" % (b14 - b13))
    print()
if b15 = = "__main__":
    fonk5()