import time
import random
def fonk1(b7):
    if len(b7) <= 1:
        return
    b1 = len(b7)
    b2 = b7[:b1]
    b3 = b7[b1:]
    fonk1(b2)
    fonk1(b3)
    fonk2(b7, b2, b3)
def fonk2(b7, b2, b3):
    b4 = j = k = 0
    while b4 < len(b2) and j < len(b3):
        if b2[b4] < b3[j]:
            b7[k] = b2[b4]
            b4 += 1
        else:
            b7[k] = b3[j]
            j += 1
        k += 1
    while b4 < len(b2):
        b7[k] = b2[b4]
        b4 += 1
        k += 1
    while j < len(b3):
        b7[k] = b3[j]
        j += 1
        k += 1
def fonk3(b7):
    for b4 in range(1, len(b7)):
        b5 = b7[b4]
        b6 = b4
        while b6 > 0 and b7[b6 - 1] > b5:
            b7[b6] = b7[b6 - 1]
            b6 -= 1
        b7[b6] = b5
def fonk4(b11):
    for size in b11:
        b7 = [random.randint(1, 1000) for _ in range(size)]
        b8 = fonk5(merge_sort, b7)
        b9 = fonk5(insertion_sort, b7)
        fonk6(size, b8, b9)
def fonk5(sort_function, b7):
    b10 = time.time()
    sort_function(b7.copy())
    return time.time() - b10
def fonk6(size, b8, b9):
    print(f"Array Size: {size}")
    print(f"Merge Sort Time: {b8:.6f} seconds")
    print(f"Insertion Sort Time: {b9:.6f} seconds")
    print("-" * 40)
b11 = [2000, 8000, 32000, 128000, 512000, 1024000, 4096000]
fonk4(b11)