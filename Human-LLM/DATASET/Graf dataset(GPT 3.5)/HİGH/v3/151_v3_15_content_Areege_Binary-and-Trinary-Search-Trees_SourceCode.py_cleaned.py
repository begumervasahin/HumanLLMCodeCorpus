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
def fonk4(b11):
    b6 = random.sample(range(1, 16001), b11)
    for index in range(len(b6)):
        if b6[index] % b7 != 0:
            b6[index] += 1
    return b6
def fonk5(b11):
    b6 = random.sample(range(1, 1000000), 10 * b11)
    for index in range(len(b6)):
        if b6[index] % b7 = = 0:
            b6[index] += 1
    return b6
def fonk6(list1):
    b8 = []
    for integer in list1:
        b8.extend([integer] * 10)
    return b8
def fonk7(search_algorithm, collection, targets):
    b9 = time.process_time()
    for b3 in targets:
        b10 = search_algorithm(collection, b3)
    print(f"{search_algorithm.b16} time:", time.process_time() - b9)
def fonk8(b15):
    for b11 in b15:
        print(f"For b11 = {b11}\b11")
        b12 = fonk4(b11)
        fonk3(b12)
        b13 = fonk6(b12)
        print("Binary Search time:")
        fonk7(binary_search, b12, b13)
        print("Trinary Search time:")
        fonk7(trinary_search, b12, b13)
        print(f"Experiment for b11 (odd list) = {b11}")
        b14 = fonk5(b11)
        fonk7(binary_search, b12, b14)
def fonk9():
    b15 = [1000, 2000, 4000, 8000, 16000]
    fonk8(b15)
if b16 = = "__main__":
    fonk9()