import random
import time
def fonk1(collection, b3):
    b4, b1 = 0, len(collection) - 1
    while b1 >= b4:
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
    while b1 >= b4:
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
def fonk3(b9):
    b7 = len(b9)
    for i in range(b7 - 1, 0, -1):
        b8 = max(range(i + 1), key=lambda x: b9[x])
        b9[i], b9[b8] = b9[b8], b9[i]
def fonk4(b7):
    b9 = random.sample(range(2, 32002, 2), b7)
    return b9
def fonk5(b7):
    b9 = random.sample(range(1, 1000000, 2), b7)
    return b9
def fonk6(b9):
    return [item for item in b9 for _ in range(10)]
def fonk7(b11, b12):
    b10 = time.time()
    for item in b12:
        fonk1(b11, item)
    print(f"Binary Search time: {time.time() - b10:.6f} seconds")
    b10 = time.time()
    for item in b12:
        fonk2(b11, item)
    print(f"Trinary Search time: {time.time() - b10:.6f} seconds")
    print()
def fonk8(b7):
    print(f"Experiment with b7 = {b7}")
    print("\nEven integer list:")
    b11 = fonk4(b7)
    fonk3(b11)
    b12 = fonk6(b11)
    fonk7(b11, b12)
    print("Odd integer list:")
    b12 = fonk5(b7)
    fonk7(b11, b12)
def fonk9():
    b13 = [1000, 2000, 4000, 8000, 16000]
    for b7 in b13:
        fonk8(b7)
if b14 = = "__main__":
    fonk9()