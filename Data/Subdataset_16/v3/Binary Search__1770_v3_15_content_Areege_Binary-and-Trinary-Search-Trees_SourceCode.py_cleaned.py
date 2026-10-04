import random
import time
def fonk1(collection, b3):
    b4, b1 = 0, len(collection) - 1
    while b4 <= b1:
        b2 = (b1 + b4)
        if b3 = = collection[b2]:
            return b2
        elif b3 < collection[b2]:
            b1 = b2 - 1
        else:
            b4 = b2 + 1
    return -1
def fonk2(collection, b3):
    b4, b1 = 0, len(collection) - 1
    while b4 <= b1:
        b5 = b4 + (b1 - b4)
        b6 = b4 + 2 * (b1 - b4)
        if b3 = = collection[b5]:
            return b5
        elif b3 < collection[b5]:
            b1 = b5 - 1
        elif b3 = = collection[b6]:
            return b6
        elif b3 < collection[b6]:
            b4, b1 = b5 + 1, b6 - 1
        else:
            b4 = b6 + 1
    return -1
def fonk3(lst):
    b7 = len(lst)
    for i in range(b7 - 1, 0, -1):
        b8 = max(range(i + 1), key=lambda x: lst[x])
        lst[i], lst[b8] = lst[b8], lst[i]
def fonk4(b7):
    return random.sample(range(2, 32002, 2), b7)
def fonk5(b7):
    return random.sample(range(1, 1000000, 2), b7)
def fonk6(lst):
    return [item for item in lst for _ in range(10)]
def fonk7(lst1, lst2):
    b9 = time.time()
    for item in lst2:
        fonk1(lst1, item)
    b10 = time.time() - b9
    print(f"Binary Search time: {b10:.6f} seconds")
    b9 = time.time()
    for item in lst2:
        fonk2(lst1, item)
    b11 = time.time() - b9
    print(f"Trinary Search time: {b11:.6f} seconds")
    print()
def fonk8(b7):
    print(f"Experiment with b7 = {b7}")
    print("\nEven integer list:")
    b12 = fonk4(b7)
    fonk3(b12)
    b13 = fonk6(b12)
    fonk7(b12, b13)
    print("Odd integer list:")
    b14 = fonk5(b7)
    fonk7(b12, b14)
def fonk9():
    b15 = [1000, 2000, 4000, 8000, 16000]
    for b7 in b15:
        fonk8(b7)
if b16 = = "__main__":
    fonk9()