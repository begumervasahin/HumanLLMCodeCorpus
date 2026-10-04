import time
import random
def fonk1(b10):
    if len(b10) > 1:
        b1 = len(b10)
        b2 = b10[:b1]
        b3 = b10[b1:]
        fonk1(b2)
        fonk1(b3)
        b4 = j = k = 0
        while b4 < len(b2) and j < len(b3):
            if b2[b4] < b3[j]:
                b10[k] = b2[b4]
                b4 += 1
            else:
                b10[k] = b3[j]
                j += 1
            k += 1
        while b4 < len(b2):
            b10[k] = b2[b4]
            b4 += 1
            k += 1
        while j < len(b3):
            b10[k] = b3[j]
            j += 1
            k += 1
def fonk2(b10):
    for b4 in range(1, len(b10)):
        b5 = b10[b4]
        b6 = b4
        while b6 > 0 and b10[b6 - 1] > b5:
            b10[b6] = b10[b6 - 1]
            b6 -= 1
        b10[b6] = b5
def fonk3(size, b7 = 1, upper=1000):
    return [random.randint(b7, upper) for _ in range(size)]
def fonk4(sort_function, b10):
    b8 = time.time()
    sort_function(b10)
    return time.time() - b8
def fonk5():
    b9 = [0, 2000, 8000, 32000, 128000, 512000, 1024000, 4096000]
    for size in b9:
        b10 = fonk3(size)
        b11 = fonk4(merge_sort, b10.copy())
        b12 = fonk4(insertion_sort, b10.copy())
        print(f"Array Size: {size}")
        print(f"Merge Sort Time: {b11:.6f} seconds")
        print(f"Insertion Sort Time: {b12:.6f} seconds")
        print("-" * 40)
if b13 = = "__main__":
    fonk5()