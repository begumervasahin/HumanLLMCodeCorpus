from random import randint
from time import time
def fonk1(b10, start, end):
    if start < end:
        b1 = fonk2(b10, start, end)
        fonk1(b10, start, b1)
        fonk1(b10, b1 + 1, end)
def fonk2(b10, start, end):
    b2 = b10[start]
    b3 = start - 1
    b4 = end + 1
    while True:
        b3 += 1
        while b10[b3] < b2:
            b3 += 1
        b4 -= 1
        while b10[b4] > b2:
            b4 -= 1
        if b3 >= b4:
            return b4
        b10[b3], b10[b4] = b10[b4], b10[b3]
def fonk3(b10, start, end):
    if start < end:
        b6, b5 = fonk4(b10, start, end)
        fonk3(b10, start, b6 - 1)
        fonk3(b10, b5 + 1, end)
def fonk4(b10, start, end):
    b2 = b10[start]
    b6 = start
    b5 = end
    b7 = start
    while b7 <= b5:
        if b10[b7] < b2:
            b10[b6], b10[b7] = b10[b7], b10[b6]
            b6 += 1
            b7 += 1
        elif b10[b7] > b2:
            b10[b7], b10[b5] = b10[b5], b10[b7]
            b5 -= 1
        else:
            b7 += 1
    return b6, b5
def fonk5(size, max_value):
    return [randint(1, max_value) for _ in range(size)]
def fonk6():
    print()
    b8 = int(input("Enter the list size: "))
    print()
    b9 = int(input("Enter the maximum element number (minimum is set at 1): "))
    print("(Hint: the lower the number, the higher the number of duplicate elements to demonstrate the algorithm's speed)")
    print()
    b10 = fonk5(b8, b9)
    b11 = b10[:]
    b12 = b10[:]
    b13 = time()
    fonk1(b11, 0, b8 - 1)
    b14 = time()
    print(f"The number of seconds for the 2-way sort was: {b14 - b13:.8f}")
    b15 = time()
    fonk3(b12, 0, b8 - 1)
    b16 = time()
    print(f"The number of seconds for the 3-way sort was: {b16 - b15:.8f}")
    print()
if b17 = = "__main__":
    fonk6()