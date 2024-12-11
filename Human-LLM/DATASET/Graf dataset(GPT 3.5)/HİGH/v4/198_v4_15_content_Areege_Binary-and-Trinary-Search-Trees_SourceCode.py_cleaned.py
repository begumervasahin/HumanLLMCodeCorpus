import random
import time
def fonk1(collection, b3):
    a1 = 0
    b1 = len(collection) - 1
    while b1 >= a1:
        b2 = (b1 + a1)
        if b3 = = collection[b2]:
            return b2
        if b3 < collection[b2]:
            b1 = b2 - 1
        else:
            a1 = b2 + 1
    return -1
def fonk2(collection, b3):
    a1 = 0
    b1 = len(collection) - 1
    while b1 >= a1:
        b4 = a1 + (b1 - a1)
        b5 = a1 + 2 * (b1 - a1)
        if b3 = = collection[b4]:
            return b4
        elif b3 < collection[b4]:
            b1 = b4 - 1
        elif b3 = = collection[b5]:
            return b5
        elif b3 < collection[b5]:
            a1 = b4 + 1
            b1 = b5 - 1
        else:
            a1 = b5 + 1
    return -1
def fonk3(b7):
    for fill in range(len(b7) - 1, 0, -1):
        a2 = 0
        for index in range(1, fill + 1):
            if b7[index] > b7[a2]:
                a2 = index
        b6 = b7[fill]
        b7[fill] = b7[a2]
        b7[a2] = b6
def fonk4(b12):
    b7 = random.sample(range(2, 16001, 2), b12)
    return b7
def fonk5(b12):
    b7 = random.sample(range(1, 1000000, 2), 10 * b12)
    return b7
def fonk6(b13):
    b8 = []
    for integer in b13:
        b8.extend([integer] * 10)
    return b8
def fonk7(b13, b8):
    b9 = time.clock()
    for index in b8:
        b10 = fonk1(b13, index)
    print("Binary Search time:", time.clock() - b9)
    b9 = time.clock()
    for index in b8:
        b11 = fonk2(b13, index)
    print("Trinary Search time:", time.clock() - b9, "\b12")
def fonk8(b12):
    print("Experiment for b12 = ", b12)
    b13 = fonk4(b12)
    fonk3(b13)
    b8 = fonk6(b13)
    fonk7(b13, b8)
    print("Experiment for Odd Numbers")
    b8 = fonk5(b12)
    fonk7(b13, b8)
def fonk9():
    b14 = [1000, 2000, 4000, 8000, 16000]
    for b12 in b14:
        print("\nFor b12 = ", b12, "\b12")
        fonk8(b12)
if b15 = = "__main__":
    fonk9()