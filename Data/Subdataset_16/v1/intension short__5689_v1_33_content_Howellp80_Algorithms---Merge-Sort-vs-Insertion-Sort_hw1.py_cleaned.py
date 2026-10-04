import time
import random
def fonk1(b8):
    if len(b8) > 1:
        b1 = len(b8)
        b2 = b8[:b1]
        b3 = b8[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            if b2[b4] < b3[j]:
                b8[k] = b2[b4]
                b4 += 1
            else:
                b8[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            b8[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            b8[k] = b3[j]
            j += 1
            k += 1
def fonk2(b8):
    for b4 in range(1, len(b8)):
        b5 = b8[b4]
        b6 = b4
        while b6 > 0 and b8[b6 - 1] > b5:
            b8[b6] = b8[b6 - 1]
            b6 -= 1
        b8[b6] = b5
b7 = [2000, 8000, 32000, 128000, 512000, 1024000, 4096000]
for size in b7:
    b8 = [random.randint(1, 1000) for _ in range(size)]
    b9 = time.time()
    fonk1(b8.copy())
    b10 = time.time() - b9
    b9 = time.time()
    fonk2(b8.copy())
    b11 = time.time() - b9
    print(f"Array Size: {size}")
    print(f"Merge Sort Time: {b10:.6f} seconds")
    print(f"Insertion Sort Time: {b11:.6f} seconds")
    print("\n")