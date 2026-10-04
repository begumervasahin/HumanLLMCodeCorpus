from random import randint
from time import time
def fonk1(b9, start, end):
    if start >= end:
        return
    b1 = fonk2(b9, start, end)
    fonk1(b9, start, b1)
    fonk1(b9, b1 + 1, end)
def fonk2(b9, start, end):
    b2 = b9[start]
    b3 = start - 1
    b4 = end + 1
    while True:
        b3 += 1
        while b9[b3] < b2:
            b3 += 1
        b4 -= 1
        while b9[b4] > b2:
            b4 -= 1
        if b3 >= b4:
            return b4
        b9[b3], b9[b4] = b9[b4], b9[b3]
def fonk3(b9, start, end):
    if start >= end:
        return
    b2 = b9[start]
    b5 = start
    b6 = end
    b3 = start
    while b3 <= b6:
        if b9[b3] < b2:
            b9[b5], b9[b3] = b9[b3], b9[b5]
            b5 += 1
            b3 += 1
        elif b9[b3] > b2:
            b9[b3], b9[b6] = b9[b6], b9[b3]
            b6 -= 1
        else:
            b3 += 1
    fonk3(b9, start, b5 - 1)
    fonk3(b9, b6 + 1, end)
def fonk4():
    print()
    b7 = int(input("Enter the list size: "))
    print()
    b8 = int(input("Enter the maximum element number (minimum is set at 1): "))
    print("(Hint, the lower the number, the higher number of duplicate elements with which to prove the algorithm's speed)")
    print()
    b9 = [randint(1, b8) for _ in range(b7)]
    b10 = b9[:]
    b11 = b9[:]
    b12 = time()
    fonk1(b10, 0, b7 - 1)
    b13 = time()
    print("The number of seconds for the 2-way sort was:  %.8f" % (b13 - b12))
    b14 = time()
    fonk3(b11, 0, b7 - 1)
    b15 = time()
    print("The number of seconds for the 3-way sort was:  %.8f" % (b15 - b14))
    print()
if b16 = = "__main__":
    fonk4()