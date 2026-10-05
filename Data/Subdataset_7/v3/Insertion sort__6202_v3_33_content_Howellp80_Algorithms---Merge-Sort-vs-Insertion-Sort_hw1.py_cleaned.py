import time
import random
def fonk1(b9):
    if len(b9) <= 1:
        return b9
    b1 = len(b9)
    b2 = fonk1(b9[:b1])
    b3 = fonk1(b9[b1:])
    return fonk2(b2, b3)
def fonk2(left, right):
    b4 = []
    b5 = j = 0
    while b5 < len(left) and j < len(right):
        if left[b5] < right[j]:
            b4.append(left[b5])
            b5 += 1
        else:
            b4.append(right[j])
            j += 1
    b4.extend(left[b5:])
    b4.extend(right[j:])
    return b4
def fonk3(b9):
    for b5 in range(1, len(b9)):
        b6 = b9[b5]
        b7 = b5
        while b7 > 0 and b9[b7 - 1] > b6:
            b9[b7] = b9[b7 - 1]
            b7 -= 1
        b9[b7] = b6
b8 = [0, 2000, 8000, 32000, 128000, 512000, 1024000, 4096000]
for size in b8:
    b9 = [random.randint(1, 1000) for _ in range(size)]
    b10 = time.time()
    b11 = fonk1(b9)
    b12 = time.time()
    b13 = b12 - b10
    b14 = time.time()
    fonk3(b9)
    b15 = time.time()
    b16 = b15 - b14
    print("Array Size:", size)
    print("Merge Sort Time:", b13)
    print("Insertion Sort Time:", b16)
    print("\n")