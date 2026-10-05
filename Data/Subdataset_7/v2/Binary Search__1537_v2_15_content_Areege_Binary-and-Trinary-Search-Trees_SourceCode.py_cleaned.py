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
        b5 = a1 + b7 * (b1 - a1)
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
def fonk3(b6):
    for fill in range(len(b6) - 1, 0, -1):
        a2 = 0
        for index in range(1, fill + 1):
            if b6[index] > b6[a2]:
                a2 = index
        b6[fill], b6[a2] = b6[a2], b6[fill]
def fonk4(b12):
    b6 = random.sample(range(1, 16001), b12)
    for index in range(len(b6)):
        if b6[index] % b7 != 0:
            b6[index] += 1
    return b6
def fonk5(b12):
    b6 = random.sample(range(1, 1000000), 10 * b12)
    for index in range(len(b6)):
        if b6[index] % b7 = = 0:
            b6[index] += 1
    return b6
def fonk6(b13):
    b8 = []
    for integer in b13:
        b8.extend([integer] * 10)
    return b8
def fonk7(b13, b8):
    b9 = time.process_time()
    for index in b8:
        b10 = fonk1(b13, index)
    print("Binary Search time:", time.process_time() - b9)
    b9 = time.process_time()
    for index in b8:
        b11 = fonk2(b13, index)
    print("Trinary Search time:", time.process_time() - b9, "\b12")
def fonk8(b14):
    for b12 in b14:
        print("For b12 = ", b12, "\b12")
        b13 = fonk4(b12)
        fonk3(b13)
        b8 = fonk6(b13)
        fonk7(b13, b8)
        print("Experiment for b12 (odd list) =", b12)
        b8 = fonk5(b12)
        fonk7(b13, b8)
def fonk9():
    b14 = [1000, 2000, 4000, 8000, 16000]
    fonk8(b14)
if b15 = = "__main__":
    fonk9()