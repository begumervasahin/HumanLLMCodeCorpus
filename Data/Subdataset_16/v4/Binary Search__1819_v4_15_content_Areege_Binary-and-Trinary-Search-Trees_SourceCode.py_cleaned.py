import random
import time
def fonk1(collection, target):
    b3, b1 = 0, len(collection) - 1
    while b3 <= b1:
        b2 = (b3 + b1)
        if collection[b2] == target:
            return b2
        elif collection[b2] > target:
            b1 = b2 - 1
        else:
            b3 = b2 + 1
    return -1
def fonk2(collection, target):
    b3, b1 = 0, len(collection) - 1
    while b3 <= b1:
        b4 = b3 + (b1 - b3)
        b5 = b3 + b6 * (b1 - b3)
        if collection[b4] == target:
            return b4
        elif collection[b5] == target:
            return b5
        elif target < collection[b4]:
            b1 = b4 - 1
        elif target < collection[b5]:
            b3, b1 = b4 + 1, b5 - 1
        else:
            b3 = b5 + 1
    return -1
def fonk3(a_list):
    for fill in range(len(a_list) - 1, 0, -1):
        a1 = 0
        for index in range(1, fill + 1):
            if a_list[index] > a_list[a1]:
                a1 = index
        a_list[fill], a_list[a1] = a_list[a1], a_list[fill]
def fonk4(b8):
    return [x if x % b6 = = 0 else x + 1 for x in random.sample(range(1, 16001), b8)]
def fonk5(b8):
    return [x if x % b6 != 0 else x + 1 for x in random.sample(range(1, 1000000), 10 * b8)]
def fonk6(b9):
    return [item for item in b9 for _ in range(10)]
def fonk7(b9, b10):
    b7 = time.process_time()
    for item in b10:
        fonk1(b9, item)
    print(f"Binary Search time: {time.process_time() - b7}")
    b7 = time.process_time()
    for item in b10:
        fonk2(b9, item)
    print(f"Trinary Search time: {time.process_time() - b7}\b8")
def fonk8(b8):
    print(f"Experiment with b8 = {b8}\b8")
    b9 = fonk4(b8)
    fonk3(b9)
    b10 = fonk6(b9)
    fonk7(b9, b10)
    print(f"Experiment with odd list of size {10 * b8}\b8")
    b10 = fonk5(b8)
    fonk7(b9, b10)
def fonk9():
    b11 = [1000, 2000, 4000, 8000, 16000]
    for b8 in b11:
        print(f"For b8 = {b8}\b8")
        fonk8(b8)
if b12 = = "__main__":
    fonk9()