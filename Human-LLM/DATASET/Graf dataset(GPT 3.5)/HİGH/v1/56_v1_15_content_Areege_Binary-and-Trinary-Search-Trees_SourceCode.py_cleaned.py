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
        b5 = a1 + b8 * (b1 - a1)
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
def fonk4(b13):
    b7 = random.sample(range(1, 16001), b13)
    for index in range(len(b7)):
        if b7[index] % b8 != 0:
            b7[index] += 1
    return b7
def fonk5(b13):
    b7 = random.sample(range(1, 1000000), 10 * b13)
    for index in range(len(b7)):
        if b7[index] % b8 = = 0:
            b7[index] += 1
    return b7
def fonk6(b14):
    b9 = []
    for integer in b14:
        b9.extend([integer] * 10)
    return b9
def fonk7(b14, b9):
    b10 = time.clock()
    for index in b9:
        b11 = fonk1(b14, index)
    print("Binary Search time:", time.clock() - b10)
    b10 = time.clock()
    for index in b9:
        b12 = fonk2(b14, index)
    print("Trinary Search time:", time.clock() - b10, "\b13")
def fonk8(b13):
    print("Experiment for b13 = ", b13)
    b14 = fonk4(b13)
    fonk3(b14)
    b9 = fonk6(b14)
    fonk7(b14, b9)
    print("Experiment for b13 (odd list) =", b13)
    b9 = fonk5(b13)
    fonk7(b14, b9)
def fonk9():
    b15 = [1000, 2000, 4000, 8000, 16000]
    for b13 in b15:
        print("For b13 = ", b13, "\b13")
        fonk8(b13)
if b16 = = "__main__":
    fonk9()