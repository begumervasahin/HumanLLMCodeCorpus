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
def fonk4(b14):
    b6 = random.sample(range(1, 16001), b14)
    for index in range(len(b6)):
        if b6[index] % b7 != 0:
            b6[index] += 1
    return b6
def fonk5(b14):
    b6 = random.sample(range(1, 1000000), 10 * b14)
    for index in range(len(b6)):
        if b6[index] % b7 = = 0:
            b6[index] += 1
    return b6
def fonk6(b12):
    b8 = []
    for integer in b12:
        b8.extend([integer] * 10)
    return b8
def fonk7(b12, b8):
    b9 = time.time()
    for index in b8:
        b10 = fonk1(b12, index)
    print("Binary Search time: {:.6f} seconds".format(time.time() - b9))
    b9 = time.time()
    for index in b8:
        b11 = fonk2(b12, index)
    print("Trinary Search time: {:.6f} seconds".format(time.time() - b9))
    print()
def fonk8(b14):
    print("Experiment with even integer list:")
    b12 = fonk4(b14)
    fonk3(b12)
    b8 = fonk6(b12)
    fonk7(b12, b8)
    print("Experiment with odd integer list:")
    b8 = fonk5(b14)
    fonk7(b12, b8)
def fonk9():
    b13 = [1000, 2000, 4000, 8000, 16000]
    for index in b13:
        print(f"For b14 = {index}\b14")
        fonk8(index)
if b15 = = "__main__":
    fonk9()