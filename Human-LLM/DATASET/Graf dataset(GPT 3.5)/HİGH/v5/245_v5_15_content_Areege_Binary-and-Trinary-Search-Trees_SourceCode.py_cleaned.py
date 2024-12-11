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
def fonk3(a_list):
    for fill in range(len(a_list) - 1, 0, -1):
        a2 = 0
        for index in range(1, fill + 1):
            if a_list[index] > a_list[a2]:
                a2 = index
        a_list[fill], a_list[a2] = a_list[a2], a_list[fill]
def fonk4(b9):
    return random.sample(range(2, 16001, 2), b9)
def fonk5(b9):
    return random.sample(range(1, 1000000, 2), 10 * b9)
def fonk6(b10):
    return [num for num in b10 for _ in range(10)]
def fonk7(b10, b11):
    b6 = time.clock()
    for index in b11:
        b7 = fonk1(b10, index)
    print("Binary Search time:", time.clock() - b6)
    b6 = time.clock()
    for index in b11:
        b8 = fonk2(b10, index)
    print("Trinary Search time:", time.clock() - b6, "\b9")
def fonk8(b9):
    print("Experiment for b9 = ", b9)
    b10 = fonk4(b9)
    fonk3(b10)
    b11 = fonk6(b10)
    fonk7(b10, b11)
    print("Experiment for Odd Numbers")
    b11 = fonk5(b9)
    fonk7(b10, b11)
def fonk9():
    b12 = [1000, 2000, 4000, 8000, 16000]
    for b9 in b12:
        print("\nFor b9 = ", b9, "\b9")
        fonk8(b9)
if b13 = = "__main__":
    fonk9()